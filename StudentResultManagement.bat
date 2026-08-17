@echo off
title Mini Student Result system

echo ========================
echo Mini Student Result System
echo ========================
echo.
echo Result System
echo.
:record
set /p na=Enter your name : 
set /p eng=English Marks : 
set /p mat=Math Marks : 
set /p com=Computer Marks : 
echo.
echo Student Name: %na%
echo English: %eng%

echo Math: %mat%
echo Computer: %com%
set /a tot=eng+mat+com
echo Obtain : %tot% from Total : 300

set /a perc=(tot*100)/300
echo Percentage: %perc%

if "%perc%" GEQ "50" (
	echo Pass
	pause
	goto record
) else (
	echo Fail
	pause
	goto record
)