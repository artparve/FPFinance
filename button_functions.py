
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
import pandas as pd
from windows import *
from PyQt5.QtWidgets import QApplication

columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

#Общие кнопки
#-------------------------------------------переход к окну просмотра календаря
def on_click_show():
	window.hide()
	window_tool.hide()
	window_all.show()

	#заглядываем в базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    form_all.textEdit.append('Информации пока нет(')
	else:
		data = file[file['date'] == form_all.calendarWidget.selectedDate().toString('yyyy MM dd')]
		if len(data) == 0:
			form_all.textEdit.clear()
			form_all.textEdit.append('Информации пока нет(')
		else:
			form_all.textEdit.append(f'{form_all.calendarWidget.selectedDate().toString("dd MMM yyyy")} Вы добавили:')
			for t in data['type'].unique():
				form_all.textEdit.append(f'{t}:')
				for d in list(data[data['type']== t]['amount']):
					form_all.textEdit.append(f'{d} руб.')
	 
	
	print("You clicked Show All")

#-------------------------------------------переход в окно добавления
def on_click_purchase():
	window_all.hide()
	window_tool.hide()
	window.show()

	#обновление из базы
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], \
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		user = (file[file["date"] == "user"].values)[0]
		form.income_list.clear()
		form.income_list.addItems(user[2].split('|'))
		form.card_list.clear()
		form.card_list.addItems(user[1].split('|'))
		form.item_list.clear()
		form.item_list.addItems(user[0].split('|'))

	form.item_list.show()
	form.income_list.hide()
	form.label_3.clear()
	form.label_3.setText('Выберите тип покупки и карту')

	form.label_4.clear()
	form.label_4.setText('Выберите дату')
	form.label_2.clear()
	form.label_2.setText('Введите сумму')

	print("You clicked Add")

#-------------------------------------------переход в окно настроек
def on_click_tool():
	window_all.hide()
	window.hide()
	window_tool.show()

	#обновление из базы
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		user = (file[file["date"] == "user"].values)[0]

		form_tool.list_card.clear()
		form_tool.list_card.addItems(user[1].split('|'))
		form_tool.income_list.clear()
		form_tool.income_list.addItems(user[2].split('|'))
		form_tool.item_list.clear()
		form_tool.item_list.addItems(user[0].split('|'))
	 
	print("You clicked tool")
#--------------------------------------------------------------

#Кнопки окна добавления

#-----------------------------------------------нажатие на кнопку  "Add" (добавление)
def on_click_enter_purchase():
	if form.label_3.text() == 'Выберите тип покупки и карту':
		on_click_enter_purchase()
	else:
		on_click_enter_income()


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
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		print('файл уже существует')

	print(file['type'][0])
	#заполняем базу данных
	new_data = [0]*9


	if form.item_list.selectedItems() == []:
		new_data[0] = 'Другое'
	else:
		new_data[0] =  form.item_list.selectedItems()[0].text()


	if form.card_list.selectedItems() == []:
		new_data[1] = 'Другое'
	else:
		new_data[1] = form.card_list.selectedItems()[0].text()

	
	if date == '':
		form.label_3.clear()
		form.label_3.setText('ВЫБЕРИТЕ ДАТУ')
	else:
		new_data[4] = date.toString('yyyy MM dd')
		new_data[5] = date.day()
		new_data[6] = date.month()
		new_data[7] = date.year()
	
	#добавление если введено число
	if text.isnumeric() and new_data[4] != 0 :
		new_data[3] = -int(text)
		file = file.append(pd.DataFrame([new_data], columns=columns))
		file.to_csv('my_by.csv', index=False)
		form.label_2.clear()
		form.label_2.setStyleSheet("font-weight: family; color: black")
		form.label_2.setText('Введите сумму')
	elif form.label_3.text() != 'ВЫБЕРИТЕ ДАТУ':
		form.label_2.clear()
		form.label_2.setStyleSheet("font-weight: bold; color: red")
		form.label_2.setText('Надо число')

	form.lineEdit.clear()


	
	print(f'file:\n{file}')
	print("You clicked ok")
#------------------------------------------------------	


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
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		print('файл уже существует')

	print(file['type'][0])
	#заполняем базу данных
	new_data = [0]*9

	if form.income_list.selectedItems() == []:
		new_data[2] = 'Другое'
	else:
		new_data[2] =  form.income_list.selectedItems()[0].text()


	if form.card_list.selectedItems() == []:
		new_data[1] = 'Другое'
	else:
		new_data[1] = form.card_list.selectedItems()[0].text()

		
	if date == '':
		form.label_3.clear()
		form.label_3.setText('ВЫБЕРИТЕ ДАТУ')
	else:
		new_data[4] = date.toString('yyyy MM dd')
		new_data[5] = date.day()
		new_data[6] = date.month()
		new_data[7] = date.year()
	
	#добавление если введено число
	if text.isnumeric() and new_data[4] != 0 :
		new_data[3] = int(text)
		file = file.append(pd.DataFrame([new_data], columns=columns))
		file.to_csv('my_by.csv', index=False)
		form.label_2.clear()
		form.label_2.setStyleSheet("font-weight: family; color: black")
		form.label_2.setText('Введите сумму')
	elif form.label_3.text() != 'ВЫБЕРИТЕ ДАТУ':
		form.label_2.clear()
		form.label_2.setStyleSheet("font-weight: bold; color: red")
		form.label_2.setText('Надо число')
	
	print(f'file:\n{file}')
	print("You clicked ok")
