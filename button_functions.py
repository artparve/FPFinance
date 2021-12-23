
#from interf_2 import *
#import sys

#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()

# ui.label.setText('sdfghjk')

# sys.exit(app.exec_())

from PyQt5 import uic, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import pandas as pd
from windows import *
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView

columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

#Общие кнопки
#-------------------------------------------переход к окну просмотра календаря +
def on_click_show():
	window.hide()
	window_tool.hide()
	on_click_calendar()
	window_all.show()

	print("You clicked Show Alllll")
#-------------------

#-------------------------------------------переход в окно добавления +
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
#-----------------------

#-------------------------------------------переход в окно настроек +
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
#-------------------


#Кнопки окна ДОБАВЛЕНИЯ
#-----------------------------------------------нажатие на кнопку  "Добавить ..." + 
def on_click_enter():
	if form.label_3.text() == 'Выберите тип покупки и карту':
		on_click_enter_purchase()
	else:
		on_click_enter_income()
#-----------------------------

#-----------------------------------------------нажатие на кнопку  "Добавить покупку" +
def on_click_enter_purchase():
	text = form.lineEdit.text()
	date = form.calendarWidget.selectedDate()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']
	file = pd.read_csv('my_by.csv')

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
		form.label_3.setStyleSheet("font-weight: bold; color: red")
	else:
		new_data[4] = date.toString('yyyy MM dd')
		new_data[5] = date.day()
		new_data[6] = date.month()
		new_data[7] = date.year()
	
	#добавление если введено число и дата
	if text.isnumeric() and new_data[4] != 0 :
		new_data[3] = -int(text)
		file = file.append(pd.DataFrame([new_data], columns=columns))
		file.to_csv('my_by.csv', index=False)

		form.label_2.clear()
		form.label_2.setStyleSheet("font-weight: family; color: black")
		form.label_2.setText('Введите сумму')

		form.label_2.clear()
		form.label_3.setStyleSheet("font-weight: family; color: black")
		form.label_2.setText('Выберите дату')
		
	elif form.label_3.text() != 'ВЫБЕРИТЕ ДАТУ':
		form.label_2.clear()
		form.label_2.setStyleSheet("font-weight: bold; color: red")
		form.label_2.setText('Надо число')

	form.lineEdit.clear()

	print(f'file:\n{file}')
	print("You clicked Добавить покупку")
#-----------------------------

#-----------------------------------------------нажатие на кнопку  "Добавить доход" +
def on_click_enter_income():
	text = form.lineEdit.text()
	date = form.calendarWidget.selectedDate()
	columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']
	file = pd.read_csv('my_by.csv')


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
#---------------------------

#-----------------------------------------------нажатие на кнопку  "Поменять" +
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
#---------------------


#Кнопки ГЛАВНОГО окна
#--------------------------------------нажатие на календарь во втором окне +
def on_click_calendar():
	
	form_all.textEdit.clear()

	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')
	
	data = file[file['date'] == form_all.calendarWidget.selectedDate().toString('yyyy MM dd')]
	if len(data) == 0:
		form_all.textEdit.append('Информации пока нет(')
	else:
		form_all.textEdit.append(f'{form_all.calendarWidget.selectedDate().toString("dd MMM yyyy")} Вы добавили:')
		for t in data['type'].unique():
			form_all.textEdit.append(f'{t}:')
			print(len(data[data['type']== t]))
			for i in range(len(data[data['type']== t])):
				print(i)
				form_all.textEdit.append(f"{list(data[data['type']== t]['card'])[i]}: {list(data[data['type']== t]['amount'])[i]} руб.")
	 
	print("You clicked Calendar")
#-----------------------

#--------------------------------------нажатие на на кнопку "Доходы" -
def on_click_graph_inc():

	size_s = str(form_all.graphic.size())
	coef = min(int(size_s[-4:-1]), int(size_s[-9:-6]))/ max(int(size_s[-4:-1]), int(size_s[-9:-6]))
	

	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')
	data = file[file['type'] == '0'][file['m'] == form_all.calendarWidget.selectedDate().month()]
	print(f'data:\n{data}')
	data = data.groupby(['income']).sum()
	
	data.plot.pie(y = 'amount', ylabel = '', title = f'Общий баланс: {file[file["m"] == form_all.calendarWidget.selectedDate().month()]["amount"].sum()}', legend = False, ).get_figure().savefig('test.jpg')
	# img = data.plot.pie(y = '', ylabel = '', legend = False).get_figure().savefig('test.jpg')
	
	# pix = QPixmap('test.jpg')
	# item = QtWidgets.QGraphicsPixmapItem(pix)
	# form_all.graphic.setScene(QtWidgets.QGraphicsScene().addItem(item))	

	
	scene = QtWidgets.QGraphicsScene()
	pixmap = QPixmap('test.jpg')
	print(pixmap.size())
	coef = int(str(pixmap.size())[-4:-1])/ int(str(pixmap.size())[-9:-6])
	pixmap = pixmap.scaled(coef*int(str(pixmap.size())[-9:-6]), coef*int(str(pixmap.size())[-4:-1]), QtCore.Qt.KeepAspectRatio)
	item = QtWidgets.QGraphicsPixmapItem(pixmap)
	scene.addItem(item)
	form_all.graphic.setScene(scene)
  
  	

	form_all.graphic.show()
	 
	print("You clicked Доходы")
