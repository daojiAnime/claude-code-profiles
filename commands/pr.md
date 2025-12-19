---
description: Clean up code, stage changes, and prepare a pull request
---

Please help me prepare a pull request by:

1. First, check for any linting or formatting tools in the project (like ESLint, Prettier, or similar)
2. Run the appropriate code cleanup/formatting commands if they exist
3. Show me what files have been changed with `git status`
4. Stage all the changes with `git add .`
5. Review the staged changes with `git diff --staged`
6. Create a well-formatted commit with an appropriate message based on the changes
7. Push the branch to the remote repository
8. Create a pull request using `gh pr create` with a summary of the changes

Make sure to:
- Use existing project conventions for formatting/linting
- Write a clear, concise commit message following the project's commit style
- Include a comprehensive PR description with a summary and test plan
- Handle cases where the branch may not have a remote tracking branch yet
