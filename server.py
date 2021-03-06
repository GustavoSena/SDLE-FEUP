import sys
import zmq
import asyncio
import os
import signal

# peers will have to connect to the server in order to get messages published on a certain topic
# peers will have an unique ID so that the server can keep track of each peer individually

# Global variables used throughout the program
pub_port = "5556"
sub_port = "5557"

program_files_dir = "program_files"

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

        # Create a dictionary with the sockets we created
        sockets = dict(poller.poll()) # we can setup a timeout for exiting blocking calls poll(1000) will block for 1s an then timeout
        
        # Using the socket as a key we can find if the socket has content to poll 
        if(pub_socket in sockets and sockets[pub_socket] == zmq.POLLIN):
            pub_message = pub_socket.recv(zmq.NOBLOCK)
            print("Received message from a publisher: {}".format(pub_message))
            pub_socket.send(b"OK")

        if(sub_socket in sockets and sockets[sub_socket] == zmq.POLLIN):
            sub_message = sub_socket.recv(zmq.NOBLOCK)
            print("Received message from a subscriber: {}".format(sub_message))
            sub_socket.send(b"OK")

    return

# Create folders and files where content will be saved
def create_program_files():
    if not os.path.exists(program_files_dir):
        os.makedirs(program_files_dir)
    
# Call the main loop and startup functions
def start():
    print("Starting server...")
    create_program_files()
    main_loop()

 
# A bit of cleanup code in case we use ctrl-c to end the server
def handler(signum, frame):
    msg = "Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = input()
    if res == 'y':
        print()
        exit(1)
 
signal.signal(signal.SIGINT, handler)

# Start the server
start()