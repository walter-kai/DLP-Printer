# Walt Yao
# November 2014
from __future__ import print_function

import time
import constants
import socket
from devices.threadManager import ThreadManager
from devices.message_structure import message_structure

class ClientTCP():

    def __init__(self, who, is_slave):
        self.isSlave = is_slave
        self.thread_manager = ThreadManager(is_slave)
        self.who = who
        if self.who == 1:
            self.name = "slave1"
            self.port = constants.TCP_PORT
            self.ip_add = constants.SLAVE_IP1
        elif self.who == 2:
            self.name = "slave2"
            self.port = constants.TCP_PORT
            self.ip_add = constants.SLAVE_IP2
        else:
            print("error: i dont know you")
        print("Creating socket")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive_tcp_data(self):

        print("Connecting to:", self.ip_add +":" + str(self.port))
        self.socket.connect((self.ip_add, self.port))
        self.running = True
        print(self.ip_add, "is connected.")

        while True:
            data = self.socket.recv(constants.BUFFER_SIZE)
            if not data: break
            print(data)
            if data[0] is not "@":
                msg_struct = message_structure()
                msg_struct.decode(data)
                if self.thread_manager is not None:
                    self.thread_manager.set_instruction(msg_struct, self)
            else:
                #we want to show this on the GUI
                if data[7] == "1":
                    print("slave 1")
                if data[7] == "2":
                    print("slave 2")

        print(":status>>Closing:", "/".join([self.name, self.ip_add, str(self.port)]))

    def execute_command(self, char):
        if char == "!":
            if self.buffering_instruction:

                self.buffering_instruction = False
                if self.isSlave:
                    msg_struct = message_structure()
                    msg_struct.decode(self.instruction)
                    self.thread_manager.set_instruction(msg_struct, self)
                    # send back a 'finished' message to master
                    self.write("*" + msg_struct.motor_id + "!")

            elif self.buffering_ready_msg:
                self.buffering_ready_msg = False
                print(":status>>received ready message from:", self.instruction)
        elif char == "*":
            # the ready message
            self.instruction = ""
            self.buffering_ready_msg = True
            self.buffering_instruction = False
        elif char == '#':
            self.instruction = ""
            self.buffering_instruction = True
            self.buffering_ready_msg = False
        else:
            if self.buffering_instruction or self.buffering_ready_msg:
                print('adding:', char)
                self.instruction = self.instruction + char

    def stop(self):
        if self.isSlave:
            self.thread_manager.stop()
        self.running = False
        time.sleep(2)
        # self.serialObj.close()
        self.socket.close()

    def write(self, str):

        print(":status>>Sending this:", str)
        print(":status>>to port:", self.port)

        self.socket.send(str)