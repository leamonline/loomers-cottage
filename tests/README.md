# Tests
Synthetic fixtures, browser regression, keyboard/focus, reduced motion, unknown/stale data, restart, manual override and Apple-device checks. Prior local P2.1 results reported; import actual test source/results after review.

## Standalone P2.1 preview

With Node.js 24 and Python 3, run:

```sh
npm ci
npx playwright install chromium
python3 tests/check-repository.py
npm test
```

The repository check reads Git’s index. Stage candidate edits to check the exact bytes before committing. It verifies tracked file privacy patterns, the 66 decision IDs, the standalone preview checksum and inline JavaScript syntax.

The new Chromium suite exercises the standalone preview at four viewport widths and both colour schemes. It starts from in-memory HTML and aborts network requests. Live Home Assistant, Apple hardware, performance, recovery and the original archive harness have separate acceptance criteria.
