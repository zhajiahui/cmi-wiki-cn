"""Preview both projects and open the browser once the server responds."""
from pathlib import Path
import argparse
import subprocess
import sys
import threading
import time
import urllib.request
import webbrowser
ROOT=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser()
parser.add_argument('--no-browser',action='store_true')
parser.add_argument('--port',type=int,default=8000)
args=parser.parse_args()
url=f'http://127.0.0.1:{args.port}/cmi-wiki-cn/'
def open_when_ready():
    for _ in range(100):
        try:
            with urllib.request.urlopen(url,timeout=1) as response:
                if response.status==200:webbrowser.open(url);return
        except OSError:time.sleep(0.2)
if __name__=='__main__':
    checked=subprocess.run([sys.executable,str(ROOT/'Site/verify.py')],cwd=ROOT)
    if checked.returncode:raise SystemExit(checked.returncode)
    if not args.no_browser:threading.Thread(target=open_when_ready,daemon=True).start()
    try:
        raise SystemExit(subprocess.call([sys.executable,'-m','mkdocs','serve','-f','Site/mkdocs.yml','--dev-addr',f'127.0.0.1:{args.port}'],cwd=ROOT))
    except KeyboardInterrupt:raise SystemExit(0)
