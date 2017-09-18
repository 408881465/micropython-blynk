import network
wlan=None
def connect():
  global wlan
  wlan=network.WLAN(network.STA_IF) 
  wlan.active(True)
  wlan.connect('<SSID>', '<PASSWORD>')
  while not wlan.isconnected():
    pass
  print('IPAddress: {}'.format(wlan.ifconfig()[0]))
  
def get_ip():
  return wlan.ifconfig()[0]

