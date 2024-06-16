import time
import asyncio

def get_local_time():
    now = time.localtime()
    hour = now[3]
    minute = now[4]
    return "{:02d}:{:02d}".format(hour, minute)
    

class Event:
    def __init__(self, name, time, quantity, callback):
        self.name = name
        self.atTime = time
        self.quantity = quantity
        self.callback = callback
    
    def getTime(self):
        hours, minutes = self.atTime.split(":")
        hours = int(hours)
        return "{:02d}:{:s}".format(hours, minutes)

    def run(self):
        print("Running...",self.name)
        self.callback(self.quantity)

class Scheduler:
    def __init__(self, every=60):
        self.every = every
        self.events = []
        
    def addEvent(self, event):
        self.events.append(event)
        
    def removeEvent(self, pos):
        self.remove(pos)
        
    def removeAll(self):
        self.events = []
        
    def getNextEvent(self):
        def time_to_tuple(event):
            return tuple(map(int, event.getTime().split(":")))

        # Sort events by time
        sorted_events = sorted(self.events, key=time_to_tuple)

        localtime = get_local_time()
        for event in sorted_events:
            eventTime = event.getTime()
            if localtime < eventTime:
                return eventTime
        
    def getAllEvents(self):
        return self.events
            
    def checkEvents(self):
        localtime = get_local_time()
        print("Checking events...", localtime)
        for event in self.events:
            if event.getTime() == localtime:
                event.run()
                
    def run(self):
        print('Starting robot...')
        while True:
            self.checkEvents()
            yield from asyncio.sleep(self.every)