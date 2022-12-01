# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextBrowser,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(419, 371)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_chrome_driver = QLabel(self.centralwidget)
        self.label_chrome_driver.setObjectName(u"label_chrome_driver")

        self.horizontalLayout.addWidget(self.label_chrome_driver)

        self.label_select_chrome_driver = QLabel(self.centralwidget)
        self.label_select_chrome_driver.setObjectName(u"label_select_chrome_driver")

        self.horizontalLayout.addWidget(self.label_select_chrome_driver)

        self.pushButton_select_chrome_driver = QPushButton(self.centralwidget)
        self.pushButton_select_chrome_driver.setObjectName(u"pushButton_select_chrome_driver")

        self.horizontalLayout.addWidget(self.pushButton_select_chrome_driver)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")

        self.horizontalLayout_2.addWidget(self.label_info)

        self.label___ = QLabel(self.centralwidget)
        self.label___.setObjectName(u"label___")
        self.label___.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label___)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.checkBox_auto = QCheckBox(self.centralwidget)
        self.checkBox_auto.setObjectName(u"checkBox_auto")

        self.horizontalLayout_2.addWidget(self.checkBox_auto)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.textEdit_translation_before = QTextEdit(self.centralwidget)
        self.textEdit_translation_before.setObjectName(u"textEdit_translation_before")

        self.verticalLayout.addWidget(self.textEdit_translation_before)

        self.pushButton_translation = QPushButton(self.centralwidget)
        self.pushButton_translation.setObjectName(u"pushButton_translation")

        self.verticalLayout.addWidget(self.pushButton_translation)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.textBrowser_papago = QTextBrowser(self.centralwidget)
        self.textBrowser_papago.setObjectName(u"textBrowser_papago")
        self.textBrowser_papago.setEnabled(True)

        self.verticalLayout_2.addWidget(self.textBrowser_papago)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.textBrowser_google = QTextBrowser(self.centralwidget)
        self.textBrowser_google.setObjectName(u"textBrowser_google")
        self.textBrowser_google.setEnabled(True)

        self.verticalLayout_3.addWidget(self.textBrowser_google)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 419, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uba40\ud2f0 \ubc88\uc5ed\uae30", None))
        self.label_chrome_driver.setText(QCoreApplication.translate("MainWindow", u"\ud06c\ub86c \ub4dc\ub77c\uc774\ubc84 : ", None))
        self.label_select_chrome_driver.setText("")
        self.pushButton_select_chrome_driver.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \uc120\ud0dd", None))
        self.label_info.setText(QCoreApplication.translate("MainWindow", u"\ubc88\uc5ed\ud560 \ub0b4\uc6a9 \uc785\ub825(\uc5b8\uc5b4 \uac10\uc9c0)", None))
        self.label___.setText(QCoreApplication.translate("MainWindow", u"-- >", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud55c\uad6d\uc5b4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc601\uc5b4", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc77c\ubcf8\uc5b4", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc911\uad6d\uc5b4(\uac04\uccb4)", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc911\uad6d\uc5b4(\ubc88\uccb4)", None))

        self.checkBox_auto.setText(QCoreApplication.translate("MainWindow", u"\ubcf5\uc0ac\uc790\ub3d9\uc785\ub825", None))
        self.pushButton_translation.setText(QCoreApplication.translate("MainWindow", u"\ubc88\uc5ed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud30c\ud30c\uace0 \ubc88\uc5ed", None))
        self.textBrowser_papago.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uad6c\uae00 \ubc88\uc5ed", None))
        self.textBrowser_google.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

