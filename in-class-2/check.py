"""Checks your output against the expected output.  Run:  python3 check.py

GitHub runs this every time you push (the green check / red X next to your commit).
"""
import subprocess, sys, pathlib, difflib

here = pathlib.Path(__file__).parent
all_ok = True
for exp in sorted((here / "expected").glob("*.txt")):
    script = here / (exp.stem + ".py")
    try:
        run = subprocess.run([sys.executable, script.name], cwd=here, capture_output=True, text=True, timeout=10)
    except subprocess.TimeoutExpired:
        print(f"✗ {script.name}: took too long (an infinite loop?)"); all_ok = False; continue
    got = run.stdout.rstrip().splitlines()
    want = exp.read_text().rstrip().splitlines()
    if run.returncode != 0:
        print(f"✗ {script.name} crashed:\n{run.stderr.strip()}\n"); all_ok = False
    elif [l.rstrip() for l in got] == [l.rstrip() for l in want]:
        print(f"✓ {script.name} matches")
    else:
        all_ok = False
        print(f"✗ {script.name} doesn't match yet. Lines with - are expected, + are yours:")
        for line in difflib.unified_diff(want, got, "expected", "yours", lineterm="", n=0):
            if not line.startswith(("---", "+++", "@@")):
                print("   " + line)
        print()
sys.exit(0 if all_ok else 1)
