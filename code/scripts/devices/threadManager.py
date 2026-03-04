from __future__ import print_function
# Walt Yao
# December 2014
__author__ = 'Yaoza'

import sys
import constants
from devices.sensorThread import SensorThread
from devices.motorImageThread import MotorImageThread

def sig_handler(signum, frame):
    print('Signal handler called with signal', signum)

    sys.exit()


class ThreadManager():
    # def sig_handler(self, signum):
    #     print('Signal handler called with signal', signum)

    def __init__(self, is_slave):
        # create sig handler
        # signal.signal(signal.SIGINT, self.sig_handler)
        self.is_slave = is_slave
        self.thread_sensor_alive = False

        if is_slave:
            print("Starting motor thread")
            self.thread_motor = MotorImageThread()
            print("Starting sensor thread")
            self.thread_sensor = SensorThread(self.thread_motor)
            self.thread_sensor.start()

        else:
            self.thread_motor = None
            self.thread_sensor = None

    def set_instruction(self, msg_struct, clientTCP):

        if len(sys.argv) is 1:
            # execute master handlers
            # print("this is where the master handles feedback")
            return False
        # if the msg_struct.motor_id matches my own ID from the arg or if 0 (means both motors)
        elif msg_struct.motor_id == sys.argv[1] or msg_struct.motor_id == "0":
            if self.is_slave:
                # print("instr:", msg_struct.instruction)
                if msg_struct.instruction == constants.INST_MOTOR_STOP:
                    self.thread_motor.stop()
                elif int(msg_struct.instruction) is constants.INST_SENSOR_CALIBRATE_OUT or int(msg_struct.instruction) is constants.INST_SENSOR_CALIBRATE_IN:
                    self.thread_sensor.load_instruction(msg_struct.instruction, clientTCP)
                elif int(msg_struct.instruction) is constants.INST_MOTOR_FLASH_IMAGE:
                    self.thread_motor.load_instruction(msg_struct, clientTCP)
                else:
                    if self.thread_motor is not None:

                        if msg_struct.sensor_on is "y":
                            # print("Sensor engaged")
                            if self.thread_sensor.engage(msg_struct.direction):
                                self.thread_motor.load_instruction(msg_struct, clientTCP)
                                self.thread_sensor.stop()
                            else:
                                print("Sensor out of bounds")
                        else:
                            self.thread_motor.load_instruction(msg_struct, clientTCP)
                self.thread_sensor.print_pos()
                return True
        else:
            print("Ignored msg, not my motor ID:", msg_struct.motor_id)
            return False

    def stop(self):
        if self.thread_motor is not None:
            self.thread_motor.stop()
        if self.thread_sensor is not None:
            self.thread_sensor.kill()