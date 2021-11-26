
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

Form_all, Window_all = uic.loadUiType("interf_show.ui")
window_all = Window_all()
form_all = Form_all()
form_all.setupUi(window_all)
window_all.hide()

#--------------------------------------------------------------------
def on_click_enter():
	text = form.lineEdit.text()
	date = form.calendarWidget.selectedDate()
	columns= ['other','tr', 'pr', 'fl', 'amount', 'day', 'month', 'year']
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame(columns= columns)
	else:
		print('файл уже существует')

	new_data = [0]*8
	for i in range(1,4):
		new_data[i] = int(form.listWidget.item(i).isSelected())
	if new_data[1:4] == [0,0,0]:
		new_data[0] = 1
	new_data[4] = int(form.calendarWidget.selectedDate().day())
	new_data[5] = int(form.calendarWidget.selectedDate().month())
	new_data[6] = int(form.calendarWidget.selectedDate().year())

	if text.isnumeric():
		new_data[3] = int(text)
		file = file.append(pd.DataFrame([new_data], columns=columns))
	else:
		print('Не число')
	
	print(f'new_data: {new_data}')
	print(f'file:\n{file}')
	file.to_csv('my_by.csv', index=False)
	print("You clicked ok")
#---------------------------------------------------------------------
def on_click_show():
	window.hide()
	window_all.show()
	
	
	print("You clicked Show All")


#-----------------------------------------------------------------------
def on_click_back():
	window_all.hide()
	window.show()
	
	
	print("You clicked Add Purchase")


#-----------------------------------------------------------------------

form.pushButton.clicked.connect(on_click_enter)
form.pushButton_2.clicked.connect(on_click_show)
form_all.pushButton_2.clicked.connect(on_click_back)


app.exec()

