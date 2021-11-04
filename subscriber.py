import sys
import zmq
import asyncio

port = "5557" # for now default port for subscribers is 5557
id = 0

# get() consumes a message from a topic

if len(sys.argv) > 1:
    id = sys.argv[1]

#subscribe() subscribes a topic
def subscribe(topic = "NULL"):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:{}".format(port))
    socket.send("{}".format("SUB:"+id+":"+topic).encode())
    # socket.close() is called when garbage collection happens but we should still call it
    return

#unsubscribe() unsubscribes a topic

subscribe()
