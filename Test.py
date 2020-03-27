from digi.xbee.devices import XBeeDevice

device = XBeeDevice("/dev/cu.usbserial-A-4008238",9600)

device.open()

device.send_data_broadcast("Hello XBee World")

device.close()
