# Walt Yao
# November 2014
import threading
from clientTCP import ClientTCP
from devices.menuThread import MenuThread
# from devices.presets import Presets

class CommunicationThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.socket_port = None
        self.slave_id = id
        self.socket_port = ClientTCP(id, False)


    def run(self):
        self.socket_port.receive_tcp_data()

# settings = Presets()

if raw_input("test mode? y/n: ") is "y":
    isTest = True
    menu_thread = MenuThread(isTest, 0, 0)
    menu_thread.run()
else:
    isTest = False
    com_thread1 = CommunicationThread(1)
    com_thread2 = CommunicationThread(2)
    com_thread1.start()
    com_thread2.start()
    menu_thread = MenuThread(isTest, com_thread1.socket_port, com_thread2.socket_port)
    menu_thread.run()

