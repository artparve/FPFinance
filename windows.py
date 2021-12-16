import pandas as pd
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
from graphics import *

#Создание окон
#---------------------------------------------создание окна добавления покупок
Form, Window = uic.loadUiType("interf_2.ui")

app = QApplication([])
size = app.primaryScreen().size()
window = Window()
form = Form()
form.setupUi(window)
window.hide()

#----------------------------------------------создание окна календаря
Form_all, Window_all = uic.loadUiType("interf_show.ui")
window_all = Window_all()
form_all = Form_all()
form_all.setupUi(window_all)
window_all.hide()
graphicsInterfShow(window_all, size)
# window_all.resize(size.width(), size.height())

#----------------------------------------------создание окна настроек
Form_tool, Window_tool = uic.loadUiType("interf_tool.ui")
window_tool = Window_tool()
form_tool = Form_tool()
form_tool.setupUi(window_tool)
window_tool.show()

#----------------------------------------------создание окна предупреждения
Form_w, Window_w = uic.loadUiType("warning.ui")
window_w = Window_w()
form_w = Form_w()
form_w.setupUi(window_w)
window_w.hide()

#----------------------------------------------создание окна добавления дохода
Form_inc, Window_inc = uic.loadUiType("interf_income.ui")
window_inc = Window_inc()
form_inc = Form_inc()
form_inc.setupUi(window_inc)
window_inc.hide()
#------------------------------------------------