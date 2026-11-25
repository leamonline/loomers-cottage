# Tests

## P2.1 fixture acceptance

The archive suite replays 120 assertions. The supplemental Chromium suite checks theme, room details, keyboard/focus, and eleven internal routes at four viewport widths in both colour schemes. Both use the archived component and synthetic fixtures in memory, with outbound browser requests blocked.

With Node.js 24 and Python 3, run the following from the repository root:

```sh
npm ci
npx playwright install chromium
python3 -m venv .venv
.venv/bin/python -m pip install -r tests/p21/requirements.txt
python3 tests/check-repository.py
.venv/bin/python tests/p21/acceptance.py
npm test
```

The repository check reads Git’s index. Stage candidate edits to check the exact bytes before committing. It verifies privacy patterns, 66 approved choices, checksums, the archived result count and JavaScript syntax.

Live Home Assistant, Apple hardware, performance, restart and recovery have separate acceptance criteria.
