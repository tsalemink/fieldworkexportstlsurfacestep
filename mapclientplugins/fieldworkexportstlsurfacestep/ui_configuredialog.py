# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(482, 246)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(Dialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.idLabel = QLabel(self.configGroupBox)
        self.idLabel.setObjectName(u"idLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.idLabel)

        self.idLineEdit = QLineEdit(self.configGroupBox)
        self.idLineEdit.setObjectName(u"idLineEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.idLineEdit)

        self.fileLocLabel = QLabel(self.configGroupBox)
        self.fileLocLabel.setObjectName(u"fileLocLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.fileLocLabel)

        self.discLabel = QLabel(self.configGroupBox)
        self.discLabel.setObjectName(u"discLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.discLabel)

        self.discLineEdit = QLineEdit(self.configGroupBox)
        self.discLineEdit.setObjectName(u"discLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.discLineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileLocLineEdit = QLineEdit(self.configGroupBox)
        self.fileLocLineEdit.setObjectName(u"fileLocLineEdit")

        self.horizontalLayout.addWidget(self.fileLocLineEdit)

        self.fileLocButton = QPushButton(self.configGroupBox)
        self.fileLocButton.setObjectName(u"fileLocButton")

        self.horizontalLayout.addWidget(self.fileLocButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        QWidget.setTabOrder(self.idLineEdit, self.fileLocLineEdit)
        QWidget.setTabOrder(self.fileLocLineEdit, self.fileLocButton)
        QWidget.setTabOrder(self.fileLocButton, self.discLineEdit)
        QWidget.setTabOrder(self.discLineEdit, self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure Export STL Surface Step", None))
        self.configGroupBox.setTitle("")
        self.idLabel.setText(QCoreApplication.translate("Dialog", u"Identifier:  ", None))
        self.fileLocLabel.setText(QCoreApplication.translate("Dialog", u"Filename:  ", None))
        self.discLabel.setText(QCoreApplication.translate("Dialog", u"Discretisation:", None))
        self.fileLocButton.setText(QCoreApplication.translate("Dialog", u"...", None))
    # retranslateUi

