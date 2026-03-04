# Walt Yao
# November 2014
  
import sys, time, threading
import constants
from threads.keypressThread import KeypressThread
# from io.keypressThread import InterCommThread
from serverTCP import server_TCP
from threads.sensorThread import SensorThread
from threads.motorImageThread import MotorImageThread
from threads.settings import XmlReader
from threads.message_structure import message_structure

lock = threading.Lock()

class MainThread(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.icomm = server_TCP("master")

    def run(self):
        if self.thread_id == constants.THREAD_TYPE_MAIN_LOOP:
            print "loop"
            self.settings = XmlReader().read()
            main_loop(self.settings)
            print "stopping main_loop"
        elif self.thread_id == constants.THREAD_TYPE_MAIN_ICOM:
            print ":status>>Starting inter communication thread"
            self.icomm.my_lock = lock
            self.icomm.run()

    def stop(self):
        self.icomm.stop()

def read_settings():
    global reader
    reader = XmlReader()
    global settings
    settings = reader.read()

def delegate_instruction(msg_struct):
    intercomm = server_TCP("master")
    intercomm.write(msg_struct.encode())

def check_settings_options(option):
    if option == 1:
        reader.write("sensor", raw_input("Enter 1 to turn on, 0 to off>>"))
    elif option == 2:
        reader.write("tank_length", raw_input("Set the total tank distance in centimeters>>"))




def build_message_structure(option, settings):
    m_struct = message_structure()
    print "option:", option
    m_struct.instruction = option

    if option == "1" or option == "2" or option == "3" or option == "4":
        motor_number = raw_input(">> Which motor? (1, 2 or 0 for both)")
        if len(motor_number) == 0:
            # default
            m_struct.motor_id = "0"
        else:
            m_struct.motor_id = motor_number

        length = raw_input(">> How much distance to move? (in CM)")
        if len(length) == 0:
            # default
            m_struct.distance_travel = "1.0"
        else:
            m_struct.distance_travel = length

    if option == "3" or option == "4":
        res = raw_input("Resolution? (in microns, default 500)>>")
        if len(res) == 0:
            # default
            m_struct.resolution = "500"
        else:
            m_struct.resolution = res
        exp = raw_input("Time of exposure? (in seconds, default 1)>>")
        if len(exp) == 0:
            # default
            m_struct.exposure_time  = "1.0"
        else:
            m_struct.exposure_time  = exp
    elif option == "9":
        print '******************SETTINGS************************'
        print '**********(1) Activate/Deactivate sensor**********'
        print '**********(2) Set tank distance*******************'
        print '**********(0) Main Menu***************************'
        check_settings_options(int(raw_input(">>")))

    elif option == 0:
        sys.exit()

    if settings.sensorOn:
        m_struct.sensor_on = "y"
    else:
        m_struct.sensor_on = "n"

    return m_struct

def execute_main_menu():


    print '****************MENU OPTIONS**********************'
    print '*************(1) Move motor C*********************'
    print '*************(2) Move motor CC********************'
    print '*************(3) Step motor C*********************'
    print '*************(4) Step motor CC********************'
    # print '******(7) Sensor mode*************************'
    # print '******(8) Intercomm mode**********************'
    # print '******(9) Settings****************************'
    # print '******(s) Stop motor**************************'
    print '*************(0) Exit*****************************'

    with lock:
        option = raw_input(">>")

    return option

def main_loop(settings):
    read_settings()
    while True:

        instruction = execute_main_menu()
        if instruction == "0":
            print "exit"
            thread1.stop()
            return
        msg_struct = build_message_structure(instruction, settings)

        read_settings()
        delegate_instruction(msg_struct)

# START OF APPLICATION
thread2 = MainThread(constants.THREAD_TYPE_MAIN_LOOP)
thread1 = MainThread(constants.THREAD_TYPE_MAIN_ICOM)

thread2.start()
thread1.start()

