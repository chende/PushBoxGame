package command:
Mac:
pyinstaller --onefile --windowed --add-data "resources/*:resources/" --add-data "data/*:data/" --icon app_icon.icns --name 疯狂推箱子 main.py

Windows:
pyinstaller --onefile --windowed --add-data "resources/*;resources/" --add-data "data/*;data/" --icon app_icon.ico --name 疯狂推箱子 main.py
