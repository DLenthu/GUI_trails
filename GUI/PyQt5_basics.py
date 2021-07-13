from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("PYQT5")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My first Label")
        self.label.move(50,50)

        self.bl = QtWidgets.QPushButton(self)
        self.bl.setText("Click Me")
        self.bl.clicked.connect(self.clicked)       

    def clicked(self):
        self.label.setText("You clicked a button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()