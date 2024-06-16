from machine import Pin, PWM
import time

#servo = PWM(Pin(15),freq=50)
class Servo:
    def __init__(self, pin, delay=3):
        self.servo = PWM(Pin(pin),freq=50)
        self.delay = delay
        print("going to origin")
        self.goToOrigin()
    
    def goToOrigin(self):
        self.servo.duty(25)
        self.position = 0
        time.sleep(self.delay)
        
    def goToEnd(self):
        self.servo.duty(125)
        self.position = 1
        time.sleep(self.delay)
        
    def move(self):
        if self.position == 0:
            self.goToEnd()
        else:
            self.goToOrigin()
            
        
            
        
            
        
        
            
                                                                                                                                    