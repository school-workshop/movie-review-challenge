# IT Setup Guide for Workshop Computers

**Workshop:** Movie Review App - Python Workshop
**Duration:** 2 hours 45 minutes
**Students per room:** ~20

---

## Overview

This guide helps IT teams prepare computers before the workshop. Students will build a web application using Python, FastAPI, and SQLite.

---

## Required Software

Please install the following on all student computers:

### 1. Python 3.8 or higher

**Download:** https://www.python.org/downloads/

**Windows Installation:**
1. Download Python 3.x.x (latest stable version)
2. Run the installer
3. **IMPORTANT:** Check ✅ "Add Python to PATH" on the first screen
4. Click "Install Now"
5. Verify installation:
   ```
   Open Command Prompt → type: python --version
   Expected output: Python 3.x.x
   ```

**Mac Installation:**
1. Download Python 3.x.x from python.org
2. Open the .pkg file and follow prompts
3. Verify installation:
   ```
   Open Terminal → type: python3 --version
   Expected output: Python 3.x.x
   ```

---

### 2. Visual Studio Code (VS Code)

**Download:** https://code.visualstudio.com/

**Installation:**
1. Download VS Code for your operating system
2. Run the installer with default settings
3. Launch VS Code after installation

**Required Extension:**
1. Open VS Code
2. Click the Extensions icon (left sidebar) or press `Ctrl+Shift+X`
3. Search for "Python"
4. Install **"Python"** by Microsoft (first result)

**Optional but Recommended Extensions:**
- "Pylance" - Better Python language support
- "SQLite Viewer" - View database files

---

### 3. Git (Optional but Recommended)

**Download:** https://git-scm.com/downloads

**Windows Installation:**
1. Download Git for Windows
2. Run installer with default settings
3. Verify: Open Command Prompt → type: `git --version`

**Mac Installation:**
```
Open Terminal → type: xcode-select --install
```

---

## Network Requirements

Please ensure the following URLs are **not blocked** by firewalls:

| URL | Purpose |
|-----|---------|
| `github.com` | Download workshop code |
| `raw.githubusercontent.com` | GitHub raw files |
| `pypi.org` | Python package installation |
| `files.pythonhosted.org` | Python package downloads |
| `python.org` | Python documentation |

**Ports Required:**
- Port 443 (HTTPS)
- Port 80 (HTTP)
- Port 8000 (localhost for running the app)

---

## Pre-Workshop Setup (Optional)

To save time during the workshop, you can pre-download the project:

### Option A: Download as ZIP
1. Go to: https://github.com/school-workshop/movie-review-challenge
2. Click green "Code" button → "Download ZIP"
3. Extract to each computer's Desktop or Documents folder

### Option B: Clone with Git
```bash
git clone https://github.com/school-workshop/movie-review-challenge.git
```

### Pre-install Python Dependencies (Recommended)
This saves ~5 minutes per student during the workshop:

```bash
cd movie-review-challenge
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

---

## Verification Checklist

Run these checks on one computer to verify setup:

| Check | Command | Expected Result |
|-------|---------|-----------------|
| Python installed | `python --version` | Python 3.8+ |
| pip installed | `pip --version` | pip 2x.x.x |
| VS Code installed | Open VS Code | App launches |
| Python extension | VS Code → Extensions | "Python" shows as installed |
| Network access | Browse to github.com | Page loads |

---

## Folder Structure After Setup

```
Desktop/
└── movie-review-challenge/
    ├── README.md
    ├── STUDENT_CHALLENGES.md
    ├── GIT_GUIDE.md
    ├── database.py          ← Students edit this file
    ├── main.py
    ├── movies.db
    ├── requirements.txt
    ├── templates/
    └── static/
```

---

## Common Issues & Solutions

### Issue: "Python is not recognized"
**Cause:** Python not added to PATH
**Fix:** Reinstall Python and check "Add Python to PATH"

### Issue: "pip is not recognized"
**Cause:** Python Scripts folder not in PATH
**Fix:**
- Windows: Add `C:\Users\<username>\AppData\Local\Programs\Python\Python3x\Scripts` to PATH
- Or reinstall Python with PATH option checked

### Issue: "Access denied" when installing packages
**Cause:** Insufficient permissions
**Fix:** Run Command Prompt as Administrator

### Issue: Cannot access github.com
**Cause:** Firewall blocking
**Fix:** Whitelist github.com and related domains (see Network Requirements)

### Issue: VS Code doesn't recognize Python
**Cause:** Python extension not installed or wrong interpreter
**Fix:**
1. Install Python extension
2. Press `Ctrl+Shift+P` → "Python: Select Interpreter"
3. Choose the installed Python version

---

## Hardware Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| RAM | 4 GB | 8 GB |
| Storage | 500 MB free | 1 GB free |
| Display | 1280x720 | 1920x1080 |
| Internet | Required | Required |

---

## Workshop Day Quick Reference

**Students will run these commands:**

```bash
# 1. Navigate to project folder
cd movie-review-challenge

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
uvicorn main:app --reload

# 6. Open browser to:
http://127.0.0.1:8000
```

---

## Support Contact

If you have questions about the setup, please contact the workshop organizer before the event.

---

**Thank you for helping prepare the computers!**
