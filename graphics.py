from PyQt5 import QtCore, QtGui, QtWidgets

def graphicsInterfBoth(form, window, size):
	w = size.width()
	h = size.height()
	window.resize(w, h)
	window.move(0, 0)	
	form.label.setGeometry(QtCore.QRect(w * 0.35, 10, w * 0.3, 100))
	
	form.label_2.setGeometry(QtCore.QRect(w * 0.2, 60, 800, 50))
	form.label_3.setGeometry(QtCore.QRect(w * 0.2, 170, 800, 50))
	form.enter_purchase_button.setGeometry(QtCore.QRect(w * 0.15, h * 0.75, w * 0.3, 70))
	form.enter_purchase_button_2.setGeometry(QtCore.QRect(w * 0.15, h * 0.85, w * 0.3, 70))
	form.lineEdit.setGeometry(QtCore.QRect(w * 0.2, h * 0.2, w * 0.2, 50))
	form.item_list.setGeometry(QtCore.QRect(w * 0.325, h * 0.35, w * 0.225, h * 0.37))
	form.calendarWidget.setGeometry(QtCore.QRect(w * 0.6, h * 0.2, w * 0.35, h * 0.42))
	form.show_all_button.setGeometry(QtCore.QRect(w * 0.635, h * 0.7, 550, 100))
	form.toolButton.setGeometry(QtCore.QRect(w * 0.95, 10, 50, 100))
	form.card_list.setGeometry(QtCore.QRect(w * 0.05, h * 0.35, w * 0.225, h * 0.37))
	form.income_list.setGeometry(QtCore.QRect(w * 0.05, h * 0.35, w * 0.225, h * 0.37))
	form.label_4.setGeometry(QtCore.QRect(380, 170, 400, 50))
	form.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))#?????


def graphicsInterfShow(form, window, size):
	w = size.width()
	h = size.height()
	window.resize(w, h)
	window.move(0, 0)
	window.setIconSize(QtCore.QSize(w, h))
	form.calendarWidget.setGeometry(QtCore.QRect(w * 0.6, h * 0.2, w * 0.35, h * 0.42))
	form.add_purchase_button.setGeometry(QtCore.QRect(w * 0.635, h * 0.7, 550, 100))
	form.textEdit.setGeometry(QtCore.QRect(w * 0.4, h * 0.2, w * 0.18, h * 0.42))
	form.toolButton.setGeometry(QtCore.QRect(w * 0.95, 10, 50, 100))
	form.toolButton.setIconSize(QtCore.QSize(50, 50))
	form.label_2.setGeometry(QtCore.QRect(w * 0.35, 10, w * 0.3, 100))
	form.graphic.setGeometry(QtCore.QRect(w * 0.05, h * 0.2, w * 0.33, h * 0.42))
	form.graph_purchase_button.setGeometry(QtCore.QRect(w * 0.08, h * 0.7, 200, 100))
	form.graph_income_button.setGeometry(QtCore.QRect(w * 0.25, h * 0.7, 200, 100))
	form.menubar.setGeometry(QtCore.QRect(0, 0, 800, 100))#???????


def graphicsInterfTool(form, window, size):
	w = size.width()
	h = size.height()
	window.resize(w, h)
	window.move(0, 0)
	form.label.setGeometry(QtCore.QRect(w * 0.35, 10, w * 0.3, 100))

	form.label_3.setGeometry(QtCore.QRect(w * 0.4, h * 0.11, w * 0.2, 50))
	form.item_list.setGeometry(QtCore.QRect(w * 0.15, h * 0.11, w * 0.2, h * 0.2))
	form.add_item_button.setGeometry(QtCore.QRect(w * 0.7, h * 0.13, 200, 70))
	form.delete_item_button.setGeometry(QtCore.QRect(w * 0.7, h * 0.225, 200, 70))
	form.add_item_field.setGeometry(QtCore.QRect(w * 0.4, h * 0.16, w * 0.2, 70))
	form.label_6.setGeometry(QtCore.QRect(w * 0.4, h * 0.23, w * 0.2, 50))
	form.card_list_4.setGeometry(QtCore.QRect(w * 0.4, h * 0.26, w * 0.2, 50))

	form.card_list.setGeometry(QtCore.QRect(w * 0.4, h * 0.36, w * 0.2, 50))
	form.list_card.setGeometry(QtCore.QRect(w * 0.15, h * 0.36, w * 0.2, h * 0.2))
	form.add_card_button.setGeometry(QtCore.QRect(w * 0.7, h * 0.38, 200, 70))
	form.delete_card_button.setGeometry(QtCore.QRect(w * 0.7, h * 0.475, 200, 70))
	form.add_card_field.setGeometry(QtCore.QRect(w * 0.4, h * 0.41, w * 0.2, 70))
	form.label_5.setGeometry(QtCore.QRect(w * 0.4, h * 0.48, w * 0.2, 50))
	form.card_list_5.setGeometry(QtCore.QRect(w * 0.4, h * 0.51, w * 0.2, 50))

	form.card_list_2.setGeometry(QtCore.QRect(w * 0.35, h * 0.61, w * 0.3, 50))
	form.income_list.setGeometry(QtCore.QRect(w * 0.15, h * 0.61, w * 0.2, h * 0.2))
	form.add_income_button.setGeometry(QtCore.QRect(w * 0.7, h * 0.63, 200, 70))
	form.delete_income_button.setGeometry(QtCore.QRect(w * 0.7, h * 0.725, 200, 70))
	form.add_income_field.setGeometry(QtCore.QRect(w * 0.4, h * 0.66, w * 0.2, 70))
	form.card_list_3.setGeometry(QtCore.QRect(w * 0.35, h * 0.73, w * 0.3, 50))
	form.card_list_6.setGeometry(QtCore.QRect(w * 0.4, h * 0.76, w * 0.2, 50))
	
	form.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))#?????
	form.show_all_button.setGeometry(QtCore.QRect(w * 0.6, h * 0.83, 550, 100))


