@echo off
Title CatTools - Installer

if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)

curl https://sneaky.pink/cattools/cattools.exe -o C:\Windows\System32\cattools.exe

del %0