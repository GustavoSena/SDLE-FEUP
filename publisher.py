import sys
import zmq
import asyncio

port = "5556" # for now default port for publishers is 5556

# if len(sys.argv) > 1:
#     port =  sys.argv[1]
#     int(port)


# put() publishes a message on a topic

#subscribe() subscribes a topic
#unsubscribe() unsubscribes a topic

def put(message, topic = "NULL"):
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:{}".format(port))
    socket.send("{}".format(message).encode())
    # socket.close() is called when garbage collection happens but we should still call it
    return

def main_loop():
    #this loop will listen to keyboard inputs and proceed accordingly
    put("teste")


    return

main_loop()
