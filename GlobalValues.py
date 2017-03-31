from PyQt4 import QtGui

def init():
	global audio_source_string
	global phone_name_string
	audio_source_string = 'Audio Off'
	audio_artist_string = ''
	phone_name_string = ''

	# declear button icons
	global home_icon
	global audio_icon
	global climate_icon
	global phone_icon
	global apps_icon
	global setting_icon
	home_icon = QtGui.QPixmap('images/home_icon.png')
	audio_icon = QtGui.QPixmap('images/audio_icon.png')
	climate_icon = QtGui.QPixmap('images/climate_icon.png')
	phone_icon = QtGui.QPixmap('images/phone_icon.png')
	apps_icon = QtGui.QPixmap('images/app_icon.png')
	setting_icon = QtGui.QPixmap('images/setting_icon.png')