#---------------------------------------------------------

#-----------------------------------------------нажатие на кнопку  "Поменять"
def on_click_change():
	if form.label_3.text() == 'Выберите тип покупки и карту':
		form.label_3.clear()
		form.label_3.setText('Выберите источник дохода и карту')
		form.enter_purchase_button.setText('Добавить доход')
		form.income_list.show()
		form.item_list.hide()
	else:
		form.label_3.clear()
		form.label_3.setText('Выберите тип покупки и карту')
		form.enter_purchase_button.setText('Добавить покупку')
		form.item_list.show()
		form.income_list.hide()	
	print("You clicked Change")
#---------------------------------------------------------

#Кнопки окна календаря
#--------------------------------------нажатие на календарь во втором окне (работает)
def on_click_calendar():
	
	form_all.textEdit.undo()

	print(form_all.textEdit.text())
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

#--------------------------------------нажатие на календарь во втором окне (работает)
def on_click_clendar():
	
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
#form_tool.add_income_button.clicked.connect(on_click_show)
def add_new_item():
	new = form_tool.add_item_field.text()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

	
	#заглядываем в базу данных
	#создаем базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		print(f'файл уже существует: \n{file}')

	user = (file[file["date"] == "user"].values)[0]
	if new in user[0]:
		form_tool.add_item_field.clear()
		form_tool.add_item_field.insert('Такой уже есть')
	else:
		print(f'{user} -> {type(user)}')
		user[0] = user[0] + f'|{new}'
		file[file["date"] == "user"] = user
		print(user)
		file.to_csv('my_by.csv', index=False)
	form_tool.item_list.clear()
	form.item_list.clear()
	form_tool.item_list.addItems(user[0].split('|'))
	form.item_list.addItems(user[0].split('|'))

	print("You added a new item")
	
#form_tool.add_card_button.clicked.connect(on_click_show)
def add_new_card():
		
	new = form_tool.add_card_field.text()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

	
	#заглядываем в базу данных
	#создаем базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		print(f'файл уже существует: \n{file}')

	user = (file[file["date"] == "user"].values)[0]
	if new in user[1]:
		form_tool.add_card_field.clear()
		form_tool.add_card_field.insert('Такой уже есть')
	else:
		print(f'{user} -> {type(user)}')
		user[1] = user[1] + f'|{new}'
		file[file["date"] == "user"] = user
		print(user)
		file.to_csv('my_by.csv', index=False)
	form_tool.list_card.clear()
	form.card_list.clear()
	form.card_list.addItems(user[1].split('|'))
	form_tool.list_card.addItems(user[1].split('|'))

	print("You added a new card")
#form_tool.add_item_button.clicked.connect(on_click_show)
def add_new_income():
	
	new = form_tool.add_income_field.text()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

	
	#заглядываем в базу данных
	#создаем базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		print(f'файл уже существует: \n{file}')

	user = (file[file["date"] == "user"].values)[0]
	if new in user[2]:
		form_tool.add_income_field.clear()
		form_tool.add_income_field.insert('Такой уже есть')
	else:
		print(f'{user} -> {type(user)}')
		user[2] = user[2] + f'|{new}'
		file[file["date"] == "user"] = user
		print(user)
		file.to_csv('my_by.csv', index=False)
	form_tool.income_list.clear()
	form.income_list.clear()
	form_tool.income_list.addItems(user[2].split('|'))
	form.income_list.addItems(user[2].split('|'))

	print("You added a new income")
#form_tool.delete_income_button.clicked.connect(on_click_show)
def delete_useless_item():
	new = form_tool.add_item_field.text()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

	
	#заглядываем в базу данных
	#создаем базу данных
	try:
	    file = pd.read_csv('my_by.csv')
	except IOError as e:
	    print(u'не удалось найти файл, так что создадим его')
	    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
	else:
		print(f'файл уже существует: \n{file}')

	user = (file[file["date"] == "user"].values)[0]
	if new in user[0]:
		form_tool.add_item_field.clear()
		form_tool.add_item_field.insert('Такой уже есть')
	else:
		print(f'{user} -> {type(user)}')
		user[0] = user[0] + f'|{new}'
		file[file["date"] == "user"] = user
		print(user)
		file.to_csv('my_by.csv', index=False)
	form_tool.item_list.clear()
	form.item_list.clear()
	form_tool.item_list.addItems(user[0].split('|'))
	form.item_list.addItems(user[0].split('|'))

	print("You added a new item")
	
	
#form_tool.delete_item_button.clicked.connect(on_click_show)

def delete_useless_income():
		for i in form_tool.item_list.selectedItems():
			print(i.text())
		


def delete_useless_incme():
	
	for i in range(len(tags)-1):
		if form.item_list.item(i).isSelected() == True:
			new_data[0] = tags[i]
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
#form_tool.delete_card_button.clicked.connect(on_click_show)
def delete_useless_card():
	
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