def graphicsInterfW(window, size):
	window.resize(size.width(), size.height())


def graphicsInterfInc(form, window, size):
	w = size.width()
	h = size.height()
	window.resize(w, h)
	window.move(0, 0)
	font = QtGui.QFont()
	font.setFamily("Segoe Print")
	font.setPointSize(16)
	window.setFont(font)
	window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
	window.setIconSize(QtCore.QSize(800, 800))
	window.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
	form.centralwidget.setObjectName("centralwidget")
	form.label.setEnabled(True)
	form.label.setGeometry(QtCore.QRect(0, 0, 800, 60))
	font = QtGui.QFont()
	font.setPointSize(32)
	form.label.setFont(font)
	form.label.setTextFormat(QtCore.Qt.PlainText)
	form.label.setAlignment(QtCore.Qt.AlignCenter)
	form.label.setObjectName("label")
	form.label_2.setGeometry(QtCore.QRect(0, 60, 800, 50))
	font = QtGui.QFont()
	font.setPointSize(16)
	form.label_2.setFont(font)
	form.label_2.setAlignment(QtCore.Qt.AlignCenter)
	form.label_2.setObjectName("label_2")
	form.label_3.setGeometry(QtCore.QRect(0, 170, 800, 50))
	font = QtGui.QFont()
	font.setPointSize(16)
	form.label_3.setFont(font)
	form.label_3.setAlignment(QtCore.Qt.AlignCenter)
	form.label_3.setObjectName("label_3")
	font = QtGui.QFont()
	font.setPointSize(24)
	form.enter_income_button.setGeometry(QtCore.QRect(50, 660, 350, 51))
	form.enter_income_button.setFont(font)
	form.enter_income_button.setObjectName("enter_income_button")
	form.lineEdit.setGeometry(QtCore.QRect(300, 110, 200, 50))
	font = QtGui.QFont()
	font.setPointSize(16)
	form.lineEdit.setFont(font)
	form.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
	form.lineEdit.setObjectName("lineEdit")
	form.income_list.setEnabled(True)
	form.income_list.setGeometry(QtCore.QRect(30, 230, 150, 400))
	form.income_list.setMinimumSize(QtCore.QSize(101, 0))
	font = QtGui.QFont()
	font.setFamily("Segoe Print")
	font.setPointSize(16)
	form.income_list.setFont(font)
	form.income_list.setLayoutDirection(QtCore.Qt.LeftToRight)
	form.income_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
	form.income_list.setFrameShadow(QtWidgets.QFrame.Plain)
	form.income_list.setAlternatingRowColors(True)
	form.income_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
	form.income_list.setLayoutMode(QtWidgets.QListView.SinglePass)
	form.income_list.setObjectName("income_list")
	form.calendarWidget.setGeometry(QtCore.QRect(370, 230, 400, 400))
	font = QtGui.QFont()
	font.setPointSize(16)
	form.calendarWidget.setFont(font)
	form.calendarWidget.setObjectName("calendarWidget")
	form.show_all_button.setGeometry(QtCore.QRect(450, 660, 300, 50))
	font = QtGui.QFont()
	font.setPointSize(24)
	font.setBold(False)
	font.setWeight(50)
	form.show_all_button.setFont(font)
	form.show_all_button.setObjectName("show_all_button")
	form.toolButton.setGeometry(QtCore.QRect(720, 10, 50, 50))
	form.toolButton.setAutoFillBackground(True)
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap("tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	form.toolButton.setIcon(icon)
	form.toolButton.setIconSize(QtCore.QSize(50, 50))
	form.toolButton.setShortcut("")
	form.toolButton.setAutoRepeat(False)
	form.toolButton.setPopupMode(QtWidgets.QToolButton.InstantPopup)
	form.toolButton.setAutoRaise(True)
	form.toolButton.setObjectName("toolButton")
	form.card_list.setEnabled(True)
	form.card_list.setGeometry(QtCore.QRect(200, 230, 150, 400))
	form.card_list.setMinimumSize(QtCore.QSize(101, 0))
	font = QtGui.QFont()
	font.setFamily("Segoe Print")
	font.setPointSize(16)
	form.card_list.setFont(font)
	form.card_list.setLayoutDirection(QtCore.Qt.LeftToRight)
	form.card_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
	form.card_list.setFrameShadow(QtWidgets.QFrame.Plain)
	form.card_list.setAlternatingRowColors(True)
	form.card_list.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
	form.card_list.setLayoutMode(QtWidgets.QListView.SinglePass)
	form.card_list.setObjectName("card_list")
	form.income_list.raise_()
	form.label.raise_()
	form.label_2.raise_()
	form.label_3.raise_()
	form.enter_income_button.raise_()
	form.lineEdit.raise_()
	form.calendarWidget.raise_()
	form.show_all_button.raise_()
	form.toolButton.raise_()
	form.card_list.raise_()
	window.setCentralWidget(form.centralwidget)
	form.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
	form.menubar.setObjectName("menubar")
	window.setMenuBar(form.menubar)
	form.statusbar.setObjectName("statusbar")
	window.setStatusBar(form.statusbar)

	form.retranslateUi(window)
	form.income_list.setCurrentRow(-1)
	form.card_list.setCurrentRow(-1)
	QtCore.QMetaObject.connectSlotsByName(window)