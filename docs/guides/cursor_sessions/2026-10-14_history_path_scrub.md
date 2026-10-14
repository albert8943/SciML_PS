# 2026-10-14 — History scrub of local machine paths

## Why

Before making `SciML_PS` public, remove absolute local paths from **all** reachable commits (latest tree was already redacted; older commits still held paths).

## Backup

Local bundle kept only on the maintainer machine (pre-rewrite snapshot). Not committed.

Pre-rewrite tip and `v0.1.0` SHAs recorded only in that private backup note.

## Method

`git-filter-repo --replace-text` with literals:

| Old (pattern) | New |
|---------------|-----|
| Absolute Obsidian vault path under a local sync folder | maintainer's local Obsidian vault (path not recorded in this public repo) |
| Absolute website-repo `open_resources.yaml` path | `<website-repo>/data/open_resources.yaml` |
| Absolute clone path for this repo | `<SciML_PS clone root>` |
| Wording "Local OneDrive path…" in secrets review | `Local machine path…` |

## After

- Tip and annotated tag `v0.1.0` rewritten
- Verified: no former absolute machine paths remain in any commit blob
- Remote updated with force-push of `master` and `v0.1.0` (when authorized)

## Note

Anyone who already cloned the pre-scrub history should re-clone or hard-reset to the new `origin/master`. No other remotes/forks expected yet (repo still private at scrub time).
