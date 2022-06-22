# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uizbiFSk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1049, 607)
        MainWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(220, 199, 225);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.header_left_frame = QFrame(self.header_frame)
        self.header_left_frame.setObjectName(u"header_left_frame")
        self.header_left_frame.setFrameShape(QFrame.StyledPanel)
        self.header_left_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.header_left_frame)
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.header_left_frame)
        self.menu_button.setObjectName(u"menu_button")
        font = QFont()
        font.setFamily(u"Nirmala UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.menu_button.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/Icon-20.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.menu_button)


        self.horizontalLayout.addWidget(self.header_left_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.NoFrame)
        self.header_center_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/Icon-22.png"))
        self.label_2.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignRight)

        self.label = QLabel(self.header_center_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Nirmala UI")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignLeft)

        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setStyleSheet(u"background-color: rgb(220, 199, 225);")
        self.header_right_frame.setFrameShape(QFrame.NoFrame)
        self.header_right_frame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.header_right_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.maximize_window_button = QPushButton(self.header_right_frame)
        self.maximize_window_button.setObjectName(u"maximize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icon-52.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_window_button.setIcon(icon1)

        self.gridLayout.addWidget(self.maximize_window_button, 0, 1, 1, 1)

        self.close_window_button = QPushButton(self.header_right_frame)
        self.close_window_button.setObjectName(u"close_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon2)

        self.gridLayout.addWidget(self.close_window_button, 0, 2, 1, 1)

        self.minimize_window_button = QPushButton(self.header_right_frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon3)

        self.gridLayout.addWidget(self.minimize_window_button, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.mainbod_frame = QFrame(self.centralwidget)
        self.mainbod_frame.setObjectName(u"mainbod_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainbod_frame.sizePolicy().hasHeightForWidth())
        self.mainbod_frame.setSizePolicy(sizePolicy)
        self.mainbod_frame.setStyleSheet(u"background-color: rgb(233, 229, 255);")
        self.mainbod_frame.setFrameShape(QFrame.NoFrame)
        self.mainbod_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mainbod_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.left_menu_container_frame = QFrame(self.mainbod_frame)
        self.left_menu_container_frame.setObjectName(u"left_menu_container_frame")
        self.left_menu_container_frame.setMinimumSize(QSize(65, 0))
        self.left_menu_container_frame.setMaximumSize(QSize(30, 16777215))
        self.left_menu_container_frame.setStyleSheet(u"background-color: rgb(220, 199, 225);")
        self.left_menu_container_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_container_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.left_menu_container_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_container_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(200, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.menu_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.menu_frame)
        self.pushButton.setObjectName(u"pushButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icon-62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(14)
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.menu_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icon-4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.menu_frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icon-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)


        self.horizontalLayout_8.addWidget(self.menu_frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_7.addWidget(self.left_menu_container_frame, 0, Qt.AlignLeft|Qt.AlignTop)

        self.mainbody_contents = QFrame(self.mainbod_frame)
        self.mainbody_contents.setObjectName(u"mainbody_contents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainbody_contents.sizePolicy().hasHeightForWidth())
        self.mainbody_contents.setSizePolicy(sizePolicy1)
        self.mainbody_contents.setFrameShape(QFrame.StyledPanel)
        self.mainbody_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainbody_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.mainbody_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.me_body_page = QWidget()
        self.me_body_page.setObjectName(u"me_body_page")
        self.stackedWidget.addWidget(self.me_body_page)
        self.activity_body_page = QWidget()
        self.activity_body_page.setObjectName(u"activity_body_page")
        self.stackedWidget.addWidget(self.activity_body_page)
        self.food_body_page = QWidget()
        self.food_body_page.setObjectName(u"food_body_page")
        self.stackedWidget.addWidget(self.food_body_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_7.addWidget(self.mainbody_contents)

        self.mainbod_right_frame = QFrame(self.mainbod_frame)
        self.mainbod_right_frame.setObjectName(u"mainbod_right_frame")
        self.mainbod_right_frame.setMinimumSize(QSize(200, 0))
        self.mainbod_right_frame.setMaximumSize(QSize(200, 16777215))
        self.mainbod_right_frame.setFrameShape(QFrame.StyledPanel)
        self.mainbod_right_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.mainbod_right_frame)


        self.verticalLayout.addWidget(self.mainbod_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(233, 229, 255);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame = QFrame(self.footer_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.footer_left_frame = QLabel(self.frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")

        self.horizontalLayout_4.addWidget(self.footer_left_frame, 0, Qt.AlignBottom)


        self.horizontalLayout_6.addWidget(self.frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.questionmark_button = QPushButton(self.footer_right_frame)
        self.questionmark_button.setObjectName(u"questionmark_button")

        self.horizontalLayout_5.addWidget(self.questionmark_button, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.footer_right_frame, 0, Qt.AlignBottom)

        self.resize_grip = QFrame(self.footer_frame)
        self.resize_grip.setObjectName(u"resize_grip")
        self.resize_grip.setMinimumSize(QSize(15, 15))
        self.resize_grip.setMaximumSize(QSize(15, 15))
        self.resize_grip.setFrameShape(QFrame.StyledPanel)
        self.resize_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.resize_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"myFITnessApp", None))
        self.maximize_window_button.setText("")
        self.close_window_button.setText("")
        self.minimize_window_button.setText("")
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Me", None))
        self.pushButton_2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.pushButton_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.footer_left_frame.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Author: Jagoda Wojcik", None))
        self.questionmark_button.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

