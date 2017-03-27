import sys
from PyQt4 import QtGui

class HomeUI(QtGui.QWidget):
    def __init__(self, parent=None):
        super(HomeUI, self).__init__(parent)
        background_label = QtGui.QLabel(self)
        background_label.setStyleSheet("background-image: url(images/background.jpg);")
        background_label.resize(800,450)
        layout = QtGui.QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # design top bar
        self.titleBar = QtGui.QLabel(self)
        self.titleBar.setStyleSheet("background-color:black;")
        topLayout = QtGui.QHBoxLayout(self.titleBar) # add layout onto a widget
        self.homeBt = QtGui.QLabel()
        self.homeBt.setPixmap(QtGui.QPixmap('images/home_icon.png'))
        self.timeInfo = QtGui.QLabel('8:00')
        topLayout.addWidget(self.homeBt)
        topLayout.setStretch(0,3)
        topLayout.addWidget(self.timeInfo)
        topLayout.setStretch(1,4)

        # design bottom tool bar
        self.bottomBar = QtGui.QLabel(self)
        self.bottomBar.setStyleSheet("background-color:lightgray;")

        # design middle content
        middle_box = QtGui.QGridLayout()
        middle_box.setContentsMargins(15, 10, 15, 10)
        self.button_left = QtGui.QPushButton()
        self.button_left.setStyleSheet("background-color:lightgray;")
        self.button_left.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        self.button_rightTop = QtGui.QPushButton()
        self.button_rightTop.setStyleSheet("background-color:lightgray;")
        self.button_rightTop.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        self.button_rightBottom = QtGui.QPushButton()
        self.button_rightBottom.setStyleSheet("background-color:lightgray;")
        self.button_rightBottom.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)

        middle_box.addWidget(self.button_left, 0, 0, 2, 1)
        middle_box.addWidget(self.button_rightTop, 0, 1, 1, 1)
        middle_box.addWidget(self.button_rightBottom, 1, 1, 1, 1)

        # layout.addStretch(1)
        layout.addWidget(self.titleBar)
        layout.setStretch(0,2)
        layout.addLayout(middle_box)
        layout.setStretch(1,10)
        layout.addWidget(self.bottomBar)
        layout.setStretch(2,3)
        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login) here