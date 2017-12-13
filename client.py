import socket
import threading

HOST = ('127.0.0.1', 5000)

class Client(object):
    def __init__(self, host):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(host)


    def send(self):
        while True:
            try:
                msg = input('--> ')
                msg = bytes(msg, 'utf-8')
                self.s.send(msg)

            except Exception as e:
                print(e)

    def recieve(self, buffer=1024):
        while True:
            try:
                msg = self.s.recv(buffer)
                msg = str(msg, 'utf-8')
                print(msg)

            except Exception as e:
                print(e)

    def run(self):
        methods = (self.recieve, self.send)
        for method in methods:
            mThread = threading.Thread(target=method)
            mThread.daemon = True
            mThread.start()


if __name__ == '__main__':
    client = Client(HOST)
    client.run()
