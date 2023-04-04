import sys
import sqlite3
import csv
import requests

from random import choice

from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QTableWidgetItem, QMainWindow, QAbstractItemView, \
    QComboBox, QLineEdit, QSpinBox, QAbstractSpinBox, QDoubleSpinBox, QPushButton, QCheckBox, \
    QTableWidget, QColumnView, QFileDialog
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt


class UiForm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 290)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 261))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 1, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 1, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.commandLinkButton.setText(_translate("Dialog", "Случайный выбор"))
        self.radioButton.setText(_translate("Dialog", "Вид 1"))
        self.radioButton_2.setText(_translate("Dialog", "Вид 2"))
        self.pushButton_2.setText(_translate("Dialog", "Удалить строку"))
        self.pushButton_3.setText(_translate("Dialog", "Добавить строку"))
        self.pushButton_4.setText(_translate("Dialog", "Изменить строку"))


class RandomClothesForm(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 394)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 462, 370))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.gridLayoutWidget)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.gridLayout.addWidget(self.commandLinkButton, 0, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 2)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.commandLinkButton.setText(_translate("Dialog", "Таблица"))
        self.pushButton.setText(_translate("Dialog", "Случайная одежда"))
        self.label.setText(_translate("Dialog", "Критерии"))
        self.label_2.setText(_translate("Dialog", "Подборка"))


class Ad(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 225)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 9, 371, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 12, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 12, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 3, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom)
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_9.setText(_translate("Form", "от ft"))
        self.label_3.setText(_translate("Form", "Название (с большой буквы)"))
        self.label_4.setText(_translate("Form", "Здесь картинка"))
        self.label_8.setText(_translate("Form", "Сезон"))
        self.label_10.setText(_translate("Form", "до tt"))
        self.label_5.setText(_translate("Form", "Для температуры:"))
        self.label.setText(_translate("Form", "Цена:"))
        self.label_7.setText(_translate("Form", "Погода"))
        self.label_6.setText(_translate("Form", "Категория"))
        self.label_2.setText(_translate("Form", "ID:"))


class DoSmtWithLineForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 316)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 305))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox.setMinimum(-999999999.99)
        self.doubleSpinBox.setMaximum(999999999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 3, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 9, 0, 1, 4)
        self.line_8 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 2, 1, 3, 1)
        self.line = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 5, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 14, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 10, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 14, 1, 1, 2)
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setText("<--")
        self.gridLayout.addWidget(self.pushButton, 14, 3, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 4)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 3, 2, 1, 2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_2.setMinimum(-999999999.99)
        self.doubleSpinBox_2.setMaximum(999999999.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout.addWidget(self.doubleSpinBox_2, 4, 3, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBox_3.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.doubleSpinBox_3.setMaximum(999999999.99)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 12, 1, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 4)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 16, 0, 1, 4)
        self.line_7 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 11, 0, 1, 4)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 10, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 3, 1)
        self.line_5 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 13, 0, 1, 4)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 8, 1, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 6, 1, 1, 3)
        self.line_9 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 15, 0, 1, 4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить строку"))
        self.label.setText(_translate("Form", "Назвние:"))
        self.label_9.setText(_translate("Form", "Фото:"))
        self.label_7.setText(_translate("Form", "Категория:"))
        self.label_4.setText(_translate("Form", "от:"))
        self.label_6.setText(_translate("Form", "Сезон:"))
        self.label_3.setText(_translate("Form", "Погода:"))
        self.label_8.setText(_translate("Form", "Цена:"))
        self.label_5.setText(_translate("Form", "до:"))
        self.label_2.setText(_translate("Form", "Температура"))


class SelectCityForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 296)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(7, 9, 381, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.gridLayoutWidget)
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Выбрать город"))


