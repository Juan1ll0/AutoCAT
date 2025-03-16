import uasyncio as asyncio
from components.servo import Servo
from components.dispenser import Dispenser
from components.scheduler import Scheduler, Event
from components.config import Config
from lib.microdot import Microdot, Request, Response, abort, redirect, send_file
from lib.microdot_utemplate import Template
import json

app = Microdot()
Response.default_content_type = 'text/html'

# def create_callback(func, arg):
#    def wrapper(*inner_args, **inner_kwargs):
#        return func(arg)
#    return wrapper

def loadEventsFromConfig(scheduler, events, dispenser):
    scheduler.removeAll()
    for event in events:
        # callback = create_callback(dispenser.dispense,event.get("doses"))
        newEvent = Event(event.get("name"),
                         event.get("time"),
                         event.get("quantity"),
                         dispenser.dispense)
                         # lambda cb=callback: cb())
        scheduler.addEvent(newEvent)
                                       
config = Config("config.json")
config.loadConfig()

servo = Servo(6)
dispenser = Dispenser(servo)
scheduler = Scheduler(60)

loadEventsFromConfig(scheduler, config.getConfig("scheduled"), dispenser)
scheduler.getNextEvent()

@app.get('/')
async def index(request):
    hours = scheduler.getAllEvents()
    return Template('index.html').render(hours)

@app.get('/serveFeed')
async def serveFeed(request):
    quantity = 2
    dispenser.dispense(quantity)
    return Response(
        body=json.dumps({'quantity': quantity}),
        headers={'Content-Type': 'application/json'})

@app.post('/setScheduler')
async def setScheduler(request):
    try:
        # Parse the incoming JSON data
        body = request.json
        config.writeConfig(body)
        return Response(
            body=json.dumps({
                'status': 'success',
                'data': body}),
            headers={'Content-Type': 'application/json'})

    except Exception as e:
        # Handle errors (e.g., invalid JSON data)
        print('Error processing request:', str(e))
        return Response(
            body=json.dumps({
                'status': 'error',
                'message': str(e)}),
            headers={'Content-Type': 'application/json'}, status_code=400)
    

@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        return 'Not found', 404
    return send_file('static/'+path)


# app.run(debug=True)

async def main():
    robot_task = asyncio.create_task(scheduler.run())
    server_task = asyncio.create_task(app.run(debug=True))
    
    # Wait for both tasks to complete (they won't, but this keeps them running)
    await asyncio.gather(server_task,robot_task)

asyncio.run(main())