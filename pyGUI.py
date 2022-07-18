# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiWDgDPS.ui'
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
        MainWindow.resize(1083, 719)
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
        self.me_menu_btn = QPushButton(self.menu_frame)
        self.me_menu_btn.setObjectName(u"me_menu_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icon-62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.me_menu_btn.setIcon(icon4)
        self.me_menu_btn.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.me_menu_btn, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Nirmala UI")
        font2.setPointSize(14)
        self.label_3.setFont(font2)

        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)

        self.activity_menu_btn = QPushButton(self.menu_frame)
        self.activity_menu_btn.setObjectName(u"activity_menu_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icon-4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_menu_btn.setIcon(icon5)
        self.activity_menu_btn.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.activity_menu_btn, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.food_menu_btn = QPushButton(self.menu_frame)
        self.food_menu_btn.setObjectName(u"food_menu_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icon-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.food_menu_btn.setIcon(icon6)
        self.food_menu_btn.setIconSize(QSize(60, 60))

        self.gridLayout_2.addWidget(self.food_menu_btn, 2, 0, 1, 1, Qt.AlignLeft)

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
        self.verticalLayout_4 = QVBoxLayout(self.me_body_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.me_body_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.me_scroll_area = QWidget()
        self.me_scroll_area.setObjectName(u"me_scroll_area")
        self.me_scroll_area.setGeometry(QRect(0, 0, 753, 1236))
        self.verticalLayout_3 = QVBoxLayout(self.me_scroll_area)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.personal_info_main_frame = QFrame(self.me_scroll_area)
        self.personal_info_main_frame.setObjectName(u"personal_info_main_frame")
        self.personal_info_main_frame.setMinimumSize(QSize(0, 300))
        self.personal_info_main_frame.setFrameShape(QFrame.StyledPanel)
        self.personal_info_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.personal_info_main_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.personal_info_frame = QFrame(self.personal_info_main_frame)
        self.personal_info_frame.setObjectName(u"personal_info_frame")
        self.personal_info_frame.setMinimumSize(QSize(0, 700))
        self.personal_info_frame.setFrameShape(QFrame.StyledPanel)
        self.personal_info_frame.setFrameShadow(QFrame.Raised)
        self.tabWidget = QTabWidget(self.personal_info_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 683, 300))
        self.tabWidget.setMinimumSize(QSize(0, 250))
        self.personal_info_tab = QWidget()
        self.personal_info_tab.setObjectName(u"personal_info_tab")
        self.label_6 = QLabel(self.personal_info_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 10, 661, 16))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_6.setFont(font3)
        self.widget = QWidget(self.personal_info_tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-10, 40, 683, 191))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.age_label = QLabel(self.widget)
        self.age_label.setObjectName(u"age_label")
        font4 = QFont()
        font4.setPointSize(10)
        self.age_label.setFont(font4)

        self.gridLayout_3.addWidget(self.age_label, 1, 0, 1, 1)

        self.name_line = QLineEdit(self.widget)
        self.name_line.setObjectName(u"name_line")
        self.name_line.setAutoFillBackground(False)
        self.name_line.setStyleSheet(u"background-color: rgb(255, 255, 245)")
        self.name_line.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.name_line, 0, 3, 1, 1)

        self.frame_5 = QFrame(self.widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        font5 = QFont()
        font5.setPointSize(9)
        self.pushButton.setFont(font5)

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.gridLayout_3.addWidget(self.frame_5, 8, 3, 2, 1)

        self.name_line_2 = QLabel(self.widget)
        self.name_line_2.setObjectName(u"name_line_2")
        self.name_line_2.setFont(font4)

        self.gridLayout_3.addWidget(self.name_line_2, 0, 0, 1, 1)

        self.weight_label = QLabel(self.widget)
        self.weight_label.setObjectName(u"weight_label")
        self.weight_label.setFont(font4)

        self.gridLayout_3.addWidget(self.weight_label, 6, 0, 1, 1)

        self.age_linetext = QLineEdit(self.widget)
        self.age_linetext.setObjectName(u"age_linetext")
        self.age_linetext.setStyleSheet(u"background-color: rgb(255, 255, 245)")

        self.gridLayout_3.addWidget(self.age_linetext, 1, 3, 1, 1)

        self.height_line = QLineEdit(self.widget)
        self.height_line.setObjectName(u"height_line")
        self.height_line.setStyleSheet(u"background-color: rgb(255, 255, 245)")

        self.gridLayout_3.addWidget(self.height_line, 3, 3, 1, 1)

        self.sex_label = QLabel(self.widget)
        self.sex_label.setObjectName(u"sex_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sex_label.sizePolicy().hasHeightForWidth())
        self.sex_label.setSizePolicy(sizePolicy2)
        self.sex_label.setMaximumSize(QSize(16777215, 13))
        self.sex_label.setFont(font4)

        self.gridLayout_3.addWidget(self.sex_label, 2, 0, 1, 1)

        self.height_label = QLabel(self.widget)
        self.height_label.setObjectName(u"height_label")
        self.height_label.setFont(font4)

        self.gridLayout_3.addWidget(self.height_label, 3, 0, 1, 1)

        self.weight_line = QLineEdit(self.widget)
        self.weight_line.setObjectName(u"weight_line")
        self.weight_line.setStyleSheet(u"background-color: rgb(255, 255, 245)")

        self.gridLayout_3.addWidget(self.weight_line, 6, 3, 1, 1)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(0, 20))
        self.frame_4.setMaximumSize(QSize(1677721, 15))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.radioButton = QRadioButton(self.frame_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 0, 74, 16))
        self.radioButton_2 = QRadioButton(self.frame_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(100, 0, 74, 16))

        self.gridLayout_3.addWidget(self.frame_4, 2, 3, 1, 1)

        self.frame_4.raise_()
        self.name_line_2.raise_()
        self.age_label.raise_()
        self.name_line.raise_()
        self.age_linetext.raise_()
        self.sex_label.raise_()
        self.weight_label.raise_()
        self.height_label.raise_()
        self.height_line.raise_()
        self.weight_line.raise_()
        self.frame_5.raise_()
        self.frame_7 = QFrame(self.personal_info_tab)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 250, 120, 80))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.tabWidget.addTab(self.personal_info_tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.personal_info_frame)


        self.verticalLayout_3.addWidget(self.personal_info_main_frame)

        self.weight_record_main_frame = QFrame(self.me_scroll_area)
        self.weight_record_main_frame.setObjectName(u"weight_record_main_frame")
        self.weight_record_main_frame.setMinimumSize(QSize(20, 400))
        self.weight_record_main_frame.setFrameShape(QFrame.StyledPanel)
        self.weight_record_main_frame.setFrameShadow(QFrame.Raised)
        self.calendarWidget = QCalendarWidget(self.weight_record_main_frame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(40, 70, 392, 236))
        palette = QPalette()
        brush = QBrush(QColor(233, 229, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.calendarWidget.setPalette(palette)
        font6 = QFont()
        font6.setBold(True)
        font6.setWeight(75)
        self.calendarWidget.setFont(font6)
        self.calendarWidget.setFocusPolicy(Qt.WheelFocus)
        self.add_weight_label = QLabel(self.weight_record_main_frame)
        self.add_weight_label.setObjectName(u"add_weight_label")
        self.add_weight_label.setGeometry(QRect(10, 20, 251, 31))
        font7 = QFont()
        font7.setPointSize(14)
        self.add_weight_label.setFont(font7)
        self.date_label = QLabel(self.weight_record_main_frame)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setGeometry(QRect(470, 20, 55, 16))
        self.date_label.setFont(font3)
        self.weight_label_2 = QLabel(self.weight_record_main_frame)
        self.weight_label_2.setObjectName(u"weight_label_2")
        self.weight_label_2.setGeometry(QRect(470, 90, 81, 31))
        self.weight_label_2.setFont(font3)
        self.display_date_label = QLabel(self.weight_record_main_frame)
        self.display_date_label.setObjectName(u"display_date_label")
        self.display_date_label.setGeometry(QRect(470, 50, 55, 16))
        self.add_weight_textEdit = QLineEdit(self.weight_record_main_frame)
        self.add_weight_textEdit.setObjectName(u"add_weight_textEdit")
        self.add_weight_textEdit.setGeometry(QRect(470, 120, 171, 22))
        self.add_weight_textEdit.setStyleSheet(u"background-color: rgb(255, 255, 245)")
        self.weight_table_view = QTableView(self.weight_record_main_frame)
        self.weight_table_view.setObjectName(u"weight_table_view")
        self.weight_table_view.setGeometry(QRect(440, 170, 256, 192))
        self.add_weight_btn = QPushButton(self.weight_record_main_frame)
        self.add_weight_btn.setObjectName(u"add_weight_btn")
        self.add_weight_btn.setGeometry(QRect(70, 340, 93, 28))
        self.remove_weight_btn = QPushButton(self.weight_record_main_frame)
        self.remove_weight_btn.setObjectName(u"remove_weight_btn")
        self.remove_weight_btn.setGeometry(QRect(250, 340, 93, 28))

        self.verticalLayout_3.addWidget(self.weight_record_main_frame)

        self.weight_chart_main_frame = QFrame(self.me_scroll_area)
        self.weight_chart_main_frame.setObjectName(u"weight_chart_main_frame")
        self.weight_chart_main_frame.setMinimumSize(QSize(0, 500))
        self.weight_chart_main_frame.setFrameShape(QFrame.StyledPanel)
        self.weight_chart_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.weight_chart_main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.weight_chart_label = QLabel(self.weight_chart_main_frame)
        self.weight_chart_label.setObjectName(u"weight_chart_label")
        self.weight_chart_label.setFont(font7)

        self.verticalLayout_6.addWidget(self.weight_chart_label, 0, Qt.AlignTop)

        self.weight_plot_space = QFrame(self.weight_chart_main_frame)
        self.weight_plot_space.setObjectName(u"weight_plot_space")
        self.weight_plot_space.setFrameShape(QFrame.StyledPanel)
        self.weight_plot_space.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.weight_plot_space)


        self.verticalLayout_3.addWidget(self.weight_chart_main_frame)

        self.scrollArea.setWidget(self.me_scroll_area)

        self.verticalLayout_4.addWidget(self.scrollArea)

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
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_6.addWidget(self.resize_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


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
        self.me_menu_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Me", None))
        self.activity_menu_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.food_menu_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Food", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Personal Information", None))
        self.age_label.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.name_line.setText(QCoreApplication.translate("MainWindow", u"enter name...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.name_line_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.weight_label.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.age_linetext.setText(QCoreApplication.translate("MainWindow", u"enter age...", None))
        self.height_line.setText(QCoreApplication.translate("MainWindow", u"enter height (cm)...", None))
        self.sex_label.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.height_label.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.weight_line.setText(QCoreApplication.translate("MainWindow", u"enter weight (kg)...", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Female", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Male", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.personal_info_tab), QCoreApplication.translate("MainWindow", u"Personal Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Add New User - coming soon...", None))
        self.add_weight_label.setText(QCoreApplication.translate("MainWindow", u"Add weight record", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.weight_label_2.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.display_date_label.setText("")
        self.add_weight_textEdit.setText(QCoreApplication.translate("MainWindow", u"enter weight (kg): ...", None))
        self.add_weight_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_weight_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.weight_chart_label.setText(QCoreApplication.translate("MainWindow", u"Weight chart", None))
        self.footer_left_frame.setText(QCoreApplication.translate("MainWindow", u"Version 1.0 | Author: Jagoda Wojcik", None))
        self.questionmark_button.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

