from components.servo import Servo
from components.dispenser import Dispenser
from components.scheduler import Scheduler, Event
from components.config import Config

def create_callback(func, arg):
    def wrapper(*inner_args, **inner_kwargs):
        return func(arg)
    return wrapper

def loadEventsFromConfig(scheduler, events, dispenser):
    scheduler.removeAll()
    for event in events:
        callback = create_callback(dispenser.dispense,event.get("doses"))
        newEvent = Event(event.get("name"),
                         event.get("time"),
                         lambda cb=callback: cb())
        scheduler.addEvent(newEvent)
                                       
config = Config("config.json")
config.loadConfig()

servo = Servo(15)
dispenser = Dispenser(servo)
scheduler = Scheduler(60)

loadEventsFromConfig(scheduler, config.getConfig("scheduled"), dispenser)
scheduler.getNextEvent()
scheduler.run()