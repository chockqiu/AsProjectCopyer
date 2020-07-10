@echo off
where pyinstaller>nul
if %errorlevel%==0 (
	pyinstaller --distpath .\build --log-level WARN -Fy aspjcp.py
	echo Build Finish.
) else (
	echo 请安装pyinstaller
	echo 例如执行命令: pip install pyinstaller
)
pause