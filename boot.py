# boot.py -- run on boot-up
import network
import ntptime
import os, time
# import gc
from lib.fs import ReadJsonFile


# Load config from config file Wifi credentials
networkConfig = ReadJsonFile("wifi.json")
ssid = networkConfig.get("ssid")
password = networkConfig.get("passwd")
config = networkConfig.get("config")

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        
        if config and all(k in config for k in ["static_ip", "subnet_mask", "gateway", "dns"]):
            print("Applying static IP configuration...")
            sta_if.ifconfig((config['static_ip'], config['subnet_mask'], config['gateway'], config['dns']))
        else:
            print("No static IP configuration found, using DHCP.")

        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Connected! Network config:', sta_if.ifconfig())
    
print("Connecting to your wifi...")
do_connect()
# gc.collect()

try:
    # Set time
    ntptime.settime()
except:
    print("problems setting date from NTP server")