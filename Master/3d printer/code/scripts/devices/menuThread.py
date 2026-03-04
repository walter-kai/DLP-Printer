# Walt Yao
# November 2014
import threading
from devices.motorImageThread import MotorImageThread
from devices.message_structure import message_structure

class MenuThread(threading.Thread):
    def __init__(self, isTest, socket1, socket2):
        threading.Thread.__init__(self)
        self.settings = settings
        self.socket1 = socket1
        self.socket2 = socket2
        self.isTest = isTest

    def run(self):

        while True:
            if self.isTest:
                instruction = "t"
            else:
                instruction = self.execute_main_menu()
            if len(instruction) > 0:
                if instruction == "0":
                    print "exit"
                    return
                msg_struct = self.build_message_structure(instruction, self.settings)
                msg_struct.output_print()

                if instruction is "t":
                    motorImage = MotorImageThread()
                    motorImage.start()
                    motorImage.load_instruction(msg_struct)
                else:
                    # send the encoded msg_struct over tcp/ip
                    self.socket1.write(msg_struct.encode())
                    self.socket2.write(msg_struct.encode())

    def execute_main_menu(self):
        print '****************MENU OPTIONS**********************'
        print '*************(1) Move motor **********************'
        print '*************(2) Step motor /w image**************'
        print '*************(3) Step motor /wo image*************'
        print '*************(4) Flash image**********************'
        # print '******(7) Sensor mode*************************'
        # print '******(8) Intercomm mode**********************'
        print '*************(9) Settings*************************'
        print '*************(t) Test mode************************'
        print '*************(0) Exit*****************************'

        option = raw_input(">>")

        return option

    def check_settings_options(self, option):
        if option == 1:
            reader.write("sensor", raw_input("Enter 1 to turn on, 0 to off>>"))
        elif option == 2:
            reader.write("tank_length", raw_input("Set the total tank distance in centimeters>>"))

    def build_message_structure(self, option, settings):
        m_struct = message_structure()
        # print "option:", option
        m_struct.img_file = "3d printer/code/scripts/devices/images/hand.png"

        if option == "t":
            print '****************MENU OPTIONS**********************'
            print '*************(1) Move motor **********************'
            print '*************(2) Step motor /w image**************'
            print '*************(3) Step motor /wo image*************'
            print '*************(4) Flash image**********************'
            option = raw_input(">>")

        m_struct.instruction = option
        if option == "1" or option == "2" or option == "3" or option == "4":
            print ">> Which slave? (1=raspi1[right], 2=raspi2[left] or 0 for both)"
            motor_number = raw_input(">>")
            if len(motor_number) == 0:

                # default
                m_struct.motor_id = "0"
            else:
                m_struct.motor_id = motor_number
        if option == "1" or option == "2" or option == "3":
            print ">> Which direction? (f=forward or b=back)"
            direction = raw_input(">>")
            if len(direction) == 0:

                # default
                m_struct.direction = "f"
            else:
                m_struct.direction = direction
            print ">> How much distance to move? (in CM)"
            length = raw_input(">>")
            if len(length) == 0:
                # default
                m_struct.distance_travel = ".3"
            else:
                m_struct.distance_travel = length

        if option == "2" or option == "3":
            print ">>Resolution? (in microns, default 500)"
            res = raw_input(">>")
            if len(res) == 0:
                # default
                m_struct.resolution = "500"
            else:
                m_struct.resolution = res
        if option == "2" or option == "4":
            print ">>Time of exposure? (in seconds, default 1)"
            exp = raw_input(">>")
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


        return m_struct