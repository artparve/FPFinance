# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interf_income.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.enter_income_button = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.income_list = QtWidgets.QListWidget(self.centralwidget)
        item = QtWidgets.QListWidgetItem()
        self.income_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.income_list.addItem(item)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.show_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.card_list = QtWidgets.QListWidget(self.centralwidget)
        item = QtWidgets.QListWidgetItem()
        self.card_list.addItem(item)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Financial analyser"))
        self.label_2.setText(_translate("MainWindow", "Добавить сумму"))
        self.label_3.setText(_translate("MainWindow", "Выберите источник дохода, карту и дату"))
        self.enter_income_button.setText(_translate("MainWindow", "Добавить доход"))
        __sortingEnabled = self.income_list.isSortingEnabled()
        self.income_list.setSortingEnabled(False)
        item = self.income_list.item(0)
        item.setText(_translate("MainWindow", "Зарплата"))
        item = self.income_list.item(1)
        item.setText(_translate("MainWindow", "Перевод"))
        self.income_list.setSortingEnabled(__sortingEnabled)
        self.show_all_button.setText(_translate("MainWindow", "Посмотреть все"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        __sortingEnabled = self.card_list.isSortingEnabled()
        self.card_list.setSortingEnabled(False)
        item = self.card_list.item(0)
        item.setText(_translate("MainWindow", "Карта 1"))
        self.card_list.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
