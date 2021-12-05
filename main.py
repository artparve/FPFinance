
#from interf_2 import *
#import sys

#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()

# ui.label.setText('sdfghjk')

# sys.exit(app.exec_())
from button_functions import on_click_enter_purchase
from PyQt5 import uic
import pandas as pd
from PyQt5.QtWidgets import QApplication

#Создание окон
#---------------------------------------------создание окна добавления покупок
Form, Window = uic.loadUiType("interf_2.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

#----------------------------------------------создание окна календаря
Form_all, Window_all = uic.loadUiType("interf_show.ui")
window_all = Window_all()
form_all = Form_all()
form_all.setupUi(window_all)
window_all.hide()

#----------------------------------------------создание окна настроек
Form_tool, Window_tool = uic.loadUiType("interf_tool.ui")
window_tool = Window_tool()
form_tool = Form_tool()
form_tool.setupUi(window_tool)
window_tool.hide()

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


#Действия
#-------------------------------------------действия в окне добавления покупок
form.enter_purchase_button.clicked.connect(on_click_enter_purchase)
form.show_all_button.clicked.connect(on_click_show)
form.toolButton.clicked.connect(on_click_tool)

#-------------------------------------------действия в окне добавления дохода
form_inc.enter_income_button.clicked.connect(on_click_enter_purchase)
form_inc.show_all_button.clicked.connect(on_click_show)
form_inc.toolButton.clicked.connect(on_click_tool)


#-------------------------------------------действия в окне с календарем
form_all.add_income_button.clicked.connect(on_click_income)
form_all.add_purchase_button.clicked.connect(on_click_enter_purchase)
form_all.calendarWidget.clicked.connect(on_click_calendar)
form_all.toolButton.clicked.connect(on_click_tool)

#-------------------------------------------действия в окне настроек
#form_tool.enter_purchase_button.clicked.connect(on_click_add_purchase)
#form_tool.show_all_button.clicked.connect(on_click_show)
#Form_tool.toolButton.clicked.connect(on_click_tool)




app.exec()