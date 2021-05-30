from random import sample
import matplotlib.pyplot as plt
import matplotlib.colors as pltc
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("chart.ui",self)
        self.show()
    sales = [15,35,50]
    colors = sample(list(pltc.cnames.values()), len(sales))
    ['#FFA500','#A52A2A','#008000']
    salesnaeme = ['Daily', 'Monthly', ' Yearly ']
    space_slice = [0.07,0.3,0]
    plt.figure(figsize=(6,5))
    plt.pie(sales, labels= salesnaeme, autopct='%1.1f%%', shadow=False, explode=space_slice,colors=colors)
    plt.title("Sales Summary")
    plt.legend(salesnaeme, loc=(-0.25,0.7),shadow =False)
    plt.show()



app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()


