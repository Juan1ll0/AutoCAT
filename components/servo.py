from machine import Pin, PWM
import time

#servo = PWM(Pin(15),freq=50)
class Servo:
    def __init__(self, pin, delay=3):
        self.servo = PWM(Pin(pin),freq=50)
        self.delay = delay
        self.goToOrigin()
    
    def goToOrigin(self):
        print("going to origin")
        self.servo.duty(25)
        self.position = 0
        time.sleep(self.delay)
        
    def goToEnd(self):
        print("going to end")
        self.servo.duty(125)
        self.position = 1
        time.sleep(self.delay)
        
    def move(self):
        print("moving, current position: ", self.position)
        if self.position == 0:
            self.goToEnd()
        else:
            self.goToOrigin()
            
        
            
        
            
        
        
            
                                                                                                                                    