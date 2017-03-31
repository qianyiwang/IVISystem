from PyQt4 import QtGui, QtCore
import GlobalValues

class AudioUI(QtGui.QWidget):
    def __init__(self, controller, parent=None):
        super(AudioUI, self).__init__(parent)
        
        self.controller = controller

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
        self.homeBt.setPixmap(GlobalValues.home_icon)
        self.homeBt.mouseReleaseEvent = self.homeBtRelease

        self.timeInfo = QtGui.QLabel('8:00')
        topLayout.addWidget(self.homeBt)
        topLayout.setStretch(0,3)
        topLayout.addWidget(self.timeInfo)
        topLayout.setStretch(1,4)

        # design bottom tool bar
        self.bottomBar = QtGui.QLabel(self)
        self.bottomBar.setStyleSheet("background-color:lightgray;")
        bottomLayout = QtGui.QHBoxLayout(self.bottomBar) # add horizontal layout on bottom bar

        self.audioBt = QtGui.QLabel(self)
        self.audioBt.setPixmap(GlobalValues.audio_icon)
        self.audioBt.setAlignment(QtCore.Qt.AlignCenter)
        self.audioBt.setStyleSheet("background-color:lightblue;")
        self.audioBt.mousePressEvent = self.audioBtPress
        self.audioBt.mouseReleaseEvent = self.audioBtRelease

        self.climateBt = QtGui.QLabel(self)
        self.climateBt.setPixmap(GlobalValues.climate_icon)
        self.climateBt.setAlignment(QtCore.Qt.AlignCenter)
        self.climateBt.mousePressEvent = self.climateBtPress
        self.climateBt.mouseReleaseEvent = self.climateBtRelease

        self.phoneBt = QtGui.QLabel(self)
        self.phoneBt.setPixmap(GlobalValues.phone_icon)
        self.phoneBt.setAlignment(QtCore.Qt.AlignCenter)
        self.phoneBt.mousePressEvent = self.phoneBtPress
        self.phoneBt.mouseReleaseEvent = self.phoneBtRelease

        self.appsBt = QtGui.QLabel(self)
        self.appsBt.setPixmap(GlobalValues.apps_icon)
        self.appsBt.setAlignment(QtCore.Qt.AlignCenter)
        self.appsBt.mousePressEvent = self.appsBtPress
        self.appsBt.mouseReleaseEvent = self.appsBtRelease

        self.settingBt = QtGui.QLabel(self)
        self.settingBt.setPixmap(GlobalValues.setting_icon)
        self.settingBt.setAlignment(QtCore.Qt.AlignCenter)
        self.settingBt.mousePressEvent = self.settingBtPress
        self.settingBt.mouseReleaseEvent = self.settingBtRelease
        
        bottomLayout.addWidget(self.audioBt)
        bottomLayout.setStretch(0,1)
        bottomLayout.addWidget(self.climateBt)
        bottomLayout.setStretch(1,1)
        bottomLayout.addWidget(self.phoneBt)
        bottomLayout.setStretch(2,1)
        bottomLayout.addWidget(self.appsBt)
        bottomLayout.setStretch(3,1)
        bottomLayout.addWidget(self.settingBt)
        bottomLayout.setStretch(4,1)


        # design middle content
        middle_box = QtGui.QGridLayout()
        middle_box.setContentsMargins(15, 10, 15, 10)

        # declear the audio info variable


        # layout.addStretch(1)
        layout.addWidget(self.titleBar)
        layout.setStretch(0,2)
        layout.addLayout(middle_box)
        layout.setStretch(1,10)
        layout.addWidget(self.bottomBar)
        layout.setStretch(2,3)
        self.setLayout(layout)

    def homeBtRelease(self, event): # go to homeUI
        self.controller.central_widget.setCurrentWidget(self.controller.homeUI)

    def audioBtPress(self, event):
        self.audioBt.setStyleSheet("background-color:lightgray;")

    def audioBtRelease(self, event):
        self.audioBt.setStyleSheet("background-color:lightgray;")

    def climateBtPress(self, event):
        self.climateBt.setStyleSheet("background-color:lightblue;")

    def climateBtRelease(self, event):
        self.climateBt.setStyleSheet("background-color:lightgray;")

    def phoneBtPress(self, event):
        self.phoneBt.setStyleSheet("background-color:lightblue;")

    def phoneBtRelease(self, event):
        self.phoneBt.setStyleSheet("background-color:lightgray;")

    def appsBtPress(self, event):
        self.appsBt.setStyleSheet("background-color:lightblue;")

    def appsBtRelease(self, event):
        self.appsBt.setStyleSheet("background-color:lightgray;")

    def settingBtPress(self, event):
        self.settingBt.setStyleSheet("background-color:lightblue;")

    def settingBtRelease(self, event):
        self.settingBt.setStyleSheet("background-color:lightgray;")