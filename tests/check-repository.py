"""Check tracked files without writing suspected sensitive values to logs."""

import hashlib
import re
import subprocess
from urllib.parse import urlsplit

PREVIEW = "lab/p21/preview.html"
SPEC = "docs/technical-specification-v2.1.md"
INDEX = "docs/decisions.md"
CHECKSUM = "releases/p21-preview.sha256"
PUBLIC_HOSTS = {
    "developers.home-assistant.io",
    "registry.npmjs.org",
    "www.home-assistant.io",
}

BLOCKED_PATH = re.compile(
    r"(^|/)(?:\.mcp\.json|\.env(?:\.[^/]+)?|\.storage|backups|private|local|"
    r"secrets\.ya?ml)(?:/|$)|"
    r"\.(?:p8|pem|key|p12|zip|tar(?:\.gz)?|sqlite\w*|db(?:-\w+)?|har|csv)$",
    re.IGNORECASE,
)
PATTERNS = {
    "credential": r"-----BEGIN [A-Z ]*PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|"
    r"github_pat_[A-Za-z0-9_]{20,}|eyJ[\w-]+\.eyJ[\w-]+\.[\w-]+|"
    r"(?:api[_-]?key|password|access[_-]?token|client[_-]?secret)"
    r"""\s*["']?\s*[:=]\s*["'][^"'\s]{8,}["']""",
    "local host or address": r"\b(?:10|192\.168|172\.(?:1[6-9]|2\d|3[01]))"
    r"(?:\.\d{1,3}){2,3}\b|\b[\w-]+\.(?:local|lan|internal|home\.arpa)\b|"
    r"(?i:\b[A-Z]{1,2}\d[A-Z\d]?\s+\d[A-Z]{2}\b)",
    "live entity identifier": r"\b(?:automation|binary_sensor|button|calendar|camera|climate|"
    r"cover|device_tracker|event|fan|image|input_boolean|input_datetime|input_select|"
    r"light|lock|media_player|person|scene|sensor|switch|tts|weather)\.[a-z0-9_]+\b",
    "account or vehicle identifier": r"\b(?:[A-HJ-NPR-Z0-9]{17}|\d{13,})\b|"
    r"\b(?:[0-9a-f]{16}|[0-9a-f]{32})\b|\b(?:[0-9a-f]{2}:){5}[0-9a-f]{2}\b",
    "hook endpoint": r"/api/(?:webhook|websocket)(?:\b|/)",
}


def index_files():
    records = subprocess.check_output(["git", "ls-files", "--stage", "-z"]).split(b"\0")
    for record in filter(None, records):
        metadata, filename = record.split(b"\t", 1)
        mode, object_id, stage = metadata.decode().split()
        path = filename.decode()
        if stage != "0" or mode not in {"100644", "100755"}:
            raise SystemExit(f"Non-regular or unresolved Git entry: {path}")
        data = subprocess.check_output(["git", "cat-file", "blob", object_id])
        yield path, data


def main():
    files = dict(index_files())
    failures = []
    for path, data in files.items():
        if BLOCKED_PATH.search(path) or b"\0" in data:
            failures.append(f"{path}: blocked file type or path")
            continue
        for number, line in enumerate(data.decode().splitlines(), 1):
            if path == "tests/check-repository.py":
                # The checker contains the detection patterns.
                continue
            for label, pattern in PATTERNS.items():
                if re.search(pattern, line):
                    failures.append(f"{path}:{number}: suspected {label}")
            for url in re.findall(r"""https?://[^\s<>)"'`]+""", line):
                link = urlsplit(url)
                if (link.scheme != "https" or link.hostname not in PUBLIC_HOSTS
                        or link.username or link.password or link.query):
                    failures.append(f"{path}:{number}: URL outside approved public sources")
    if failures:
        raise SystemExit("\n".join(failures))

    expected = {f"{prefix}{number:02}" for prefix in "OP" for number in range(1, 34)}
    for path in (SPEC, INDEX):
        ids = re.findall(rb"^\| ([OP]\d{2}) \|", files[path], re.MULTILINE)
        if len(ids) != len(expected) or {item.decode() for item in ids} != expected:
            raise SystemExit(f"{path}: expected each of the 66 decision IDs exactly once")

    digest = hashlib.sha256(files[PREVIEW]).hexdigest()
    if files[CHECKSUM].decode() != f"{digest}  {PREVIEW}\n":
        raise SystemExit("Standalone preview checksum mismatch")
    scripts = re.findall(rb"<script>(.*?)</script>", files[PREVIEW], re.DOTALL)
    if len(scripts) != 1:
        raise SystemExit("Expected one inline preview script")
    subprocess.run(["node", "--check"], input=scripts[0], check=True)
    print(f"Privacy patterns checked in {len(files)} tracked files")
    print("66 decision IDs verified in the specification and index")
    print("Standalone preview SHA-256 and JavaScript syntax verified")


if __name__ == "__main__":
    main()
