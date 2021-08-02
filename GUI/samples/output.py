# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SPLASH.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setStyleSheet("QFrame{\n"
"background-color:rgb(46, 52, 54);\n"
"color: rgb(238, 238, 236);\n"
"border-radius:10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label = QtWidgets.QLabel(self.dropShadowFrame)
        self.label.setGeometry(QtCore.QRect(0, 90, 661, 111))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(238, 238, 236);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_2.setGeometry(QtCore.QRect(0, 180, 661, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(238, 238, 236);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(40, 270, 571, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"        background-color: rgb(74, 67, 93);\n"
"        color:rgb(138, 226, 52);\n"
"        border-style: none;\n"
"        norder-radius: 10px;\n"
"        text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0.0248756, y1:0.722, x2:0.851, y2:0.778, stop:0 rgba(238, 238, 236, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    background-color: \n"
"}\n"
"\n"
"color: rgb(0, 0, 0);")
        self.progressBar.setProperty("value", 50)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_3.setGeometry(QtCore.QRect(0, 310, 661, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(166, 158, 158)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_4.setGeometry(QtCore.QRect(-20, 360, 661, 20))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(166, 158, 158)")
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<strong>TiVRA</strong> AI"))
        self.label_2.setText(_translate("MainWindow", "Data Annotation Tool"))
        self.label_3.setText(_translate("MainWindow", "Loading..."))
        self.label_4.setText(_translate("MainWindow", "<strong>Created:</strong> Ayushman Kumar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
