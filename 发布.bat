@echo off
chcp 65001 >nul
setlocal
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo 请先运行 启动.bat 安装依赖。
  pause
  exit /b 1
)
.venv\Scripts\python.exe scripts\verify-docs.py
if errorlevel 1 goto fail
.venv\Scripts\python.exe -m mkdocs build --strict
if errorlevel 1 goto fail
git add -- .
git diff --cached --quiet
if errorlevel 1 git commit -m "Update Chinese CMI Wiki"
git push -u origin main
if errorlevel 1 goto fail
echo 已推送。GitHub Actions 完成后，访问 https://zhajiahui.github.io/cmi-wiki-cn/
pause
exit /b 0
:fail
echo 发布尚未完成，请查看上方输出。GitHub 首次使用需要完成登录。
pause
exit /b 1
