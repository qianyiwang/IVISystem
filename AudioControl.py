import gobject
import dbus
import dbus.mainloop.glib
import os
import GlobalValues

class AudioControl():
	def __init__(self):
		bus = dbus.SessionBus()
		player = bus.get_object('org.mpris.clementine','/Player')
		iface = dbus.Interface(player, dbus_interface = 'org.freedesktop.MediaPlayer')
		metadata = iface.GetMetadata()
		print (metadata['title'])
		print (metadata['artist'])
		GlobalValues.audio_source_string = metadata['title']+"\n"+metadata['artist']
		GlobalValues.audio_artist_string = metadata['artist']

		# man = dbus.SessionBus().get_object('org.bluez', '/')

		# AudioSourceServiceClass_UUID = "0000110A-0000-1000-8000-00805F9B34FB"
		# #Get bluez dbus objects
		# man = bus.get_object('org.bluez', '/')
		# iface = dbus.Interface(man, 'org.bluez.Manager')
		# adapterPath = iface.DefaultAdapter()
		# adapter = dbus.Interface(bus.get_object('org.bluez', adapterPath),dbus_interface='org.bluez.Adapter')
		# devices = adapter.GetProperties()['Devices']
		
		# # get clementine data
		# player = bus.get_object('org.mpris.clementine','/Player')
  #   	# iface = dbus.Interface(player, dbus_interface = 'org.freedesktop.MediaPlayer')
  #   	# metadata = iface.GetMetadata()
  #   	# print (metadata['title'])
  #   	# 
  #   	# GlobalValues.audio_source_string = metadata['title']
  #   	# GlobalValues.audio_artist_string = metadata['artist']
		# for d in devices:
		#     dev = dbus.Interface(bus.get_object('org.bluez', d),dbus_interface='org.bluez.Device')
		#     props = dev.GetProperties()
		#     if any(AudioSourceServiceClass_UUID in UUID.upper() for UUID in props["UUIDs"]):
		#         #This device is an A2DP Audio source
		#         devobj = bus.get_object('org.bluez', d)
		#         # iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')
		#         devobj.Trusted = True
		#         if props["Connected"] == True:
		#         	print  (props["Name"] + " is connected!")
		#         	print  (props["Name"] + " has A2DP audio source")
		#         	GlobalValues.phone_name_string = props['Name']

