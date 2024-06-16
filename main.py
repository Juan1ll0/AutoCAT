import uasyncio as asyncio
from components.servo import Servo
from components.dispenser import Dispenser
from components.scheduler import Scheduler, Event
from components.config import Config
# from microdot import Microdot, Request, Response, abort, redirect, send_file  # noqa: F401
from lib.microdot import Microdot, Request, Response, abort, redirect, send_file
from microdot_utemplate import Template

app = Microdot()
Response.default_content_type = 'text/html'

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

servo = Servo(6)
dispenser = Dispenser(servo)
scheduler = Scheduler(10)

loadEventsFromConfig(scheduler, config.getConfig("scheduled"), dispenser)
scheduler.getNextEvent()

@app.get('/')
async def index(request):
    return Template('index.html').render()

@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        return 'Not found', 404
    return send_file('static/'+path)


async def main():
    robot_task = asyncio.create_task(scheduler.run())
    server_task = asyncio.create_task(app.run(debug=True))
    
    # Wait for both tasks to complete (they won't, but this keeps them running)
    await asyncio.gather(robot_task, server_task)

asyncio.run(main())