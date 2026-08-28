@echo off 
title JARVIS
color 0b

:login 
cls
echo ======================
echo    Welcome   %username%
echo =====================
echo.
set /p pass= Enter your password:

if "%pass%"=="@li786" (
	echo Access granted
	pause
	goto success
) else ( 
 	echo Access denied. Try again
	pause
	goto login
)
:success
cls
echo ======================
echo Access granted. Initializing JARVIS...
echo ======================

start  py main.py

exit