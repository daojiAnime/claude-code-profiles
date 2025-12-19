---
description: Read all changed files in the current git branch
---

Please help me catch up on the changes in my current git branch by:

1. First, run `git diff --name-only $(git merge-base HEAD origin/main)..HEAD` to get all changed files compared to the main branch (or use `origin/master` if main doesn't exist)
2. Read all the changed files that were found
3. Provide a brief summary of what has changed across these files

Make sure to handle the case where the branch might be based on `master` instead of `main`.
