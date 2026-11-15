@echo off
cd /d "%~dp0"
echo ============================================================
echo   Push GoodNotes Pro to GitHub ^& Build GoodNotesPro.ipa
echo ============================================================
echo.
set /p REPO_URL="Paste your GitHub repo URL (e.g. https://github.com/YOURNAME/goodnotes-pro.git): "
if "%REPO_URL%"=="" (
    echo No URL entered. Exiting.
    pause
    exit /b 1
)
git branch -M main
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git push -u origin main
echo.
echo Done! Open your GitHub repository ^> Actions tab to download GoodNotesPro.ipa!
pause
