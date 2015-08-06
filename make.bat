pyside-uic.exe player.ui > mochil_gui.py
pyinstaller  -w -D mediamochil.py -i icon.ico
copy avbin.dll dist\mediamochil