from startiot import Startiot
import pycom
import time

pycom.heartbeat(False)     # disable the blue blinking
iot = Startiot()

print("Connecting....")
pycom.rgbled(0x0F0000)    # Red light when not connected
iot.connect()
pycom.rgbled(0x00000F)    # Blue light when connected

count = 0

while True:
  print("Send data...",  count)
  data = "TEMP,%s" % (count)
  count = count + 1
  iot.send(data)
  time.sleep(10)
