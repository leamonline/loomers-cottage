# P2.1.0 source import

All five SHA-256 entries in the original release archive matched. The archive’s consolidated specification matched the workspace copy byte for byte. Both approved choice registers agree with the 66 choices in the repository edition.

| Repository artifact | Source and verification |
|---|---|
| [Lab module](../lab/p21/loomers-lab-p21.js) | Exact archived component, including its seven synthetic scenarios. Its checksum matches the upstream manifest. |
| [HTML preview](../lab/p21/preview.html) | Exact archived wrapper. Its checksum was recorded during this import. |
| [Python acceptance harness](../tests/p21/acceptance.py) | Archive assertion logic with portable paths and browser launch, blocked network transport, and console results. |
| [Historical test report](p21-upstream-results.json) | Exact archived JSON with 120 passing assertions. Its checksum matches the upstream manifest. |
| [Consolidated specification](../docs/technical-specification-v2.1.md) | Repository edition with live bindings, baselines and instance-specific deployment details removed. |
| [Release checksums](p21.sha256) | Repository paths for the component, HTML wrapper and upstream historical report. |

The archive’s deployment patch and live manifest were inspected privately. Their configuration fingerprints, exact target, baseline and recovery details belong in private owner-controlled storage.

Home Assistant deployment belongs to issue #6 and requires verified G0 recovery, fresh fingerprints, exact target and diff, and separate approval. Keep the native fallback and verify the existing Lab routes and resources before any promotion.