class SelectCity(QMainWindow, SelectCityForm):
    def __init__(self, btn, table, func, temp_mode=True):
        """Виджет выбора города"""
        super().__init__()
        self.setupUi(self)
        self.btn = btn
        self.table = table
        self.func = func
        self.temp_mode = temp_mode
        self.initUI()

    def initUI(self):
        self.red_palette = QtGui.QPalette()
        self.red_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 0, 0))
        self.black_palette = QtGui.QPalette()
        self.black_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(0, 0, 0))

        self.setCentralWidget(self.gridLayoutWidget)
        self.setFixedSize(self.size().width(), self.size().height())
        self.lineEdit.textChanged.connect(self.find_cities)
        self.buttonBox.clicked.connect(self.check_finded)
        self.find_cities()

    def check_finded(self, button):
        """Проверяет - найден ли город"""
        if button.text() == "Cancel":
            self.close()
        elif self.comboBox.currentText() != "":
            set_text_for_button(self.btn, self.comboBox.currentText(), self.temp_mode)
            self.table.resizeRowsToContents()
            self.table.resizeColumnsToContents()
            if self.func:
                self.func()
            self.close()
        self.lineEdit.setPalette(self.red_palette)

    def find_cities(self):
        """Меняет выбор в comboBox'е"""
        self.comboBox.clear()
        finded = [city for city in cities_id
                  if self.lineEdit.text().lower() in city.lower()][:100]
        self.comboBox.addItems(finded)
        if finded:
            self.lineEdit.setPalette(self.black_palette)


class AdBase(QMainWindow, Ad):
    def __init__(self, args):
        """Виджет, отображающий информацию об одежде"""
        super().__init__()
        self.setupUi(self)
        self.args = args
        self.initUI()

    def initUI(self):
        self.setCentralWidget(self.gridLayoutWidget)

        self.setWindowTitle(f"{self.args[1].capitalize()}({self.args[0]})")

        self.label.setText(f"Цена: {self.args[7]}")
        self.label_2.setText(f"ID: {self.args[0]}")
        self.label_3.setText(self.args[1].capitalize())
        self.label_4.setPixmap(QPixmap(self.args[8]).scaledToHeight(200)
                               if max((pixmap := QPixmap(self.args[8])).height(),
                                      pixmap.width()) == pixmap.height()
                               else QPixmap(self.args[8]).scaledToWidth(200))
        self.label_6.setText(reverse_dictionary(categories)[self.args[6]])
        self.label_7.setText(reverse_dictionary(weather)[self.args[4]])
        self.label_8.setText(reverse_dictionary(seasons)[self.args[5]])
        self.label_9.setText(f"от {self.args[2]}")
        self.label_10.setText(f"до {self.args[3]}")

        self.setFixedSize(0, 0)


