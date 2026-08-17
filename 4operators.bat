
@echo off



rem Simple Calculator Menu
setlocal EnableDelayedExpansion
:cal
echo =======================
echo    CALCULATOR
echo =======================
echo.
echo 1. Addition
echo 2. Subtraction
echo 3. Multiplication
echo 4. Division
echo 5. Exit
echo.
set /p choi=Enter choice:
echo.
if "%choi%"=="1" (
	set /p fn=Enter first number:
	set /p sn=Enter Second number:
	set /a addi=fn+sn
	echo Result: !addi!
	pause
	goto cal
) else if "%choi%"=="2" (
	set /p fn=Enter first number:
	set /p sn=Enter Second number:
	set /a subs=fn-sn
	echo Result: !subs!
	pause
	goto cal
) else if "%choi%"=="3" (
	set /p fn=Enter first number:
	set /p sn=Enter Second number:
	set /a mult=fn*sn
	echo Result: !mult!
	pause
	goto cal
) else if "%choi%"=="4" (
	set /p fn=Enter first number:
	set /p sn=Enter Second number:
	set /a divi=fn/sn
	echo Result: !divi!
	pause
	goto cal
) else if "%choi%"=="5" (
	echo The program is closing..
	pause	
	exit
) else (
	echo Invalid choice!, try again
	pause
	goto cal
)

