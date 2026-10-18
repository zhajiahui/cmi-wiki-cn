@echo off
chcp 65001 >nul
setlocal
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
cd /d "%~dp0"
set "WIKI_PYTHON=.venv\Scripts\python.exe"
if not exist "%WIKI_PYTHON%" if exist "CMI\.venv\Scripts\python.exe" set "WIKI_PYTHON=CMI\.venv\Scripts\python.exe"
if not exist "%WIKI_PYTHON%" (
  echo 请先运行 启动.bat 安装依赖。
  pause
  exit /b 1
)
"%WIKI_PYTHON%" Site\verify.py
if errorlevel 1 goto fail
"%WIKI_PYTHON%" -m mkdocs build --strict -f Site\mkdocs.yml
if errorlevel 1 goto fail
"%WIKI_PYTHON%" Site\verify-site.py
if errorlevel 1 goto fail
git add -- .
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "Update Chinese plugin Wiki"
  if errorlevel 1 goto fail
)
git push -u origin main
if errorlevel 1 goto fail
echo 已推送。GitHub Actions 完成后，访问 https://zhajiahui.github.io/cmi-wiki-cn/
pause
exit /b 0
:fail
echo 发布尚未完成，请查看上方输出。
pause
exit /b 1