#------------------------

#--------------------------------------нажатие на на кнопку "Расходы" -
def on_click_graph_purch():
	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')
	
	data = file[file['date'] == form_all.calendarWidget.selectedDate().toString('yyyy MM dd')]


		 
	print("You clicked Расходы")
#--------------------------

#Кнопки окна НАСТРОЕК

#--------------------------------------нажатие на на кнопку "Добавить" новый тип +
def add_new_item():
	new = form_tool.add_item_field.text()

	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')

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
#------------------

#--------------------------------------нажатие на на кнопку "Добавить" новую карту +
def add_new_card():
		
	new = form_tool.add_card_field.text()

	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')

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
#------------------

#--------------------------------------нажатие на на кнопку "Добавить" новый источник дохода +
def add_new_income():
	
	new = form_tool.add_income_field.text()
	
	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')
	
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
		form_tool.add_income_field.clear()

	form_tool.income_list.clear()
	form.income_list.clear()
	form_tool.income_list.addItems(user[2].split('|'))
	form.income_list.addItems(user[2].split('|'))

	print("You added a new income")
#--------------------

#--------------------------------------нажатие на на кнопку "Удалить" тип -
def delete_useless_item():

	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')

	# user = (file[file["date"] == "user"].values)[0]
	# if new in user[0]:
	# 	form_tool.add_item_field.clear()
	# 	form_tool.add_item_field.insert('Такой уже есть')
	# else:
	# 	print(f'{user} -> {type(user)}')
	# 	user[0] = user[0] + f'|{new}'
	# 	file[file["date"] == "user"] = user
	# 	print(user)
	# 	file.to_csv('my_by.csv', index=False)
	# form_tool.item_list.clear()
	# form.item_list.clear()
	# form_tool.item_list.addItems(user[0].split('|'))
	# form.item_list.addItems(user[0].split('|'))

	print(f"You deleted an item {1}")
#------------------

#--------------------------------------нажатие на на кнопку "Удалить" карту -
def delete_useless_card():

	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')

	# user = (file[file["date"] == "user"].values)[0]
	# if new in user[1]:
	# 	form_tool.add_card_field.clear()
	# 	form_tool.add_card_field.insert('Такой уже есть')
	# else:
	# 	print(f'{user} -> {type(user)}')
	# 	user[1] = user[1] + f'|{new}'
	# 	file[file["date"] == "user"] = user
	# 	print(user)
	# 	file.to_csv('my_by.csv', index=False)
	# form_tool.list_card.clear()
	# form.card_list.clear()
	# form.card_list.addItems(user[1].split('|'))
	# form_tool.list_card.addItems(user[1].split('|'))

	print(f"You deleted a card {1}")
#------------------

#--------------------------------------нажатие на на кнопку "Удалить" источник дохода -
def delete_useless_income():
	
	new = form_tool.add_income_field.text()
	
	#заглядываем в базу данных
	file = pd.read_csv('my_by.csv')
	
	# user = (file[file["date"] == "user"].values)[0]
	# if new in user[2]:
	# 	form_tool.add_income_field.clear()
	# 	form_tool.add_income_field.insert('Такой уже есть')
	# else:
	# 	print(f'{user} -> {type(user)}')
	# 	user[2] = user[2] + f'|{new}'
	# 	file[file["date"] == "user"] = user
	# 	print(user)
	# 	file.to_csv('my_by.csv', index=False)
	# 	form_tool.add_income_field.clear()

	# form_tool.income_list.clear()
	# form.income_list.clear()
	# form_tool.income_list.addItems(user[2].split('|'))
	# form.income_list.addItems(user[2].split('|'))

	print(f"You deleted an income {1}")
#--------------------








