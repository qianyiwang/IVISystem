import sys
from PyQt4 import QtGui
from HomeUI import HomeUI
from AudioUI import AudioUI
import GlobalValues
import AudioControl

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # design root window
        self.setWindowTitle('IVI')
        self.setGeometry(400,400,800,450)

        # declear stack and add HomeUI into stack to show
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.homeUI = HomeUI(self)
        self.audioUI = AudioUI(self)
        self.central_widget.addWidget(self.homeUI) # first add UI on the top
        self.central_widget.addWidget(self.audioUI)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    GlobalValues.init()
    audio = AudioControl.AudioControl()
    window = MainWindow()
    window.show()
    app.exec_()