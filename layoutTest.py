import sys
from PyQt4 import QtGui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    Q = QtGui.QWidget()

    H = QtGui.QHBoxLayout()
    H.addWidget(QtGui.QTextBrowser())
    H.setStretch(0,2)
    H.addWidget(QtGui.QTextBrowser())
    H.setStretch(1,3)

    Q.setLayout(H)

    Q.show()

    app.exec_()