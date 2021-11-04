import sys
import zmq
import asyncio

from zmq.backend import zmq_poll

# peers will have to connect to the server in order to get messages published on a certain topic
# peers will have an unique ID so that the server can keep track of each peer individually

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:{}".format(port))

print(zmq.NOBLOCK)

async def save_message(args):
    #create a file descriptor and save a message to a new file or append to the end of one that already exists
    return

async def read_message(args):
    #read from a file a message that belongs to a certain topic
    return

def main_loop():
    #Server must be listening to incoming messages from publishers.
    #Server must also be listening for get requests from subscribers.

    while True:
        message = socket.recv() #zmq.NOBLOCK
        print("Received message: {}".format(message))
        socket.send(b"OK")
    return

def start():
    print("Starting server...")
    main_loop()

start()