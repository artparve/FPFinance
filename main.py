
# from interf import *
# import sys

# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# ui = Ui_MainWindow()
# ui.setupUi(MainWindow)
# MainWindow.show()

# ui.label.setText('sdfghjk')

# sys.exit(app.exec_())

from PyQt5 import uic
import pandas as pd
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("interf.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
try:
    file = pd.read_csv('my_by.csv')
except IOError as e:
    print(u'не удалось найти файл, так что создадим его')
    file = pd.DataFrame({'tr' : [], 'pr' : [], 'fl' : [],
    	'amount' : [], 'day' : [], 'month' : [], 'year' : []})
print(file)

def on_click():
	print(form.lineEdit.text())
	print(form.listWidget.item(1).isSelected())
	print(form.calendarWidget.selectedDate())
	print("You clicked ok")

form.pushButton.clicked.connect(on_click)




app.exec()