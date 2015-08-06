SET PATH=%PATH%;C:\Python27-x86\Lib\site-packages\PySide
pyside-uic -o mochil_gui.py player.ui
pyside-rcc -o resources_rc.py resources.qrc