class DoSmtWithLine(QMainWindow, DoSmtWithLineForm):
    def __init__(self, add_mode=True, info=None, id=None):
        """Виджет с помощью которого можно поменять или добавить строку в таблицу"""
        super().__init__()
        self.setupUi(self)
        self.add_mode = add_mode
        self.info = info
        self.id = id
        self.initUI()

    def initUI(self):
        self.red_palette = QtGui.QPalette()
        self.red_palette.setColor(QtGui.QPalette.Text, QColor(255, 0, 0))
        self.black_palette = QtGui.QPalette()
        self.black_palette.setColor(QtGui.QPalette.Text, QColor(0, 0, 0))

        self.setCentralWidget(self.gridLayoutWidget)
        self.setFixedSize(self.size().width(), self.size().height())

        self.comboBox.addItems(get_titles("weather"))
        self.comboBox_2.addItems(get_titles("seasons"))
        self.comboBox_3.addItems(get_titles("categories"))
        self.buttonBox.clicked.connect(self.check_settings)
        self.pushButton.clicked.connect(self.select_picture)

        if not self.add_mode:
            self.lineEdit.setText(self.info[0])
            self.doubleSpinBox.setValue(self.info[1])
            self.doubleSpinBox_2.setValue(self.info[2])
            self.comboBox.setCurrentText(reverse_dictionary(weather)[self.info[3]])
            self.comboBox_2.setCurrentText(reverse_dictionary(seasons)[self.info[4]])
            self.comboBox_3.setCurrentText(reverse_dictionary(categories)[self.info[5]])
            self.doubleSpinBox_3.setValue(self.info[6])
            self.lineEdit_2.setText(self.info[7])

    def select_picture(self):
        self.lineEdit_2.setText(f[0] if
                                (f := QFileDialog.getOpenFileName(self, 'Выбрать картинку', '',
                                                                  'Картинка (*.jpg);;Картинка '
                                                                  '(*.png)'))[0]
                                else self.lineEdit_2.text())

    def check_settings(self, button):
        """Вызывается при нажатии 'OK' или 'Cancel', проверяет правильно ли все заполнено"""
        if button.text() == "OK":
            self.doubleSpinBox.setPalette(self.red_palette if
                                          self.doubleSpinBox.value() > self.doubleSpinBox_2.value()
                                          else self.black_palette)
            self.doubleSpinBox_2.setPalette(self.red_palette if
                                            self.doubleSpinBox.value() > self.doubleSpinBox_2.value()
                                            else self.black_palette)
            if self.doubleSpinBox.value() <= self.doubleSpinBox_2.value():
                cur.execute(f"INSERT INTO clothes(title, ft, tt, weather, "
                            f"season, category, cost, linkphoto) VALUES('{self.lineEdit.text()}', "
                            f"{self.doubleSpinBox.value()}, {self.doubleSpinBox_2.value()}, "
                            f"{weather[self.comboBox.currentText()]}, "
                            f"{seasons[self.comboBox_2.currentText()]}, "
                            f"{categories[self.comboBox_3.currentText()]}, "
                            f"{self.doubleSpinBox_3.value()}, "
                            f"'{self.lineEdit_2.text()}')" if self.add_mode else
                            f"UPDATE clothes SET title='{self.lineEdit.text()}', "
                            f"ft={self.doubleSpinBox.value()}, tt={self.doubleSpinBox_2.value()}, "
                            f"weather={weather[self.comboBox.currentText()]}, "
                            f"season={seasons[self.comboBox_2.currentText()]}, "
                            f"category={categories[self.comboBox_3.currentText()]}, "
                            f"cost={self.doubleSpinBox_3.value()}, "
                            f"linkphoto='{self.lineEdit_2.text()}' WHERE id={self.id}")
                [table.find_items() for table in tables]
                con.commit()
                self.close()
        else:
            self.close()


