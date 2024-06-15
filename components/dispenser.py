import machine

class Dispenser:
    def __init__(self, servo):
        self.servo = servo
        
        
    def dispense(self, quantity):
        for i in range(quantity):
            print("Dispense", i)
            self.servo.move()