# Walt Yao
# November 2014
import threading
from clientTCP import ClientTCP

# it's a class that spawns a thread and is the executor or the TCP class
class CommunicationThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.socket_port = None
        self.slave_id = id
        self.socket_port = ClientTCP(id, False)


    def run(self):
        self.socket_port.receive_tcp_data()