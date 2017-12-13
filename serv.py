import socket
import threading

''' This will be a chat server that will recieve messages, and store them
then deliver all messages when a client asks for a message
'''

HOST = ('127.0.0.1', 5000)

class Server(object):
    def __init__(self, host):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(host)
        self.s.listen(1)
        self.connections = []
        self.message = []

    def _handle_connections(self):