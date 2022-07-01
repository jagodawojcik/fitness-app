### Fitness App main.py ####
## Author: Jagoda Wojcik ###
############################

#Imports

import sys
import os
from PySide2 import *
from cv2 import moveWindow
from qt_material import *
from PyQt5 import QtGui, QtCore


#Import the UI developed in QT Designer
from pyGUI import *

#Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Load Style Sheet - overrides fonts selected in qt designer
        #apply_stylesheet(app, theme='-----.xml')

        #Remove window title bar
        self.setWindowFlags(Qt.FramelessWindowHint)

        #Set main background to transparent
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))

        #Apply shadow effect to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #Set Window Icon and Title (hidden)
        self.setWindowIcon(QIcon(r"C:\Users\JagodaW\repos\FitApp\fitness-app\imgs\icons\Icon-22.png"))
        self.setWindowTitle("myFITness App")

        #Add resize grip functionality to the 'resize_grip' region on UI
        QSizeGrip(self.ui.resize_grip)
        
        ####Top right corner buttons functionality
        #Minimise window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        #Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())

        #Maximize window
        self.ui.maximize_window_button.clicked.connect(lambda: self.maximizeWindow())

        ####Stacked Widget Pages Navigation
        #Move to 'Me' personal info page
        self.ui.me_menu_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.me_body_page))

        #Move to 'Activity' page
        self.ui.activity_menu_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activity_body_page))

        #Move to 'Me' personal info page
        self.ui.food_menu_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.food_body_page))
        
        self.oldPos = self.pos()
        self.show()
    

    def maximizeWindow(self):
            if self.isMaximized():
                self.showNormal()
                #Change icon to ->go to normal view one page !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                self.ui.maximize_window_button.setIcon(QIcon(r"C:\Users\JagodaW\repos\FitApp\fitness-app\imgs\icons\Icon-1.png"))
            else:
                self.showMaximized()
                #Change icon to ->go to maximized two windows !!!!!!!!!!!!!!!!!!!!!!!
                self.ui.maximize_window_button.setIcon(QIcon(r"C:\Users\JagodaW\repos\FitApp\fitness-app\imgs\icons\Icon-52.png"))

    #read the position of the mouse on the screen when clicked
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    #calculate the distance between the last click point and the current mouse location
    def mouseMoveEvent(self, event):
       delta = QPoint (event.globalPos() - self.oldPos)
       self.move(self.x() + delta.x(), self.y() + delta.y())
       self.oldPos = event.globalPos()


#Execute App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

