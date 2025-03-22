from machine import Pin, PWM
import time

#servo = PWM(Pin(15),freq=50)
class Servo:
    def __init__(self, pin, angle, delay=3):
        self.servo = PWM(Pin(pin, Pin.OUT),freq=50)
        self.angle = angle
        self.delay = delay
        self.min_duty = 25
        
        if self.angle == 180:
            self.max_duty = 125  # 180 degrees
        elif self.angle == 270:
            self.max_duty = 90  # 270 degrees
        else:
            raise ValueError("Unsupported angle. Use 180 or 270 degrees.")
        
        print("going to origin")
        self.goToOrigin()
    
    def goToOrigin(self):
        self.servo.duty(self.min_duty)
        self.position = 0
        time.sleep(self.delay)
        
    def goToEnd(self):
        self.servo.duty(self.max_duty)
        self.position = 1
        time.sleep(self.delay)
        
    def move(self):
        if self.position == 0:
            self.goToEnd()
        else:
            self.goToOrigin()
            
        
            
        
            
        
        
            
                                                                                                                                    