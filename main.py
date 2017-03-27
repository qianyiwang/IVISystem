import sys
from PyQt4 import QtGui
from HomeUI import HomeUI

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # design root window
        self.setWindowTitle('IVI')
        self.setGeometry(400,400,800,450)

        # declear stack and add HomeUI into stack to show
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        homeUI = HomeUI(self)
        self.central_widget.addWidget(homeUI)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()