class FindWidget(QMainWindow):
    def __init__(self, coords, layout_widget, window, statements, for_compare,
                 always_update=True, one_item=False, category=None):
        """Виджет, в котором таблица с условиями, таблица с найденной одеждой и кнопкой для
        добавления условий"""
        super().__init__()
        self.coords = coords
        self.layout = layout_widget.layout()
        self.layoutWidget = layout_widget
        self.window = window
        self.statements = statements  # Знаки для сравнения на каждый вариант из первого comboBox'а
        self.for_compare = for_compare  # Варианты для выбора для третьего comboBox'а
        self.always_update = always_update  # Изменяется ли при любом обновлении условий
        self.one_item = one_item
        self.category = category  # Одежда только такой категории может проходить проверку
        self.initUI()

    def initUI(self):
        self.pushButton = QPushButton(self.window)  # Кнопка для создания условий
        self.pushButton.setText("+")
        self.layout.addWidget(self.pushButton, *self.coords[0])
        self.pushButton.clicked.connect(self.add_if)

        self.tableWidget = QTableWidget(self.layoutWidget)  # Таблица с условиями
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(4)
        self.layout.addWidget(self.tableWidget, *self.coords[1])

        self.tableWidget_2 = QTableWidget(self.layoutWidget)  # Таблица с найденной одеждой
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget_2.doubleClicked.connect(self.show_ad)
        self.layout.addWidget(self.tableWidget_2, *self.coords[2])

        self.combo_boxes = []
        self.btns = []
        self.first_look = True

        self.find_items()

    def show_ad(self, event):
        """Вызывается, когда нажимают два раза подряд на строчку в таблице, и создает AdBase,
        в котором отображается информация об одежде"""
        global ads
        ads = [ad for ad in ads if not ad.isHidden()]  # Удаляются объявления, которые уже закрыты
        ad_info = self.choice if self.one_item else self.result[event.row()]
        if f"{ad_info[1].capitalize()}({ad_info[0]})" not in [ad.windowTitle() for ad in ads]:
            ads.append(AdBase(ad_info))  # Проверака: нет ли уже таких объявлений
            ads[-1].show()

    def find_items(self):
        """Собирает из таблицы условия и ищет по ним в базе данных подходщую одежду,
        а потом выводит результаты поиска на таблицу"""
        texts = []
        for i in range(self.tableWidget.rowCount()):
            tab = []
            for j in range(self.tableWidget.columnCount() - 1):  # Цикл, формирующий построчное
                widget = self.tableWidget.cellWidget(i, j)  # представление информации
                if widget.__class__ == QComboBox:
                    tab.append(widget.currentText() if j != 2
                               else str([weather, seasons, categories][
                                            ["погода (вручную)", "сезон", "категория"]
                                        .index(self.tableWidget.cellWidget(i, 0)
                                               .currentText())][widget.currentText()]))
                elif widget.__class__ == QDoubleSpinBox:
                    tab.append(widget.text().replace(",", "."))
                else:
                    tab.append(widget.text())
            # Далее формируются условия для базы данных
            if tab[0] not in {"температура (вручную)", "название", "температура (по городам)",
                              "погода (по городам)"}:
                texts.append({"погода (вручную)": "weather", "сезон": "season",
                              "категория": "category", "цена": "cost"}.
                             get(tab[0], tab[0]) + "".join(tab[1:]))
            elif tab[1] in {"=", "!="} and tab[0] == "температура (вручную)":
                texts.append(f"{tab[2]} {'' if tab[1] == '=' else 'NOT'} BETWEEN ft AND tt")
            elif tab[1] in {">", "<"} and tab[0] == "температура (вручную)":
                texts.append(f"{tab[2]} {'< tt' if tab[1] == '>' else '> ft'}")
            elif tab[1] in {"=", "!="} and tab[0] == "температура (по городам)":
                if (temp := tab[2][tab[2].rfind('(') + 1:-1]) != "?":
                    texts.append(f"{temp} {'' if tab[1] == '=' else 'NOT'} BETWEEN ft AND tt")
            elif tab[1] in {"=", "!="} and tab[0] == "погода (по городам)":
                if (weather_city := tab[2][tab[2].rfind('(') + 1:-1]) != "?":
                    texts.append(f"weather={weather[weather_city]}")
            elif tab[1] in {">", "<"}:
                if (temp := tab[2][tab[2].rfind('(') + 1:-1]) != "?":
                    texts.append(f"{temp} {'< tt' if tab[1] == '>' else '> ft'}")
            else:
                texts.append(f"title {'' if tab[1] == '=' else 'NOT'} "
                             f"LIKE '%{tab[2].lower().replace('ё', 'e')}%'")
        self.result = cur.execute(f"SELECT * FROM clothes WHERE "
                                  f"{' AND '.join([inp for inp in texts if inp])}"
                                  if ' AND '.join([inp for inp in texts if inp])
                                  else """SELECT * FROM clothes""").fetchall()
        if self.one_item:
            self.result = list(filter(lambda x: x[6] == self.category, self.result))
        if self.result:
            self.tableWidget_2.setRowCount(1 if self.one_item else len(self.result))
            self.tableWidget_2.setColumnCount(len(self.result[0]) if self.first_look else 2)
        else:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setHorizontalHeaderLabels(["id", "название", "от", "до",
                                                      "погода", "сезон", "категория", "цена",
                                                      "фото"] if self.first_look else
                                                     ["информация", "фото"])
        # Далее размещение полученной одежды по таблице
        if not self.one_item:
            if self.first_look:
                for i, row in enumerate(self.result):
                    for j, elem in enumerate(row):
                        if 4 <= j <= 6:
                            elem = reverse_dictionary([weather, seasons, categories][j - 4])[elem]
                        if j != 8:
                            self.tableWidget_2.removeCellWidget(i, j)
                            self.tableWidget_2.setItem(i, j, QTableWidgetItem(str(elem)))
                        elif elem:
                            self.image = QLabel(self)
                            self.pixmap = QPixmap(elem)
                            if self.pixmap.height():
                                self.image.setPixmap(QPixmap(elem).scaledToHeight(200))
                            self.tableWidget_2.setCellWidget(i, j, self.image)
            else:
                for i, row in enumerate(self.result):
                    self.tableWidget_2.setItem(
                        i, 0, QTableWidgetItem(f"id: {row[0]};\nназвание: {row[1]};\n"
                                               f"для температуры от {row[2]} до {row[3]};\nносить, "
                                               f"когда {reverse_dictionary(weather)[row[4]]}, "
                                               f"{reverse_dictionary(seasons)[row[5]]};\nчасть "
                                               f"тела - {reverse_dictionary(categories)[row[6]]};"
                                               f"\nцена: {row[7]}".lower()))
                    self.image = QLabel(self)
                    self.image.setPixmap(QPixmap(row[8]).scaledToHeight(200))
                    self.tableWidget_2.setCellWidget(i, 1, self.image)

        elif self.result:
            self.choice = choice(self.result)
            for i, elem in enumerate(self.choice[:-1]):
                if 4 <= i <= 6:
                    elem = reverse_dictionary([weather, seasons, categories][i - 4])[elem]
                self.tableWidget_2.setItem(0, i, QTableWidgetItem(str(elem)))
            self.label = QLabel(self.layoutWidget)
            self.label.setPixmap(QPixmap(self.choice[-1]).scaledToHeight(200))
            self.tableWidget_2.setCellWidget(0, 8, self.label)

        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.resizeRowsToContents()

    def add_if(self):
        """Добавление условия, вызывается при нажатии соответствующей кнопки"""
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)

        self.btn = QPushButton(self.window)  # Кнопка для удаления условий
        self.btns.append(self.btn)
        self.btn.setText("-")
        self.btn.clicked.connect(self.delete_if)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 3, self.btn)

        self.combo_box = QComboBox(self.window)  # Первый comboBox
        self.combo_boxes.append(self.combo_box)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 0, self.combo_box)
        self.combo_box.currentTextChanged.connect(self.change_if)
        self.combo_box.addItems(self.statements.keys())

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def change_if(self, event):
        """Изменение одного из условий, вызывается когда значение первого comboBox'а в какой-либо
        из строчек меняется"""
        if event == "id":
            widget = QSpinBox(self.window)
            widget.setButtonSymbols(QAbstractSpinBox.NoButtons)
            widget.setMaximum(999999999)
            if self.always_update:
                widget.valueChanged.connect(self.find_items)
        elif event == "название":
            widget = QLineEdit(self)
            if self.always_update:
                widget.textChanged.connect(self.find_items)
        elif event in ["температура (вручную)", "цена"]:
            widget = QDoubleSpinBox(self.window)
            widget.setButtonSymbols(QAbstractSpinBox.NoButtons)
            widget.setMaximum(999999999)
            widget.setMinimum(-999999999 if event == "температура (вручную)" else 0)
            if self.always_update:
                widget.valueChanged.connect(self.find_items)
        elif event in {"температура (по городам)", "погода (по городам)"}:
            widget = QPushButton(self.window)
            set_text_for_button(widget, cities_id[0], event == "температура (по городам)")
            widget.clicked.connect(self.add_select_city_temp_class
                                   if event == "температура (по городам)"
                                   else self.add_select_city_weather_class)
        else:
            widget = QComboBox(self.window)
            widget.addItems(self.for_compare[event])
            if self.always_update:
                widget.currentTextChanged.connect(self.find_items)
        self.tableWidget.setCellWidget(self.combo_boxes.index(self.sender()), 2, widget)
        self.variants = self.tableWidget.cellWidget(self.combo_boxes.index(self.sender()), 1)
        if self.variants:
            self.variants.blockSignals(True)
            self.variants.clear()
            # Метод также вызывается при создании первого comboBox'а, когда еще нет третьего
            # и тогда self.variants равен None, для того здесь и проверка
        else:
            self.variants = QComboBox(self.window)
            if self.always_update:
                self.variants.currentTextChanged.connect(self.find_items)
            self.tableWidget.setCellWidget(self.combo_boxes.index(self.sender()), 1, self.variants)
        self.variants.blockSignals(False)
        self.variants.addItems(self.statements[event])

        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnsToContents()

    def delete_if(self):
        """Вызывается когда нажимается кнопка для удаления условий"""
        index = self.btns.index(self.sender())
        self.combo_boxes.pop(index)
        self.btns.pop(index)
        self.tableWidget.removeRow(index)

        if self.always_update:
            self.find_items()

    def add_select_city_temp_class(self):
        """Вызывает окно с выбором города для выставления температуры"""
        self.select_temp_city = SelectCity(self.sender(), self.tableWidget,
                                           (self.find_items if self.always_update else None))
        self.select_temp_city.show()

    def add_select_city_weather_class(self):
        """Вызывает окно с выбором города для выставления погоды"""
        self.select_weather_city = SelectCity(self.sender(), self.tableWidget,
                                              (self.find_items if self.always_update else None),
                                              False)
        self.select_weather_city.show()


