# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interf_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.enter_purchase_button = QtWidgets.QPushButton(self.centralwidget)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.item_list = QtWidgets.QListWidget(self.centralwidget)
        item = QtWidgets.QListWidgetItem()
        self.item_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_list.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.item_list.addItem(item)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.show_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.card_list = QtWidgets.QListWidget(self.centralwidget)
        item = QtWidgets.QListWidgetItem()
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Financial analyser"))
        self.label_2.setText(_translate("MainWindow", "Добавить сумму"))
        self.label_3.setText(_translate("MainWindow", "Выберите тип, карту и дату"))
        self.enter_purchase_button.setText(_translate("MainWindow", "Добавить покупку"))
        __sortingEnabled = self.item_list.isSortingEnabled()
        self.item_list.setSortingEnabled(False)
        item = self.item_list.item(0)
        item.setText(_translate("MainWindow", "Транспорт"))
        item = self.item_list.item(1)
        item.setText(_translate("MainWindow", "Продукты"))
        item = self.item_list.item(2)
        item.setText(_translate("MainWindow", "Коммуналка"))
        self.item_list.setSortingEnabled(__sortingEnabled)
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
