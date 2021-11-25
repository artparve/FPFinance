
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
columns= ['tr', 'pr', 'fl', 'amount', 'day', 'month', 'year']
try:
    file = pd.read_csv('my_by.csv')
except IOError as e:
    print(u'не удалось найти файл, так что создадим его')
    file = pd.DataFrame(columns= columns)
else:
	print('файл уже существует')
print(file)


def on_click():
	text = form.lineEdit.text()

	print(text)
	new_data = [0]*7
	for i in range(3):
		new_data[i] = int(form.listWidget.item(i).isSelected())
		print(form.listWidget.item(i).isSelected())
		
	if text.isnumeric():
		new_data[3] = int(text)
	else:
		print('Не число')
	
	print(form.calendarWidget.selectedDate())
	print(new_data)
	print("You clicked ok")

form.pushButton.clicked.connect(on_click)




app.exec()