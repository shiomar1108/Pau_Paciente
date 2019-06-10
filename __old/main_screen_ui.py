# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_screen_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Alimente(object):
    def setupUi(self, Alimente):
        Alimente.setObjectName("Alimente")
        Alimente.resize(838, 640)
        self.layout = QtWidgets.QWidget(Alimente)
        self.layout.setObjectName("layout")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(self.layout)
        self.logo.setEnabled(True)
        self.logo.setMaximumSize(QtCore.QSize(820, 515))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)
        self.welcome = QtWidgets.QLabel(self.layout)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.welcome.setFont(font)
        self.welcome.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.welcome.setObjectName("welcome")
        self.verticalLayout.addWidget(self.welcome, 0, QtCore.Qt.AlignHCenter)
        self.newpatient_btn = QtWidgets.QPushButton(self.layout)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.newpatient_btn.setFont(font)
        self.newpatient_btn.setObjectName("newpatient_btn")
        self.verticalLayout.addWidget(self.newpatient_btn)
        self.oldpatient_btn = QtWidgets.QPushButton(self.layout)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.oldpatient_btn.setFont(font)
        self.oldpatient_btn.setObjectName("oldpatient_btn")
        self.verticalLayout.addWidget(self.oldpatient_btn)
        self.report_btn = QtWidgets.QPushButton(self.layout)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.report_btn.setFont(font)
        self.report_btn.setObjectName("report_btn")
        self.verticalLayout.addWidget(self.report_btn)
        Alimente.setCentralWidget(self.layout)

        self.retranslateUi(Alimente)
        QtCore.QMetaObject.connectSlotsByName(Alimente)

    def retranslateUi(self, Alimente):
        _translate = QtCore.QCoreApplication.translate
        Alimente.setWindowTitle(_translate("Alimente", "Alimente"))
        self.welcome.setText(_translate("Alimente", "Bienvenida Dr. Paulina"))
        self.newpatient_btn.setText(_translate("Alimente", "Nuevo Paciente"))
        self.oldpatient_btn.setText(_translate("Alimente", "Paciente Existente"))
        self.report_btn.setText(_translate("Alimente", "Crear Reporte"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Alimente = QtWidgets.QMainWindow()
    ui = Ui_Alimente()
    ui.setupUi(Alimente)
    Alimente.show()
    sys.exit(app.exec_())

