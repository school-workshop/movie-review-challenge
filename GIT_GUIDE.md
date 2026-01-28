# Git & GitHub Guide for Beginners

A simple guide to help you get started with Git and GitHub.

---

## What is Git?

**Git** is a version control system that tracks changes to your code. Think of it like "save points" in a video game - you can save your progress and go back if something goes wrong.

## What is GitHub?

**GitHub** is a website that stores your Git projects online. It lets you:
- Back up your code in the cloud
- Share code with others
- Collaborate on projects
- Show off your work to employers

---

## Getting Started

### 1. Install Git

**Windows:**
1. Download from [git-scm.com](https://git-scm.com/download/win)
2. Run the installer (use default settings)
3. Open "Git Bash" from Start menu

**Mac:**
```bash
# Open Terminal and run:
xcode-select --install
```

**Linux:**
```bash
sudo apt install git
```

### 2. Configure Git (First Time Only)

Open your terminal and set your name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 3. Create a GitHub Account

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Choose a username, enter your email, create a password
4. Verify your email

---

## Essential Git Commands

### Clone a Repository (Download Code)

```bash
git clone https://github.com/school-workshop/movie-review-challenge.git
```

This downloads the project to your computer.

### Check Status

```bash
git status
```

Shows which files have been changed.

### Stage Changes (Prepare to Save)

```bash
# Add a specific file
git add filename.py

# Add all changed files
git add .
```

### Commit (Save Your Progress)

```bash
git commit -m "Describe what you changed"
```

Good commit messages:
- ✅ "Add search functionality"
- ✅ "Fix bug in rating calculation"
- ❌ "Updated stuff"
- ❌ "asdfasdf"

### Push (Upload to GitHub)

```bash
git push
```

Sends your commits to GitHub.

### Pull (Download Latest Changes)

```bash
git pull
```

Gets the latest code from GitHub.

---

## Common Workflows

### Workflow 1: Working on an Existing Project

```bash
# 1. Clone the project
git clone https://github.com/username/project.git
cd project

# 2. Make your changes in the code editor

# 3. Check what changed
git status

# 4. Stage your changes
git add .

# 5. Commit with a message
git commit -m "Complete challenge 2"

# 6. Push to GitHub
git push
```

### Workflow 2: Create a New Project

```bash
# 1. Create a folder and go into it
mkdir my-project
cd my-project

# 2. Initialize Git
git init

# 3. Create some files
echo "# My Project" > README.md

# 4. Stage and commit
git add .
git commit -m "Initial commit"

# 5. Create repo on GitHub, then connect and push
git remote add origin https://github.com/yourusername/my-project.git
git branch -M main
git push -u origin main
```

---

## Forking (Make Your Own Copy)

Forking creates your own copy of someone else's project on GitHub.

### How to Fork:

1. Go to the repository on GitHub
2. Click the **"Fork"** button (top right)
3. Select your account
4. You now have your own copy!

### Clone Your Fork:

```bash
git clone https://github.com/YOUR-USERNAME/movie-review-challenge.git
```

---

## Branching (Work on Features Separately)

Branches let you work on new features without affecting the main code.

```bash
# Create and switch to a new branch
git checkout -b my-new-feature

# Make changes, then commit
git add .
git commit -m "Add new feature"

# Push the branch to GitHub
git push -u origin my-new-feature

# Switch back to main branch
git checkout main
```

---

## Fixing Common Problems

### "I made changes to the wrong branch"

```bash
# Stash (temporarily save) your changes
git stash

# Switch to the correct branch
git checkout correct-branch

# Apply your changes
git stash pop
```

### "I want to undo my last commit"

```bash
# Undo commit but keep changes
git reset --soft HEAD~1

# Undo commit and discard changes (careful!)
git reset --hard HEAD~1
```

### "I have merge conflicts"

When Git can't automatically merge changes:

1. Open the file with conflicts
2. Look for markers like `<<<<<<`, `======`, `>>>>>>`
3. Edit the file to keep the code you want
4. Remove the conflict markers
5. Stage and commit:
   ```bash
   git add .
   git commit -m "Resolve merge conflicts"
   ```

### "My push was rejected"

```bash
# Pull the latest changes first
git pull

# Then push again
git push
```

---

## Git Cheat Sheet

| Command | What it does |
|---------|--------------|
| `git clone <url>` | Download a repository |
| `git status` | See changed files |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Save changes with a message |
| `git push` | Upload to GitHub |
| `git pull` | Download latest changes |
| `git log` | View commit history |
| `git branch` | List branches |
| `git checkout -b name` | Create new branch |
| `git checkout main` | Switch to main branch |

---

## GitHub Features

### README.md

A `README.md` file appears on your repository's main page. Use it to:
- Describe your project
- Explain how to install/run it
- Show examples

### Issues

Use Issues to:
- Track bugs
- Plan new features
- Ask questions

### Pull Requests

Pull Requests (PRs) let you propose changes:
1. Fork the repo
2. Make changes in your fork
3. Click "New Pull Request"
4. Describe your changes
5. Submit for review

---

## Tips for Success

1. **Commit often** - Small, frequent commits are better than big ones
2. **Write clear messages** - Your future self will thank you
3. **Pull before you push** - Avoid conflicts by staying up to date
4. **Don't commit secrets** - Never commit passwords or API keys
5. **Use .gitignore** - Exclude files you don't want to track

---

## Learn More

- [GitHub Skills](https://skills.github.com/) - Free interactive courses
- [Git Documentation](https://git-scm.com/doc) - Official docs
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fixing common mistakes

---

Happy coding! 🚀
