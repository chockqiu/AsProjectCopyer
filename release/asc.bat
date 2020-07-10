@echo off
set p1=%1
if "%p1%"=="" (set /p p1="请输入需要复制的工程:")
aspjcp "%p1%" "D:\AS Project"
pause