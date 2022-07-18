import numpy as np
import sys
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg  import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget

class Canvas(FigureCanvas):
    def __init__(self, parent, width=5, height=4, dpi=100):
        fig, self.axes = plt.subplots(figsize=(width,height), dpi=dpi)
        super(Canvas, self).__init__(fig)
        self.setParent(parent)



#Demo of the created widget###

class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1600,800)

        ###Matplotlib FigureCanvas object create and
        # code on what I want to be plotted###
        chart = Canvas(self,width=10, height=5, dpi=100)
        chart.axes.plot([0, 1, 2, 3, 4], [10,1,20,3,4])
        #layout.addWidget(chart) #add this widget to the layout of the area of interest in mainwindow
        
        self.show()


app = QApplication(sys.argv)
demo = AppDemo()
demo.show()
sys.exit(app.exec_())