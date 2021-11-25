
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
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("interf.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
form.listWidget.addItem("Trrrrr")

def on_click():
	print(form.lineEdit.text())

	print(form.listWidget.selectedItems())
	print("You clicked ok")

form.pushButton.clicked.connect(on_click)




app.exec()