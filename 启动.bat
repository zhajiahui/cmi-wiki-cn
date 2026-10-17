@echo off
chcp 65001 >nul
setlocal
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  py -3.12 -m venv .venv
  if errorlevel 1 (
    echo 请先安装 Python 3.12，然后重新运行。
    pause
    exit /b 1
  )
)
set "WIKI_PY=.venv\Scripts\python.exe"
"%WIKI_PY%" -c "import mkdocs, material, jieba" >nul 2>nul
if errorlevel 1 (
  "%WIKI_PY%" -m pip install -r requirements-tools.txt
  if errorlevel 1 (
    echo 依赖安装未完成，请查看上方输出。
    pause
    exit /b 1
  )
)
"%WIKI_PY%" scripts\serve.py %*
pause
