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

    def _message_server(self, conn_tuple):
        '''This will handle storing data'''

    def _connection_manager(self):
        '''This will manage putting new connections in list and sending them to the message server'''
        while True:
            conn, addr = self.s.accept()
            connect_tuple = (conn, addr)
            self.connections.append(connect_tuple)

            # Create thread for individual connection
            chat_thread = threading.Thread(target=self._message_server, args=(connect_tuple,))
            chat_thread.daemon = True
            chat_thread.start()

