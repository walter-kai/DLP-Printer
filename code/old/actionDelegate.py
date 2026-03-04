# Walt Yao
# November 2014
  
import signal, sys, threading
import constants
from threads.keypressThread import KeypressThread
from threads.sensorThread import SensorThread
from threads.motorImageThread import MotorImageThread
from threads.settings import XmlReader

from time import sleep     # this lets us have a time delay

MY_LOCK = threading.Lock()

def read_settings():
    global reader
    reader = XmlReader()
    global settings
    settings = reader.read()



def sig_handler(signum, frame):
    print 'Signal handler called with signal', signum
    motor.stop()
    if settings.sensorOn:
        sensor.stop()
    sys.exit()

def initialize_hardware(instruction, args):
    signal.signal(signal.SIGINT, sig_handler)

    # global sensor
    global motor
    if settings.sensorOn:
        sensor = SensorThread()
        sensor.start()
    if instruction != 7:
        motor = MotorImageThread(MY_LOCK)
        motor.start()
        motor.load_instruction(instruction,settings.tank_length,args)

def check_settings_options(option):


    if option == 1:
        reader.write("sensor", raw_input("Enter 1 to turn on, 0 to off>>"))
    elif option == 2:
        reader.write("distance", raw_input("Set the total tank distance in centimeters>>"))




def build_args(option):
    args = []

    if option == 0:
        sys.exit()
    else:
        if option == 5 or option == 6:
            arg.append(int(raw_input(">> How much distance to move? (in CM)")))
        elif option == 3 or option ==4:
            res = raw_input("Resolution? (in microns, default 500)>>")
            if len(res) == 0:
                # default
                arg.append(500)
            else:
                arg.append(int(res))
            exp = raw_input("Time of exposure? (in seconds, default 1)>>")
            if len(exp) == 0:
                # default
                arg.append(1)
            else:
                arg.append(int(exp))
        elif option == 9:
            print '******************SETTINGS********************'
            print '******(1) Activate/Deactivate sensor**********'
            print '******(2) Set tank distance*******************'
            print '******(0) Main Menu***************************'
            check_settings_options(int(raw_input(">>")))

        return args


def execute_main_menu():
    print '***************MENU OPTIONS*******************'
    print '******(1) Move motor C************************'
    print '******(2) Move motor CC***********************'
    print '******(3) Step motor C************************'
    print '******(4) Step motor CC***********************'
    print '******(5) Move motor x distance C*************'
    print '******(6) Move motor x distance CC************'
    print '******(7) Sensor mode*************************'
    print '******(9) Settings****************************'
    print '******(0) Exit********************************'

    return int(raw_input(">>"))

# START OF APPLICATION

while True:
    menu_option = execute_main_menu()

    args = build_args(menu_option)

    if menu_option == 0:
        break
    if menu_option != 9:
        read_settings()
        initialize_hardware(menu_option, args)
    else:
        pass