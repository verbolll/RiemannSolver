# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Riemann(object):
    def setupUi(self, Riemann):
        if not Riemann.objectName():
            Riemann.setObjectName(u"Riemann")
        Riemann.resize(630, 416)
        self.horizontalLayout_5 = QHBoxLayout(Riemann)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget = QWidget(Riemann)
        self.widget.setObjectName(u"widget")

        self.verticalLayout_11.addWidget(self.widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.p1_lab = QLabel(Riemann)
        self.p1_lab.setObjectName(u"p1_lab")
        self.p1_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.p1_lab)

        self.p1_edt = QLineEdit(Riemann)
        self.p1_edt.setObjectName(u"p1_edt")
        self.p1_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.p1_edt)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.p2_lab = QLabel(Riemann)
        self.p2_lab.setObjectName(u"p2_lab")
        self.p2_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.p2_lab)

        self.p2_edt = QLineEdit(Riemann)
        self.p2_edt.setObjectName(u"p2_edt")
        self.p2_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.p2_edt)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.u1_lab = QLabel(Riemann)
        self.u1_lab.setObjectName(u"u1_lab")
        self.u1_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.u1_lab)

        self.u1_edt = QLineEdit(Riemann)
        self.u1_edt.setObjectName(u"u1_edt")
        self.u1_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.u1_edt)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.u2_lab = QLabel(Riemann)
        self.u2_lab.setObjectName(u"u2_lab")
        self.u2_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.u2_lab)

        self.u2_edt = QLineEdit(Riemann)
        self.u2_edt.setObjectName(u"u2_edt")
        self.u2_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.u2_edt)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.rho1_lab = QLabel(Riemann)
        self.rho1_lab.setObjectName(u"rho1_lab")
        self.rho1_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.rho1_lab)

        self.rho1_edt = QLineEdit(Riemann)
        self.rho1_edt.setObjectName(u"rho1_edt")
        self.rho1_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.rho1_edt)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rho2_lab = QLabel(Riemann)
        self.rho2_lab.setObjectName(u"rho2_lab")
        self.rho2_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.rho2_lab)

        self.rho2_edt = QLineEdit(Riemann)
        self.rho2_edt.setObjectName(u"rho2_edt")
        self.rho2_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.rho2_edt)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.t_lab = QLabel(Riemann)
        self.t_lab.setObjectName(u"t_lab")
        self.t_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.t_lab)

        self.t_edt = QLineEdit(Riemann)
        self.t_edt.setObjectName(u"t_edt")
        self.t_edt.setEnabled(True)
        self.t_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.t_edt)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.pushButton = QPushButton(Riemann)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_11.addWidget(self.pushButton)

        self.radioButton = QRadioButton(Riemann)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_11.addWidget(self.radioButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.t1_lab = QLabel(Riemann)
        self.t1_lab.setObjectName(u"t1_lab")
        self.t1_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.t1_lab)

        self.t1_edt = QLineEdit(Riemann)
        self.t1_edt.setObjectName(u"t1_edt")
        self.t1_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.t1_edt)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.t2_lab = QLabel(Riemann)
        self.t2_lab.setObjectName(u"t2_lab")
        self.t2_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.t2_lab)

        self.t2_edt = QLineEdit(Riemann)
        self.t2_edt.setObjectName(u"t2_edt")
        self.t2_edt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.t2_edt)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.widget_2 = QWidget(Riemann)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_11.addWidget(self.widget_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout_11)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pic_lab = QLabel(Riemann)
        self.pic_lab.setObjectName(u"pic_lab")
        self.pic_lab.setMinimumSize(QSize(500, 375))
        self.pic_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.pic_lab)

        self.tittle_lab = QLabel(Riemann)
        self.tittle_lab.setObjectName(u"tittle_lab")
        self.tittle_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.tittle_lab)


        self.horizontalLayout_5.addLayout(self.verticalLayout_10)


        self.retranslateUi(Riemann)

        QMetaObject.connectSlotsByName(Riemann)
    # setupUi

    def retranslateUi(self, Riemann):
        Riemann.setWindowTitle(QCoreApplication.translate("Riemann", u"Riemann", None))
        self.p1_lab.setText(QCoreApplication.translate("Riemann", u"p1", None))
        self.p2_lab.setText(QCoreApplication.translate("Riemann", u"p2", None))
        self.u1_lab.setText(QCoreApplication.translate("Riemann", u"u1", None))
        self.u2_lab.setText(QCoreApplication.translate("Riemann", u"u2", None))
        self.rho1_lab.setText(QCoreApplication.translate("Riemann", u"rho1", None))
        self.rho2_lab.setText(QCoreApplication.translate("Riemann", u"rho2", None))
        self.t_lab.setText(QCoreApplication.translate("Riemann", u"t", None))
        self.pushButton.setText(QCoreApplication.translate("Riemann", u"calculate", None))
        self.radioButton.setText(QCoreApplication.translate("Riemann", u"make video", None))
        self.t1_lab.setText(QCoreApplication.translate("Riemann", u"t1", None))
        self.t2_lab.setText(QCoreApplication.translate("Riemann", u"t2", None))
        self.pic_lab.setText("")
        self.tittle_lab.setText("")
    # retranslateUi

