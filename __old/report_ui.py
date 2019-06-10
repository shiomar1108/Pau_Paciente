# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(874, 640)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.patient_list = QtWidgets.QListWidget(Form)
        self.patient_list.setObjectName("patient_list")
        self.gridLayout.addWidget(self.patient_list, 2, 1, 1, 1)
        self.title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 1, 1, 2)
        self.generate_btn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.generate_btn.setFont(font)
        self.generate_btn.setObjectName("generate_btn")
        self.gridLayout.addWidget(self.generate_btn, 2, 2, 1, 1, QtCore.Qt.AlignVCenter)
        self.back_btn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")
        self.gridLayout.addWidget(self.back_btn, 1, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Generar reporte de Paciente"))
        self.generate_btn.setText(_translate("Form", "Generar Reporte"))
        self.back_btn.setText(_translate("Form", "Regresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

