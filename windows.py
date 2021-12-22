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
window_all.show()
graphicsInterfShow(form_all, window_all, size)

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


window_all.show()

#----------------------------------------------создание окна настроек
Form_tool, Window_tool = uic.loadUiType("interf_tool.ui")
window_tool = Window_tool()
form_tool = Form_tool()
form_tool.setupUi(window_tool)
graphicsInterfTool(form_tool, window_tool, size)
window_tool.hide()
