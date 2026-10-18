@echo off
chcp 65001 >nul
setlocal
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
cd /d "%~dp0"
set "WIKI_PYTHON=.venv\Scripts\python.exe"
if not exist "%WIKI_PYTHON%" if exist "CMI\.venv\Scripts\python.exe" set "WIKI_PYTHON=CMI\.venv\Scripts\python.exe"
if not exist "%WIKI_PYTHON%" (
  py -3.12 -m venv .venv
  if errorlevel 1 goto fail
)
"%WIKI_PYTHON%" -c "import mkdocs, material, jieba, bs4, markdownify, requests" >nul 2>&1
if errorlevel 1 (
  "%WIKI_PYTHON%" -m pip install -r Site\requirements-tools.txt
  if errorlevel 1 goto fail
)
"%WIKI_PYTHON%" Site\serve.py %*
if errorlevel 1 goto fail
exit /b 0
:fail
echo 启动未完成，请查看上方输出。首次运行需要 Python 3.12。
pause
exit /b 1
