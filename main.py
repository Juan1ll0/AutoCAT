from machine import Pin, PWM
import time

def do_connect(SSID, PASSWD):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(hostname="ImHungry")
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSID, PASSWD)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


do_connect("ssid", "paaswd")
servo = PWM(Pin(15),freq=50)

while True:
    # Move to 0
    servo.duty(25)
    print("25")
    time.sleep(5)
    
    # Move to 180
    servo.duty(125)
    print("125")
    time.sleep(5)
    
    