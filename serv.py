import socket
import threading

''' This will be a chat server that will recieve messages, and store them
then deliver all messages when a client asks for a message
'''

HOST = ('127.0.0.1', 5000)

class Server(object):
    def __init__(self, host, secret='recieve_all'):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(host)
        self.s.listen(1)
        self.connections = []
        self.messages = []
        self.secret = secret

    def _message_server(self, conn_tuple, buffer=1024):
        '''This will handle storing data'''
        while True:
            try:
                msg = conn_tuple[0].recv(buffer)
                if str(msg, 'utf-8') == self.secret:
                    for conn, addr in self.connections:
                        for message in self.messages:
                            conn.send(message)
                    self.messages = []
                else:
                    self.messages.append(msg)

            except Exception as e:
                print(e)
                self.connections.remove(conn_tuple)
                break

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


if __name__ == '__main__':
    serv = Server(HOST)
    serv._connection_manager()