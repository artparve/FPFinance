
#from interf_2 import *
#import sys

#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()

# ui.label.setText('sdfghjk')

# sys.exit(app.exec_())

from PyQt5 import uic
from main import *
import pandas as pd
from PyQt5.QtWidgets import QApplication

#Общие кнопки
#-------------------------------------------переход к окну добавления дохода)
def on_click_income():
	window.hide()
	Window_all.hide()
	window_inc.show()
	
	print("You clicked Add income")

#-------------------------------------------переход к окну просмотра календаря
def on_click_show():
	window.hide()
	window_inc.hide()
	window_all.show()
	
	print("You clicked Show All")

#-------------------------------------------переход в окно добавления покупок
def on_click_purchase():
	window_all.hide()

	window.show()
	
	print("You clicked Add Purchase")

#-------------------------------------------переход в окно настроек
def on_click_tool():
	
	window_all.hide()
	window.hide()
	window_tool.hide()
	window_tool.show()
	 
	print("You clicked tool")
#--------------------------------------------------------------

#Кнопки окна добавления покупок
#-----------------------------------------------нажатие на кнопку  "Add_Purchase" (добавление покупок)
def on_click_enter_purchase():
	text = form.lineEdit.text()
	date = form.calendarWidget.selectedDate()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

	#создаем базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт Продукты Комуналка Другое', 'Карта 1', '', 'base', 0, 0, 0]], columns=columns)
	else:
		print('файл уже существует')

	print(file['type'][0])
	#заполняем базу данных
	new_data = [0]*6

	tags = [i for i in (file['amount'][0]).split()]
	for i in range(len(tags)-1):
		if form.item_list.item(i).isSelected() == True:
			new_data[0] = tags[i]
	if new_data[0] == 0:
		new_data[0] = 'Other'
		
	new_data[2] = date.toString('yyyy MM dd')
	new_data[3] = date.day()
	new_data[4] = date.month()
	new_data[5] = date.year()
	
	#добавление если введено число
	if text.isnumeric():
		new_data[1] = int(text)
		file = file.append(pd.DataFrame([new_data], columns=columns))
		file.to_csv('my_by.csv', index=False)
	else:
		print('Не число')
	
	print(f'file:\n{file}')
	print("You clicked ok")
#---------------------------------------------------------	

#Кнопки окна добавления дохода
#-----------------------------------------------нажатие на кнопку  "Add_income" (добавление дохода)
def on_click_enter_income():
	text = form.lineEdit.text()
	date = form.calendarWidget.selectedDate()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

	#создаем базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт Продукты Комуналка Другое', 'Карта 1', '', 'base', 0, 0, 0]], columns=columns)
	else:
		print('файл уже существует')

	print(file['type'][0])
	#заполняем базу данных
	new_data = [0]*6

	tags = [i for i in (file['amount'][0]).split()]
	for i in range(len(tags)-1):
		if form.listWidget.item(i).isSelected() == True:
			new_data[0] = tags[i]
	if new_data[0] == 0:
		new_data[0] = 'Other'
		
	new_data[2] = date.toString('yyyy MM dd')
	new_data[3] = date.day()
	new_data[4] = date.month()
	new_data[5] = date.year()
	
	#добавление если введено число
	if text.isnumeric():
		new_data[1] = int(text)
		file = file.append(pd.DataFrame([new_data], columns=columns))
		file.to_csv('my_by.csv', index=False)
	else:
		print('Не число')
	
	print(f'file:\n{file}')
	print("You clicked ok")
#---------------------------------------------------------

#Кнопки окна календаря
#--------------------------------------нажатие на календарь во втором окне (работает)
def on_click_calendar():
	
	form_all.textEdit.clear()
	
	#заглядываем в базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    form_all.textEdit.append('Информации пока нет(')
	else:
		data = file[file['date'] == form_all.calendarWidget.selectedDate().toString('yyyy MM dd')]
		if len(data) == 0:
			form_all.textEdit.append('Информации пока нет(')
		else:
			form_all.textEdit.append(f'{form_all.calendarWidget.selectedDate().toString("dd MMM yyyy")} Вы добавили:')
			for t in data['type'].unique():
				form_all.textEdit.append(f'{t}:')
				for d in list(data[data['type']== t]['amount']):
					form_all.textEdit.append(f'{d} руб.')
	 
	print("You clicked Calendar")
#---------------------------------------------------------
#Кнопки окна настроек

#---------------------------------------------------------






