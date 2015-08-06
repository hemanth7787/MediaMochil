# MediaMochil
A media player in Python using Pyglet and Pyside

Alpha version

This is particularly for windows version. It may run on some linux version , but with modification mainly to the "avbin" loading part.

![picture alt](http://i.imgur.com/yiEEcTY.png "Screenshot")

## Building windows binary

Install python 32-bit.

set the path to `<python dir>\scripts`

Install pip , run `python get-pip.py`  from `<python-dir>`

Install PySide , Pyglet, mutagen , pyinstaller using pip

check weather commands `pyside-uic` , `pyinstaller` etc works from console

run `make.bat` and open the dist directory for the binary

## Extra setup

Use Pycharm IDE for editing python files, Qt designer for editing `.ui` files and qt linguist for translation.

`mochil_gui.py` is auto generated from `player.ui` file using pyside-uic, run the `compile_ui.bat` to pick up any 
update to the `.ui` file.
