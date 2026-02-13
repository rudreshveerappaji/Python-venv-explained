"""
projectA - venv demo

This file demonstrates WHY virtual environments matter.

Key points:
1) Each project creates its own venv folder:
   - projectA\venv\ (Windows)
2) When you activate that venv, `python` and `pip` point to the venv.
3) The `requests` package version can be DIFFERENT across projects.

Run (Windows):
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python app.py

Deactivate:
    deactivate
"""

import sys

# requests will be installed inside THIS project's venv after:
#   pip install -r requirements.txt
import requests


def main() -> None:
    # Print a clear banner so learners know which project is running.
    print("=== Project A ===")

    # sys.executable shows which Python interpreter is being used.
    # When the venv is active, this should point inside:
    #   ...\projectA\venv\Scripts\python.exe
    print("Python executable:", sys.executable)

    # Show the requests version. This is the key "aha" moment:
    # - Project A prints 2.25.1
    # - Project B prints 2.31.0
    print("requests version :", requests.__version__)

    # Keep the output educational:
    print("If you activate the other project's venv later, you should see a different requests version.")


if __name__ == "__main__":
    main()
