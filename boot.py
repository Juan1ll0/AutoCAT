# boot.py -- run on boot-up
import network
import ntptime
import os, time
# import gc
from libs.fs import ReadJsonFile


# Load config from config file Wifi credentials
wifiConfig = ReadJsonFile("wifi.json")
SSID = wifiConfig.get("ssid")
SSID_PASSWORD = wifiConfig.get("passwd")

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, SSID_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()
# gc.collect()

# Set time
ntptime.settime()