class ShowData(QMainWindow, UiForm):
    def __init__(self):
        """Отображает саму базу данных, возможно по некоторым критериям"""
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton_2.clicked.connect(self.delete_line)
        self.pushButton_3.clicked.connect(self.add_line)
        self.pushButton_4.clicked.connect(self.change_line)
        self.commandLinkButton.clicked.connect(self.change_window)
        self.radioButton.toggled.connect(self.change_look)

        self.setWindowTitle("Таблица")
        self.setGeometry(300, 300, 500, 500)
        self.setCentralWidget(self.gridLayoutWidget)

        self.table_class = FindWidget([[2, 0, 1, 1], [3, 0, 1, 1], [3, 1, 1, 1]],
                                      self.gridLayoutWidget, self,
                                      {"id": ["=", ">", "<", "!="], "название": ["=", "!="],
                                       "температура (вручную)": ["=", ">", "<", "!="],
                                       "погода (вручную)": ["=", "!="],
                                       "сезон": ["=", "!="], "категория": ["=", "!="],
                                       "цена": ["=", ">", "<", "!="],
                                       "температура (по городам)": ["=", ">", "<", "!="],
                                       "погода (по городам)": ["=", "!="]},
                                      {"погода (вручную)": get_titles("weather"),
                                       "сезон": get_titles("seasons"),
                                       "категория": get_titles("categories")})
        tables.append(self.table_class)

    def change_line(self):
        """Меняет одну из выделенных строк"""
        selected = self.table_class.tableWidget_2.selectedIndexes()
        if selected:
            selected = self.table_class.result[selected[-1].row()]
            self.do_line = DoSmtWithLine(False, selected[1:], selected[0])
            self.do_line.show()

    def delete_line(self):
        """Удаляет выделенные строки из таблицы с одеждой"""
        need_rows = tuple({self.table_class.result[index.row()][0] for index in
                           self.table_class.tableWidget_2.selectedIndexes()})
        if need_rows:
            need_rows = f"({need_rows[0]})" if len(need_rows) == 1 else need_rows
            cur.execute(f"DELETE FROM clothes WHERE id IN {need_rows}")
            con.commit()
            # Может надо менять id при удалении строк, а может и нет
            self.table_class.find_items()

    def add_line(self):
        """Добавляет строку в таблицу с одеждой"""
        self.do_line = DoSmtWithLine()
        self.do_line.show()

    def change_window(self):
        """Скрывает ShowData и показывает RandomClothes"""
        win2.show()
        win.hide()

    def change_look(self, event):
        """Меняет способ заполнения таблицы у FindWidget, созданного в этом классе"""
        self.table_class.first_look = event

        self.table_class.find_items()


