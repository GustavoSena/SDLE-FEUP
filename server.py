import sys
import zmq
import asyncio

# peers will have to connect to the server in order to get messages published on a certain topic
# peers will have an unique ID so that the server can keep track of each peer individually 