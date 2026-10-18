"""Run each independent project's content checks."""
from pathlib import Path
import subprocess
import sys
ROOT=Path(__file__).resolve().parent.parent
for project in ('CMI','Residence','Typewriter'):
    result=subprocess.run([sys.executable,str(ROOT/project/'scripts/verify-docs.py')],cwd=ROOT)
    if result.returncode:raise SystemExit(result.returncode)

result=subprocess.run([sys.executable,str(ROOT/'Phoenix/scripts/verify-docs.py')],cwd=ROOT)
if result.returncode:raise SystemExit(result.returncode)