class RandomClothes(QMainWindow, RandomClothesForm):
    def __init__(self):
        """Показывает случайную подборку одежды по каждой категории"""
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Случайный выбор")

        self.table_classes = []
        self.check_boxes = {}

        self.pushButton.clicked.connect(self.update_tables)
        self.commandLinkButton.clicked.connect(self.change_window)

        self.setCentralWidget(self.gridLayoutWidget)

        for i, category in enumerate(cur.execute("SELECT title FROM categories").fetchall(), 2):
            check_box = QCheckBox(self.gridLayoutWidget)
            check_box.setText(category[0])
            check_box.setChecked(True)
            check_box.clicked.connect(self.hide_or_show_table)
            self.gridLayout.addWidget(check_box, i, 0)
            self.table_classes.append(table_class := FindWidget([[i, 1], [i, 2], [i, 3]],
                                                                self.gridLayoutWidget, self,
                                                                {"id": ["=", ">", "<", "!="],
                                                                 "название": ["=", "!="],
                                                                 "температура (вручную)":
                                                                     ["=", ">", "<", "!="],
                                                                 "погода (вручную)": ["=", "!="],
                                                                 "сезон": ["=", "!="],
                                                                 "цена": ["=", ">", "<", "!="],
                                                                 "температура (по городам)":
                                                                     ["=", ">", "<", "!="],
                                                                 "погода (по городам)": ["=", "!="]},
                                                                {"погода (вручную)":
                                                                     get_titles("weather"),
                                                                 "сезон": get_titles("seasons")},
                                                                False, True, i - 1))
            self.check_boxes[check_box] = [table_class.pushButton, table_class.tableWidget,
                                           table_class.tableWidget_2]
        tables.extend(self.table_classes)

    def change_window(self):
        """Скрывает RandomClothes и показывает ShowData"""
        win.show()
        win2.hide()

    def hide_or_show_table(self, event):
        """Прячет все виджеты определенного FindWidget'а,
        вызывается когда нажимается любой checkBox"""
        [widget.setEnabled(event) for widget in self.check_boxes[self.sender()]]

    def update_tables(self):
        """Вызывает метод find_items у каждого FindWidget, созданного в этом классе,
        вызывается когда нажимается кнопка для поиска подходящей одежды"""
        [table_class.find_items() for table_class in self.table_classes
         if table_class.pushButton.isEnabled()]


