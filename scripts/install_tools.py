import os
import subprocess
import sys

TOOLS = ["python", "git"]

def main():
    missing = [t for t in TOOLS if subprocess.call(["sh", "-lc", f"command -v {t} >/dev/null 2>&1"]) != 0]
    if missing:
        print("Missing tools:", ", ".join(missing))
        return 1
    print("Required tools available")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
