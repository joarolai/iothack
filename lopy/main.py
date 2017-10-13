from libiot import LoRaIoT
import pycom
import time

# Change app_eui and app_key to match your application
app_eui = "000000000000015d"
app_key = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"

pycom.heartbeat(False)              # Disable the blue blinking
iot = LoRaIoT(app_eui, app_key)

pycom.rgbled(0x0F0000)              # Red light when not connected
iot.connect()
pycom.rgbled(0x000F00)              # Green light when connected

count = 0

while True:
  data = "TEMP,%s" % (count)
  count = count + 1
  print("Send data:", data)
  iot.send(data)
  pycom.rgbled(0x00000F)            # Blue flash when sending
  time.sleep(0.1)
  pycom.rgbled(0x000F00)            # Green light when sleeping
  time.sleep(10)
