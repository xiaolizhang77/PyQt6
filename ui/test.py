# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.PyQt6Button = QtWidgets.QPushButton(parent=Form)
        self.PyQt6Button.setGeometry(QtCore.QRect(54, 80, 141, 111))
        self.PyQt6Button.setObjectName("PyQt6Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.PyQt6Button.setText(_translate("Form", "PyQt6Button"))
