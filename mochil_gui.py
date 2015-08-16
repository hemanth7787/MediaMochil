# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created: Sun Aug 09 00:57:11 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(558, 297)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mochil_final.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 541, 181))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scrollArea = QtGui.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 541, 181))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 539, 179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.musicTable = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.musicTable.setGeometry(QtCore.QRect(0, 0, 541, 181))
        self.musicTable.setColumnCount(4)
        self.musicTable.setObjectName("musicTable")
        self.musicTable.setColumnCount(4)
        self.musicTable.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 200, 441, 19))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.play = QtGui.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(90, 230, 31, 31))
        self.play.setObjectName("play")
        self.pause = QtGui.QPushButton(self.centralwidget)
        self.pause.setGeometry(QtCore.QRect(130, 230, 31, 31))
        self.pause.setObjectName("pause")
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(170, 230, 31, 31))
        self.stop.setObjectName("stop")
        self.volume = QtGui.QDial(self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(500, 220, 41, 51))
        self.volume.setObjectName("volume")
        self.open = QtGui.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(210, 230, 31, 31))
        self.open.setObjectName("open")
        self.previous = QtGui.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(10, 230, 31, 31))
        self.previous.setObjectName("previous")
        self.next_item = QtGui.QPushButton(self.centralwidget)
        self.next_item.setGeometry(QtCore.QRect(50, 230, 31, 31))
        self.next_item.setObjectName("next_item")
        self.play_timer = QtGui.QLineEdit(self.centralwidget)
        self.play_timer.setEnabled(True)
        self.play_timer.setGeometry(QtCore.QRect(460, 200, 91, 22))
        self.play_timer.setReadOnly(True)
        self.play_timer.setObjectName("play_timer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setStatusTip("")
        self.statusbar.setAccessibleDescription("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 558, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionRecent = QtGui.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.actionRecent)
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MediaMochil", None, QtGui.QApplication.UnicodeUTF8))
        self.play.setToolTip(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.play.setText(QtGui.QApplication.translate("MainWindow", "|>", None, QtGui.QApplication.UnicodeUTF8))
        self.pause.setToolTip(QtGui.QApplication.translate("MainWindow", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.pause.setText(QtGui.QApplication.translate("MainWindow", "||", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setToolTip(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("MainWindow", "[]", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setToolTip(QtGui.QApplication.translate("MainWindow", "Add files", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.previous.setToolTip(QtGui.QApplication.translate("MainWindow", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.previous.setText(QtGui.QApplication.translate("MainWindow", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.next_item.setToolTip(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.next_item.setText(QtGui.QApplication.translate("MainWindow", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.play_timer.setText(QtGui.QApplication.translate("MainWindow", "00:00 / 00:00", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent.setText(QtGui.QApplication.translate("MainWindow", "Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
