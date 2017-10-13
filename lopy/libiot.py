from network import LoRa
import socket, time, binascii, pycom, network

class LoRaIoT:
  def __init__(self, eui, key):
    self.dev_eui = network.LoRa().mac()
    # Temporary work-around for bug in Telenor MIC
    self.dev_eui = binascii.unhexlify("FFFFFFFF00001071")
    self.app_eui = binascii.unhexlify(eui)
    self.app_key = binascii.unhexlify(key)
    self.lora    = LoRa(mode=LoRa.LORAWAN)

  def connect(self):
    self.lora.join(activation=LoRa.OTAA, auth=(self.dev_eui, self.app_eui, self.app_key), timeout=0)

    while not self.lora.has_joined():
        time.sleep(2.5)

    self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    self.s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)        # Set the data rate
    self.s.setblocking(False)

  def send(self, data):
    self.s.send(data)

  def recv(self, length):
    return self.s.recv(length)
