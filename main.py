from PyQt5 import QtCore, QtGui, QtWidgets

import  os
import sys

from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from interfeis import Ui_MainWindow
import webbrowser


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.interfeis = Ui_MainWindow()
        self.interfeis.setupUi(self)
        self.init_UI()

    from AI import ai
    # Функция вызова диалоговова окна с выбором папки
    def GetDirectory(self):
        dirlist = QFileDialog.getExistingDirectory(self,"Выбрать папку",".")
        with open("G:/SortPhoto1.1/code/data/getDirectory.txt", "w") as file:
            file.write(dirlist)
    #Функция вызова диалоговова окна с выбором директории
    def GetFileNames(self):
        filenames, ok = QFileDialog.getOpenFileNames(self,"Выберите несколько файлов", ".","All Files(*.*)")
        with open("G:/SortPhoto1.1/code/data/getFileNames.txt", "w") as file:
            file.write(str(filenames)[1:-1])
    def Help(self):
        webbrowser.open('https://enter_your_site', new=2)


    def init_UI(self):
        self.setWindowTitle('PhotoAIsort')
        self.setWindowIcon(QIcon('artificial-intelligence-in-marketing.png'))
        self.interfeis.ImportPhoto.clicked.connect(self.GetFileNames) # вызов функции по нажатию на кнопку ImportPhoto
        self.interfeis.AI.clicked.connect(self.ai) # вызов функции по нажатию на кнопку AI
        self.interfeis.YourFolder.clicked.connect(self.GetDirectory) # вызов функции по нажатию на кнопку YourFolder
        self.interfeis.Help.clicked.connect(self.Help)
        #self.interfeis.RU.clicked.connect()
        #self.interfeis.US.clicked.connect()

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
