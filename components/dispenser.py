import machine

class Dispenser:
    def __init__(self, servo, weight):
        self.servo = servo
        self.weight = weight
        
        
    def dispense(self, quantity):
        print("weight: ", self.weight.getWeight())    
        print("Serving feed...", quantity)
        for i in range(quantity):
            self.servo.move()