def get_titles(table_name):
    """Возвращает названия из определенной таблицы"""
    return [elem[0] for elem in cur.execute(f"SELECT title FROM {table_name}").fetchall()]


def get_dictionary(table_name):
    """Возвращает словарь, составленный по таблицы из базы данных"""
    dictionary = {}
    for elem in cur.execute(f"SELECT * FROM {table_name}").fetchall():
        dictionary[elem[1]] = elem[0]
    return dictionary


def reverse_dictionary(dictionary):
    """Возвращает 'перевернутый' словарь"""
    reversed_dictionary = {}
    for key in dictionary:
        reversed_dictionary[dictionary[key]] = key
    return reversed_dictionary


def set_text_for_button(btn, city, temp_mode):
    """Ставит текст кнопки равный температуре или погоде в указанном городе"""
    try:  # На всякий случай, вдруг такого id не будет
        req = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city[city.find("(") + 1:city.rfind(")")],
                                   'units': 'metric',
                                   'lang': 'ru',
                                   'APPID': "f398d06879170fa356797b66887022db"}).json()
        if temp_mode:
            btn.setText(f"{city}({req['main']['temp']})")
        elif (weather_id := str(req["weather"][0]["id"])) in {"202", "232", "302", "312",
                                                              "313", "314", "502", "503",
                                                              "504", "520", "521", "522",
                                                              "531"}:
            btn.setText(f"{city}(Ливень)")
        elif weather_id in {"200", "201", "230", "231", "300", "301", "310", "311", "321",
                            "500", "501", "511"}:
            btn.setText(f"{city}(Дождь)")
        elif weather_id[0] == "6":
            btn.setText(f"{city}(Снег)")
        elif weather_id[0] == "8":
            btn.setText(f"{city}(Ясно)")
        else:
            raise KeyError
    except KeyError:
        btn.setText(f"{city}(?)")


con = sqlite3.connect("clothes.sqlite")
cur = con.cursor()

categories = get_dictionary("categories")
weather = get_dictionary("weather")
seasons = get_dictionary("seasons")

ads = []
tables = []

cities_id = [line[0] for line in
             csv.reader(open("cities.txt", "r", encoding="utf-8"), delimiter="\n")]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ShowData()
    win2 = RandomClothes()
    win.show()
    sys.exit(app.exec())
