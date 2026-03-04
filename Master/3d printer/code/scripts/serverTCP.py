# Walt Yao
# January 2015

from __future__ import print_function

__author__ = 'Yaoza'
import threading
import constants


class ServerTCP(threading.Thread):

    def __init__(self, conn, thread_manager):
        threading.Thread.__init__(self)

        self.connection_socket = conn
        self.thread_manager = thread_manager

    def run(self):