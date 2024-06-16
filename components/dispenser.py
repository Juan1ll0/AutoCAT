import machine

class Dispenser:
    def __init__(self, servo):
        self.servo = servo
        
        
    def dispense(self, quantity):
        print("Serving feed...", quantity)
        for i in range(quantity):
            self.servo.move()