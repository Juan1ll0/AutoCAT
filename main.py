from components.servo import Servo
from components.dispenser import Dispenser
from machine import Pin, PWM
 
servo = Servo(15)
dispenser = Dispenser(servo)


dispenser.dispense(2)