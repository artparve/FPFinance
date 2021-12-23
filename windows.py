import pandas as pd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from graphics import *
#Создание окон
#---------------------------------------------создание окна добавления покупок
Form, Window = uic.loadUiType("interf_both.ui")

app = QApplication([])
size = app.primaryScreen().size()
window = Window()
form = Form()
form.setupUi(window)
graphicsInterfBoth(form, window, size)
window.hide()

#----------------------------------------------создание окна календаря
Form_all, Window_all = uic.loadUiType("interf_show_graph.ui")
window_all = Window_all()
form_all = Form_all()
form_all.setupUi(window_all)
graphicsInterfShow(form_all, window_all, size)
columns= ['type','card','income','amount', 'date', 'd', 'm', 'y', 'comment']

#создаем или подгружаем базу данных
try:
    file = pd.read_csv('my_by.csv')
except IOError as e:
    form_all.textEdit.append('Информации пока нет(')
    file = pd.DataFrame([['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'base', 0, 0, 0, ''], 
	    	['Транспорт|Продукты|Комуналка|Другое', 'Карта 1|Другое', 'Зарплата|Другое', 0, 'user', 0, 0, 0, '']], columns=columns)
    file.to_csv('my_by.csv', index=False)
else:
	data = file[file['date'] == form_all.calendarWidget.selectedDate().toString('yyyy MM dd')]
	if len(data) == 0:
		form_all.textEdit.append('Информации пока нет(')
	else:
		form_all.textEdit.append(f'{form_all.calendarWidget.selectedDate().toString("dd MMM yyyy")} Вы добавили:')
		for t in data['type'].unique():
			form_all.textEdit.append(f'{t}:')
			print(len(data[data['type']== t]))
			for i in range(len(data[data['type']== t])):
				form_all.textEdit.append(f"{list(data[data['type']== t]['card'])[i]}: {list(data[data['type']== t]['amount'])[i]} руб.")

window_all.show()

#----------------------------------------------создание окна настроек
Form_tool, Window_tool = uic.loadUiType("interf_tool.ui")
window_tool = Window_tool()
form_tool = Form_tool()
form_tool.setupUi(window_tool)
graphicsInterfTool(form_tool, window_tool, size)
window_tool.hide()
