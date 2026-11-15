# Mission 6 — Git and GitHub

**Goal:** understand version control and practice the basic local Git workflow safely.

## 1. Key ideas

- **Git** is a version-control system that records changes to files.
- A **repository** is a project tracked by Git.
- A **commit** is a saved snapshot with a message.
- A **branch** is an independent line of development.
- **GitHub** hosts Git repositories online and adds collaboration features.
- A **remote** is a named reference to another repository, often on GitHub.
- A **pull request** proposes changes so they can be reviewed and merged.

## 2. Check Git

In Terminal:

```bash
git --version
git config --global user.name
git config --global user.email
```

If name or email is not configured, set the name and an email you are comfortable associating with commits:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use your own details; do not publish private account information in this assignment.

## 3. Practice in a safe folder

The following commands create a small practice repository in your home folder. They do not modify this assignment repository.

```bash
mkdir -p ~/git-practice
cd ~/git-practice
git init
printf "My first Git note
" > notes.txt
git status
git add notes.txt
git status
git commit -m "Add first practice note"
git log --oneline
```

What happened?
1. `git init` created a local repository.
2. `git status` showed the working-tree state.
3. `git add` staged the file for the next commit.
4. `git commit` saved the staged change.
5. `git log --oneline` displayed a compact commit history.

Edit `notes.txt`, then repeat:

```bash
printf "A second line
" >> notes.txt
git diff
git add notes.txt
git commit -m "Add second note"
git log --oneline
```

## 4. Branch practice

```bash
git switch -c practice-branch
git branch
```

A branch lets you work on a change without immediately changing another branch. Return to the default branch name shown by `git branch` when finished; do not guess its name.

## 5. Connect to GitHub

For an existing GitHub repository, the remote is commonly named `origin`:

```bash
git remote -v
```

If you have cloned a repository, its remote is usually configured already. For a new local repository, add the URL of a repository you own or are authorized to use:

```bash
git remote add origin https://github.com/OWNER/REPOSITORY.git
```

Then check the branch name and remote before pushing. A typical first push is:

```bash
git push -u origin main
```

Only use `main` if that is actually your local branch and the remote is ready for the push. If authentication is requested, use GitHub's supported sign-in flow or credential manager; never paste a password or token into this README.

To download remote updates, use `git pull`. A pull fetches and integrates remote changes into the current branch.

## 6. Pull requests

A pull request is a GitHub collaboration feature. A contributor pushes a branch and opens a request to merge it into another branch. Reviewers can inspect the changes, discuss them, request updates and approve the merge.

## 7. Command reference

| Command | Purpose |
|---|---|
| `git status` | Show changed, staged and untracked files |
| `git add FILE` | Stage a file |
| `git commit -m "message"` | Save staged changes |
| `git log --oneline` | Show compact commit history |
| `git diff` | Show unstaged changes |
| `git branch` | List branches |
| `git switch -c NAME` | Create and switch to a branch |
| `git remote -v` | Show remote URLs |
| `git pull` | Fetch and integrate remote changes |
| `git push` | Send local commits to a remote |

## Experiment log

| Command I ran | What it displayed or changed |
|---|---|
| `git status` |  |
| `git add` and `git commit` |  |
| `git log --oneline` |  |
| Branch command |  |

## Reflection

- How is a commit different from saving a file?
- Why should commit messages describe the change?
- What is one benefit of using a branch?
- What is the difference between Git and GitHub?

## Completion checklist

- [ ] Checked Git version and configuration.
- [ ] Created a safe practice repository.
- [ ] Staged and committed a file.
- [ ] Viewed commit history and tried a branch.
- [ ] Explained remote, push, pull and pull request.
- [ ] Completed my own experiment log and reflection.

**Safety:** Never commit passwords, API keys, access tokens, private keys or sensitive personal data. Check `git status` before committing.
