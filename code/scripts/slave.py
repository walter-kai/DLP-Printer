# Walt Yao
# November 2014
from __future__ import print_function
import sys
import signal
import constants
import socket
import threading
from devices.message_structure import message_structure
from devices.threadManager import ThreadManager
import RPi.GPIO as GPIO

def icom_setup(icomm):
    print(":status>>Starting inter communication thread")
    icomm.run()


def interface(icomm):
    print("interface")
    while True:
        if input("quit?y/n:") == "y":
            icomm.stop()
            sys.exit()


def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    # signal.signal(signal.SIGINT, original_sigint)

    # if input("\nReally quit? (y/n)> ").lower() is not "n":
    threadManager.stop()
    print("Ok ok, quitting")
    GPIO.cleanup()
    sys.exit(1)

    # except KeyboardInterrupt:
    #     print("Ok ok,scs quitting")
    #     GPIO.cleanup()
    #     sys.exit(1)

    # # restore the exit gracefully handler here
    # signal.signal(signal.SIGINT, exit_gracefully)

def data_received(data, conn, thread_manager):
    print("Received data:", data)
    msg_struct = message_structure()
    msg_struct.decode(data)

    thread_manager.set_instruction(msg_struct, conn)

def wait_for_instruction(ip_address, thread_manager):
    # print "Creating server socket"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Created server socket at:", ip_address, ":", str(constants.TCP_PORT))
    # s.connect(('192.168.0.17', port))
    s.bind((ip_address, constants.TCP_PORT))
    # print "Binded to port:", constants.TCP_PORT
    # s.listen(1)
    # self.running = True
    print("Waiting for a client...")
    while True:
        s.listen(1)
        conn, address = s.accept()
        print("Client connected:", address)
        print("\nListening for command...")
        while True:
            data = conn.recv(constants.BUFFER_SIZE)
            if not data:
                break
            else:
                msgExecute = TCP_msgExecute(conn, thread_manager, data)
                msgExecute.start()
                msgExecute.join()
                print("\nListening for command...")
            data = ""
        print("Client terminated, waiting for a new client...")

class TCP_msgExecute(threading.Thread):

    def __init__(self, conn, thread_manager, data):
        threading.Thread.__init__(self)
        self.connection_socket = conn
        self.thread_manager = thread_manager
        self.data = data

    def run(self):
        if len(self.data) > 0:
            msg_struct = message_structure()
            msg_struct.decode(self.data)

            self.thread_manager.set_instruction(msg_struct, self.connection_socket)

# START OF APPLICATION
if __name__ == "__main__":
    # we're gonna cheat and clean up all the other devices
    # os.system("~/killslave")

    # threadManager = None
    original_sigint = signal.getsignal(signal.SIGINT)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)

    # if threadManager is None:
    # print "create a threadManager()"
    threadManager = ThreadManager(True)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    my_ipaddress = s.getsockname()[0]
    s.close()

    wait_for_instruction(my_ipaddress, threadManager)
    # icom = InterCommThread("slave" + sys.argv[1])
    # thread_icom = threading.Thread(target=icom_setup(icom))
    # thread_interface = threading.Thread(target=interface(icom))

# thread_interface.start()
# thread_icom.start()
