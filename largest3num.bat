@echo off
color 0a
title Largest-of-three-numbers

:lar
set /p f1=Enter number 1:
set /p s2=Enter number 2:
set /p t3=Enter number 3:
echo.

set /a largest=f1

if %s2% GTR %largest% (
	set /a largest=s2
) 
if %t3% GTR %largest% (
	set /a largest=t3
) 
echo largest number is %largest%
	pause
	goto lar

