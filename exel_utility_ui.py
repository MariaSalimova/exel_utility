# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exel_utility_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(319, 151)
        self.file_path_lineEdit = QtWidgets.QLineEdit(Form)
        self.file_path_lineEdit.setGeometry(QtCore.QRect(20, 30, 281, 22))
        self.file_path_lineEdit.setObjectName("file_path_lineEdit")
        self.new_file_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.new_file_name_lineEdit.setGeometry(QtCore.QRect(20, 80, 281, 22))
        self.new_file_name_lineEdit.setObjectName("new_file_name_lineEdit")
        self.file_path_label = QtWidgets.QLabel(Form)
        self.file_path_label.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.file_path_label.setObjectName("file_path_label")
        self.new_file_name_label = QtWidgets.QLabel(Form)
        self.new_file_name_label.setGeometry(QtCore.QRect(20, 60, 141, 16))
        self.new_file_name_label.setObjectName("new_file_name_label")
        self.do_it_button = QtWidgets.QPushButton(Form)
        self.do_it_button.setGeometry(QtCore.QRect(20, 110, 281, 28))
        self.do_it_button.setObjectName("do_it_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Exel utility"))
        self.file_path_label.setText(_translate("Form", "Путь к файлу"))
        self.new_file_name_label.setText(_translate("Form", "Имя нового файла"))
        self.do_it_button.setText(_translate("Form", "Обработать"))
