# | Command                                  | Purpose                                                           |
# | ---------------------------------------- | ----------------------------------------------------------------- |
# | `git init`                               | Initialize a new Git repository.                                  |
# | `git clone <repository-url>`             | Copy an existing repository to your computer.                     |
# | `git status`                             | Show the current status of files.                                 |
# | `git add <file>`                         | Stage a specific file.                                            |
# | `git add .`                              | Stage all changed files.                                          |
# | `git commit -m "Your message"`           | Save staged changes with a message.                               |
# | `git log`                                | View commit history.                                              |
# | `git log --oneline`                      | View a compact commit history.                                    |
# | `git diff`                               | Show unstaged changes.                                            |
# | `git diff --staged`                      | Show staged changes.                                              |
# | `git branch`                             | List branches.                                                    |
# | `git branch <branch-name>`               | Create a new branch.                                              |
# | `git checkout <branch-name>`             | Switch branches.                                                  |
# | `git switch <branch-name>`               | Modern way to switch branches.                                    |
# | `git switch -c <branch-name>`            | Create and switch to a new branch.                                |
# | `git merge <branch-name>`                | Merge a branch into the current branch.                           |
# | `git remote -v`                          | List configured remote repositories.                              |
# | `git remote add origin <repository-url>` | Add a remote repository.                                          |
# | `git push origin main`                   | Push changes to the remote repository.                            |
# | `git pull origin main`                   | Download and merge changes from the remote.                       |
# | `git fetch`                              | Download remote changes without merging.                          |
# | `git stash`                              | Save uncommitted changes temporarily.                             |
# | `git stash pop`                          | Restore stashed changes.                                          |
# | `git reset --soft HEAD~1`                | Undo the last commit but keep changes staged.                     |
# | `git reset --hard HEAD~1`                | Remove the last commit and discard changes. **Use with caution.** |
# | `git restore <file>`                     | Discard changes in a file.                                        |
# | `git restore --staged <file>`            | Unstage a file.                                                   |
# | `git rm <file>`                          | Remove a file from Git and your working directory.                |
# | `git mv <old> <new>`                     | Rename or move a file.                                            |
# | `git tag`                                | List tags.                                                        |
# | `git tag <tag-name>`                     | Create a tag.                                                     |

# # Clone a repository
# git clone https://github.com/username/project.git

# # Go into the project
# cd project

# # Check status
# git status

# # Create a new branch
# git switch -c feature/login

# # Make changes...

# # Stage changes
# git add .

# # Commit
# git commit -m "Add login feature"

# # Push the branch
# git push -u origin feature/login

# # Switch back to main
# git switch main

# # Pull latest changes
# git pull origin main

# # Merge your feature
# git merge feature/login

# # Push updated main
# git push origin main

# # Configure your identity
# git config --global user.name "Your Name"
# git config --global user.email "you@example.com"

# # Check configuration
# git config --list

# # Add GitHub remote
# git remote add origin https://github.com/username/repository.git

# # Verify remote
# git remote -v

# # Push for the first time
# git push -u origin main

# git status                 # Check repository status
# git log --oneline          # View commit history
# git remote -v              # Show remotes
# git branch                 # Show local branches
# git branch -a              # Show all branches
# git fetch                  # Fetch remote changes
# git pull                   # Pull latest changes
# git push                   # Push commits
# # Unstage a file
# git restore --staged file.txt

# # Discard changes in a file
# git restore file.txt

# # Undo the last commit (keep changes)
# git reset --soft HEAD~1

# # Undo the last commit (delete changes)
# git reset --hard HEAD~1