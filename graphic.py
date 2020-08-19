
import sys
import random
from PyQt5 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #background
        self.setStyleSheet("background-color:rgb(58, 58, 60);")

        # TODO menu
        
        #buttons
        self.button = QtWidgets.QPushButton("click here")
        self.button.setStyleSheet("background-color:rgb(142, 142, 147);")


        self.text = QtWidgets.QLabel("Hello world")
        self.text.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())


