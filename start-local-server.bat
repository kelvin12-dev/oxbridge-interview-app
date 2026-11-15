@echo off
title GoodNotes Pro - Local iPad Wi-Fi Server
cd /d "%~dp0web"
echo ============================================================
echo   GoodNotes Pro - Instant iPad Wi-Fi Server
echo ============================================================
echo.
echo Open Safari on your iPad (on the same Wi-Fi) and visit one
echo of your Windows PC IP addresses below on port 8090:
echo.
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4 Address"') do (
    for /f "tokens=* delims= " %%b in ("%%a") do echo   http://%%b:8090
)
echo.
echo Also works on this PC at: http://localhost:8090
echo Tip on iPad Safari: Tap Share ^> "Add to Home Screen" for full-screen app mode!
echo.
python -m http.server 8090 --bind 0.0.0.0
pause
