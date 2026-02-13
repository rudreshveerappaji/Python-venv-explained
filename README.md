# Python-venv-explained
An illustration of the use of virtual environments (venv) in Python with examples

This repo is a hands-on exercise to learn **Python virtual environments (venv)** and how to **switch cleanly between two projects** that need different dependency versions.

## 1) What is `venv`?

A **virtual environment** is an **isolated Python + installed packages** area for a single project.

- It prevents dependency/version conflicts between projects.
- When activated, `python` and `pip` in your terminal point to the project’s environment (not your global/system Python).
- `deactivate` only *turns it off* for the current terminal session — it **does not delete** the `venv/` folder.

Think of it like:
- `activate` = “use this project’s Python + packages”
- `deactivate` = “go back to system Python”
- deleting the `venv/` folder = “remove the environment entirely”

---

## 2) Repo Layout

```
venv-switching-demo/
├─ projectA/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ .gitignore
├─ projectB/
│  ├─ app.py
│  ├─ requirements.txt
│  └─ .gitignore
├─ .gitignore
└─ README.md
```

- **Project A** installs `requests==2.25.1`
- **Project B** installs `requests==2.31.0`

Each project has its own `venv/` folder (created locally by you).

---

## 3) Prerequisites

- Python 3.9+ installed
- Windows PowerShell or Command Prompt (instructions below)

Verify Python:

```bat
python --version
```

---

## 4) Exercise: Create + Run Project A

From the repo root:

```bat
cd projectA
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

✅ Example output you should see:

```
=== Project A ===
Python executable: C:\...\projectA\venv\Scripts\python.exe
requests version : 2.25.1
If you activate Project B later, you should see a different requests version.
```

Deactivate:

```bat
deactivate
```

Your prompt will lose the `(venv)` prefix.

---

## 5) Exercise: Create + Run Project B

```bat
cd ..\projectB
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

✅ Example output you should see:

```
=== Project B ===
Python executable: C:\...\projectB\venv\Scripts\python.exe
requests version : 2.31.0
If you activate Project A later, you should see a different requests version.
```

Deactivate:

```bat
deactivate
```

---

## 6) Switching Between the Two Projects (the key lesson)

**Switch B → A**

```bat
cd ..\projectA
venv\Scripts\activate
python app.py
deactivate
```

**Switch A → B**

```bat
cd ..\projectB
venv\Scripts\activate
python app.py
deactivate
```

You’ll see the `requests` version flip based on which venv is active.

---

## 7) Notes: What gets committed to Git?

- ✅ Commit: `app.py`, `requirements.txt`, `README.md`
- ❌ Do **NOT** commit: `venv/` (it’s machine-specific and can be huge)

This repo includes `.gitignore` rules that prevent `venv/` from being committed.

---

## 8) (Optional) Mac/Linux commands

Activation is different:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
deactivate
```

---

## 9) Troubleshooting

### PowerShell “running scripts is disabled”
If you get an execution policy error when activating:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then try:

```powershell
.\venv\Scripts\Activate.ps1
```

(You can revert later if you want.)

---

Enjoy — this is the cleanest way to **avoid dependency conflicts** across projects.

