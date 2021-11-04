import sys
import zmq
import asyncio

from zmq.backend import zmq_poll

# peers will have to connect to the server in order to get messages published on a certain topic
# peers will have an unique ID so that the server can keep track of each peer individually

pub_port = "5556"
sub_port = "5557"

# if len(sys.argv) > 1:
#     pub_port =  sys.argv[1]
#     int(pub_port)

# create pub and sub sockets

context = zmq.Context()

# pub socket is used to communicate with publishers
pub_socket = context.socket(zmq.REP)
pub_socket.bind("tcp://*:{}".format(pub_port))

# sub socket is used to communicate with subscribers

sub_socket = context.socket(zmq.REP)
sub_socket.bind("tcp://*:{}".format(sub_port))

async def save_message(args):
    #create a file descriptor and save a message to a new file or append to the end of one that already exists
    return

async def read_message(args):
    #read from a file a message that belongs to a certain topic
    return

def main_loop():
    #Server must be listening to incoming messages from publishers.
    #Server must also be listening for get requests from subscribers.

    #start polling

    poller = zmq.Poller() #At the moment we only need to listen to 2 sockets

    #Register both sockets for polling 

    poller.register(pub_socket, zmq.POLLIN)
    poller.register(sub_socket, zmq.POLLIN)


    while True:
        sockets = dict(poller.poll()) # we can setup a timeout for exiting blocking calls poll(1000) will block for 1s an then timeout
        
        if(pub_socket in sockets and sockets[pub_socket] == zmq.POLLIN):
            pub_message = pub_socket.recv(zmq.NOBLOCK)
            print("Received message from a publisher: {}".format(pub_message))
            pub_socket.send(b"OK")

        if(sub_socket in sockets and sockets[sub_socket] == zmq.POLLIN):
            sub_message = sub_socket.recv(zmq.NOBLOCK)
            print("Received message from a subscriber: {}".format(sub_message))
            sub_socket.send(b"OK")

        
    return

def start():
    print("Starting server...")
    main_loop()

start()