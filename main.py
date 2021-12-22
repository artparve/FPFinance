
#from interf_2 import *
#import sys

#app = QtWidgets.QApplication(sys.argv)
#MainWindow = QtWidgets.QMainWindow()
#ui = Ui_MainWindow()
#ui.setupUi(MainWindow)
#MainWindow.show()

# ui.label.setText('sdfghjk')

# sys.exit(app.exec_())
from button_functions import *
from windows import *
from PyQt5 import uic
import pandas as pd
from PyQt5.QtWidgets import QApplication

#Действия
#-------------------------------------------действия в окне добавления покупок
form.enter_purchase_button.clicked.connect(on_click_enter_purchase)
form.show_all_button.clicked.connect(on_click_show)
form.toolButton.clicked.connect(on_click_tool)
form.enter_purchase_button_2.clicked.connect(on_click_change)

#-------------------------------------------действия в окне с календарем
#form_all.add_income_button.clicked.connect(on_click_income)
form_all.add_purchase_button.clicked.connect(on_click_purchase)
form_all.calendarWidget.clicked.connect(on_click_calendar)
form_all.toolButton.clicked.connect(on_click_tool)

#-------------------------------------------действия в окне настроек
form_tool.show_all_button.clicked.connect(on_click_show)
form_tool.add_income_button.clicked.connect(add_new_income)
form_tool.add_card_button.clicked.connect(add_new_card)
form_tool.add_item_button.clicked.connect(add_new_item)
form_tool.delete_income_button.clicked.connect(on_click_show)
form_tool.delete_item_button.clicked.connect(delete_useless_income)
form_tool.delete_card_button.clicked.connect(on_click_show)

app.exec()