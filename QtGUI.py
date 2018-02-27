import sys
from PyQt5 import QtWidgets, QtGui


class AppMainWindow(QtWidgets.QApplication):

    def __init__(self):
        super(AppMainWindow,self).__init__([])
        self.mainWidget = QtWidgets.QWidget()

        self.initUi()

    def initUi(self):
        self.mainWidget.setGeometry(20, 20, 500, 500)
        self.mainWidget.setWindowTitle("Fuzzy Map Analyser")
        self.mainWidget.setWindowIcon(QtGui.QIcon('Resources/network.png'))

    def run(self):
        self.mainWidget.show()

        sys.exit(self.exec_())
