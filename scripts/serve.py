"""Start MkDocs and open the browser after the preview responds."""
from pathlib import Path
import subprocess, sys, threading, time, urllib.request, webbrowser

BASE = Path(__file__).resolve().parents[1]
URL = 'http://127.0.0.1:8000/cmi-wiki-cn/'

def open_when_ready():
    for _ in range(100):
        try:
            with urllib.request.urlopen(URL, timeout=1) as response:
                if response.status == 200:
                    webbrowser.open(URL)
                    return
        except OSError:
            time.sleep(0.2)

if __name__ == '__main__':
    if '--no-browser' not in sys.argv:
        threading.Thread(target=open_when_ready, daemon=True).start()
    try:
        raise SystemExit(subprocess.call([sys.executable, '-m', 'mkdocs', 'serve'], cwd=BASE))
    except KeyboardInterrupt:
        raise SystemExit(0)
