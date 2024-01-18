# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QTabWidget, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(840, 270)
        MainWindow.setMinimumSize(QSize(840, 270))
        MainWindow.setMaximumSize(QSize(840, 270))
        self.actionImport_Modules = QAction(MainWindow)
        self.actionImport_Modules.setObjectName(u"actionImport_Modules")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 811, 221))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.logBrowser = QTextBrowser(self.tab)
        self.logBrowser.setObjectName(u"logBrowser")
        self.logBrowser.setGeometry(QRect(15, 11, 781, 171))
        self.tabWidget.addTab(self.tab, "")
        self.Records_Check = QWidget()
        self.Records_Check.setObjectName(u"Records_Check")
        self.pushButton = QPushButton(self.Records_Check)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(174, 10, 91, 24))
        self.lineEdit = QLineEdit(self.Records_Check)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 10, 151, 22))
        self.domainLabel = QLabel(self.Records_Check)
        self.domainLabel.setObjectName(u"domainLabel")
        self.domainLabel.setGeometry(QRect(10, 40, 161, 21))
        self.label = QLabel(self.Records_Check)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 161, 21))
        self.label_2 = QLabel(self.Records_Check)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 161, 20))
        self.label_3 = QLabel(self.Records_Check)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 100, 161, 20))
        self.domainLabelResult = QLabel(self.Records_Check)
        self.domainLabelResult.setObjectName(u"domainLabelResult")
        self.domainLabelResult.setGeometry(QRect(190, 40, 611, 21))
        self.spfLabelResult = QLabel(self.Records_Check)
        self.spfLabelResult.setObjectName(u"spfLabelResult")
        self.spfLabelResult.setGeometry(QRect(190, 60, 611, 21))
        self.DKIMLabelResult_1 = QLabel(self.Records_Check)
        self.DKIMLabelResult_1.setObjectName(u"DKIMLabelResult_1")
        self.DKIMLabelResult_1.setGeometry(QRect(190, 80, 611, 21))
        self.DKIMLabelResult_2 = QLabel(self.Records_Check)
        self.DKIMLabelResult_2.setObjectName(u"DKIMLabelResult_2")
        self.DKIMLabelResult_2.setGeometry(QRect(190, 100, 611, 21))
        self.tabWidget.addTab(self.Records_Check, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 840, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.actionImport_Modules)
        self.menuSettings.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionImport_Modules.setText(QCoreApplication.translate("MainWindow", u"Import Modules", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Log", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Check Records", None))
        self.domainLabel.setText(QCoreApplication.translate("MainWindow", u"Domain: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contains spfva.gofax.com.au: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Contains DKIM Key 1: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contains DKIM Key 2: ", None))
        self.domainLabelResult.setText(QCoreApplication.translate("MainWindow", u"domain", None))
        self.spfLabelResult.setText(QCoreApplication.translate("MainWindow", u"SPF", None))
        self.DKIMLabelResult_1.setText(QCoreApplication.translate("MainWindow", u"DKIM Key 1", None))
        self.DKIMLabelResult_2.setText(QCoreApplication.translate("MainWindow", u"DKIM Key 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Records_Check), QCoreApplication.translate("MainWindow", u"Records Check", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

