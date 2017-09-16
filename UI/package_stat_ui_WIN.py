# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/package_stat_ui_WIN.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(423, 251)
        MainWindow.setMinimumSize(QtCore.QSize(423, 251))
        MainWindow.setMaximumSize(QtCore.QSize(423, 251))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(81, 81, 81);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(391, 46))
        self.frame_2.setMaximumSize(QtCore.QSize(391, 46))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.btn_start = QtWidgets.QPushButton(self.frame_2)
        self.btn_start.setMinimumSize(QtCore.QSize(75, 23))
        self.btn_start.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_start.setStyleSheet("QPushButton { /* all types of tool button */\n"
"    color: rgb(80, 80, 80);\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_start.setObjectName("btn_start")
        self.gridLayout_4.addWidget(self.btn_start, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setMinimumSize(QtCore.QSize(391, 65))
        self.groupBox.setMaximumSize(QtCore.QSize(391, 65))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.frame_11 = QtWidgets.QFrame(self.groupBox)
        self.frame_11.setGeometry(QtCore.QRect(1, 8, 390, 57))
        self.frame_11.setMinimumSize(QtCore.QSize(390, 57))
        self.frame_11.setMaximumSize(QtCore.QSize(390, 57))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_21.setContentsMargins(13, -1, 13, -1)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.fld_package_dir = QtWidgets.QLineEdit(self.frame_11)
        self.fld_package_dir.setMinimumSize(QtCore.QSize(324, 31))
        self.fld_package_dir.setMaximumSize(QtCore.QSize(324, 31))
        self.fld_package_dir.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_package_dir.setText("")
        self.fld_package_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_package_dir.setObjectName("fld_package_dir")
        self.gridLayout_21.addWidget(self.fld_package_dir, 0, 0, 1, 1)
        self.btn_package_dir = QtWidgets.QToolButton(self.frame_11)
        self.btn_package_dir.setMinimumSize(QtCore.QSize(40, 31))
        self.btn_package_dir.setMaximumSize(QtCore.QSize(40, 31))
        self.btn_package_dir.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_package_dir.setObjectName("btn_package_dir")
        self.gridLayout_21.addWidget(self.btn_package_dir, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setMinimumSize(QtCore.QSize(391, 70))
        self.groupBox_6.setMaximumSize(QtCore.QSize(391, 70))
        self.groupBox_6.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fld_tag = QtWidgets.QLineEdit(self.groupBox_6)
        self.fld_tag.setMinimumSize(QtCore.QSize(365, 31))
        self.fld_tag.setMaximumSize(QtCore.QSize(365, 31))
        self.fld_tag.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_tag.setText("")
        self.fld_tag.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_tag.setObjectName("fld_tag")
        self.gridLayout_3.addWidget(self.fld_tag, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar{\n"
"background-color: rgb(81, 81, 81);\n"
"color: rgb(203, 203, 203);}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Package Statistic"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.groupBox.setTitle(_translate("MainWindow", "Package Path"))
        self.fld_package_dir.setPlaceholderText(_translate("MainWindow", "Select Package Directory"))
        self.btn_package_dir.setText(_translate("MainWindow", "..."))
        self.groupBox_6.setTitle(_translate("MainWindow", "Tags"))
        self.fld_tag.setPlaceholderText(_translate("MainWindow", "Enter Tag"))

