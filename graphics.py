from PyQt5 import QtCore, QtGui, QtWidgets

def graphicsInterf2(window, size):
	window.resize(size.width(), size.height())


def graphicsInterfShow(form, window, size):
	window.resize(size.width(), size.height())
	font = QtGui.QFont()
	font.setFamily("Segoe Print")
	font.setPointSize(16)
	window.setFont(font)
	window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
	window.setIconSize(QtCore.QSize(800, 800))

	form.centralwidget.setObjectName("centralwidget")
	form.calendarWidget.setGeometry(QtCore.QRect(350, 100, 400, 500))
	form.calendarWidget.setObjectName("calendarWidget")
	form.add_purchase_button.setGeometry(QtCore.QRect(30, 640, 350, 60))
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
	sizePolicy.setHorizontalStretch(0)
	sizePolicy.setVerticalStretch(0)
	sizePolicy.setHeightForWidth(form.add_purchase_button.sizePolicy().hasHeightForWidth())
	form.add_purchase_button.setSizePolicy(sizePolicy)
	font = QtGui.QFont()
	font.setPointSize(24)
	form.add_purchase_button.setFont(font)
	form.add_purchase_button.setObjectName("add_purchase_button")
	form.textEdit.setGeometry(QtCore.QRect(50, 150, 250, 400))
	form.textEdit.setObjectName("textEdit")
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
	form.label_2.setEnabled(True)
	form.label_2.setGeometry(QtCore.QRect(100, 0, 600, 60))
	font = QtGui.QFont()
	font.setPointSize(32)
	form.label_2.setFont(font)
	form.label_2.setTextFormat(QtCore.Qt.PlainText)
	form.label_2.setAlignment(QtCore.Qt.AlignCenter)
	form.label_2.setObjectName("label_2")
	form.add_income_button.setGeometry(QtCore.QRect(420, 640, 350, 60))
	sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
	sizePolicy.setHorizontalStretch(0)
	sizePolicy.setVerticalStretch(0)
	sizePolicy.setHeightForWidth(form.add_income_button.sizePolicy().hasHeightForWidth())
	form.add_income_button.setSizePolicy(sizePolicy)
	font = QtGui.QFont()
	font.setPointSize(24)
	form.add_income_button.setFont(font)
	form.add_income_button.setObjectName("add_income_button")
	window.setCentralWidget(form.centralwidget)
	form.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
	form.menubar.setObjectName("menubar")
	window.setMenuBar(form.menubar)
	form.statusbar.setObjectName("statusbar")
	window.setStatusBar(form.statusbar)
	form.retranslateUi(window)
	QtCore.QMetaObject.connectSlotsByName(window)


def graphicsInterfTool(window, size):
	window.resize(size.width(), size.height())


def graphicsInterfW(window, size):
	window.resize(size.width(), size.height())


def graphicsInterfInc(window, size):
	window.resize(size.width(), size.height())