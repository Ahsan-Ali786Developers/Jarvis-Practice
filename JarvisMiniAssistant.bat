
@echo off
setlocal EnableDelayedExpansion
title Jarvis v2
:Jarvis
echo ===========================
echo JARVIS v2 is publishing
echo ===========================
echo.
echo 1. Say Hello
echo 2. Open notepad
echo 3. Open calculator
echo 4. Show Username
echo 5. Calculator
echo 6. Exit
set /p cho=Enter your choice:
echo.
if "%cho%"=="1" (
	echo Hello! Welcome to JARVIS.
	goto Jarvis
) else if "%cho%"=="2" (
	start notepad
	goto Jarvis
) else if "%cho%"=="3" (
	start calc
	goto Jarvis
) else if "%cho%"=="4" (
	echo Your Window username is: %username%
	goto Jarvis
) else if "%cho%"=="5" (
	goto Calculator

) else if "%cho%"=="6" (
	echo Jarvis is going to sleep.
	exit
) else (
	echo Invalid choice! Try again.
	goto Jarvis
)
:Calculator

echo zJarvis Calcluator
echo.
echo 1. Addition
echo 2. Subtraction
echo 3. Multiplication
echo 4. Division
echo 5. Back to Jarvis
set /p jar=Enter your choice:
echo.
if "%jar%"=="1" (
	set /p n1=Enter your first number:
	set /p n2=Enter your second number:
	set /a sum=n1+n2
	echo The sum of !n2! and !n1! is !sum!
	pause
	goto Calculator
) else if "%jar%"=="2" (
	set /p n1=Enter your first number:
	set /p n2=Enter your second number:
	set /a sub=n1-n2
	echo The subtraction of !n1! and !n2! is !sub!
	pause
	goto Calculator
) else if "%jar%"=="3" (
	set /p n1=Enter your first number:
	set /p n2=Enter your second number:
	set /a mul=n1*n2
	echo The Multiplication of !n1! and !n2! is !mul!
	pause
	goto Calculator
) else if "%jar%"=="4" (
	goto division
) else if "%jar%"=="5" (
	goto Jarvis
) else (
	echo Invalid choice! Try again.
	pause
	goto Calculator
)
:division
	set /p n1=Enter your first number:
	set /p n2=Enter your second number:
	if "!n2!"=="0" (
		echo You can not divide by zero
		echo enter a valid number.
		pause
		goto division
	) else (
		set /a div=n1/n2
		echo The divsion of !n1! and !n2! is !div!
		pause
		goto Calculator
)