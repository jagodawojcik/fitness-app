### Fitness App main.py ####
## Author: Jagoda Wojcik ###
############################

#Imports

import sys
import os
from PySide2 import *

from pyqtGUI import *

#Main window class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

#Execute App

if __name__ == "__main__":
    print("hello")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

