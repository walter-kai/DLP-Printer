# Walt Yao
# November 2014
from __future__ import print_function
import threading
import time
import constants
import sys, os, signal
from collections import Counter
import adafruit.Adafruit_ADS1x15.Adafruit_ADS1x15 as ADS1x15


# from Tkinter import *


class SensorThread(threading.Thread):
    def __init__(self, thread_motor):
        threading.Thread.__init__(self)

        self.adc = ADS1x15.ADS1x15(ic=0x00)
        self.engaged = False
        self.alive = True

        self.out_limit = 0
        self.in_limit = 0
        self.motor = thread_motor
        # self.activated = False
        self.direction = None

    def engage(self, direction):
        self.direction = int(direction)
        self.engaged = self.check_pos()
        return self.engaged

    def test_sensor(self):
        while True:
            reading = self.adc.readADCSingleEnded(0, 6144, 256)
            # time.sleep(1)
            print ("\rSensor: ", reading, " mV", end="")
            # print("sensor:", reading)

    def print_pos(self):
        reading = self.get_calibration(50)
        print("Current pos:", reading, "| out limit:",self.out_limit, "| in limit:",self.in_limit, "|")

    def check_pos(self):
        # returns TRUE if inbounds
        result = True
        reading = int(self.adc.readADCSingleEnded(0, 6144, 256))
        if (reading >= self.in_limit and self.direction is 0) or (reading <= self.out_limit and self.direction is 1):
            result = False
        return result

    def stop(self):
        self.engaged = False

    def kill(self):
        self.alive = False

    def run(self):
        # I never stop
        while self.alive:
            if self.engaged:
                reading = int(self.adc.readADCSingleEnded(0, 6144, 256))
                if (reading >= self.in_limit and self.direction is 0) or (reading <= self.out_limit and self.direction is 1):
                    # print("Stop the motor!")
                    self.motor.stop()
                    #disengage myself
                    self.engaged = False

    def get_calibration(self, amount):
        calibrate = []
        print("Calibrating please wait...")
        for x in range(0, amount):
            reading = self.adc.readADCSingleEnded(0, 6144, 256)
            # time.sleep(.2)
            calibrate.append(reading)
        most_common = Counter(calibrate).most_common(1)
        # print("calibrated to:", )

        # return Counter(calibrate).values()[0]
        return int(most_common[0][0])

    def load_instruction(self, instruction, clientTCP):
        self.instruction = instruction
        if int(instruction) == constants.INST_SENSOR_CALIBRATE_OUT:
            print(":COMMAND>>calibrate sensor out")
            reading = self.get_calibration(256)
            if int(reading) < 3:
                self.out_limit = 0
            else:
                self.out_limit = int(reading)
            status = "slave %s>> calibrated outside limit to:%d" % (sys.argv[1], self.out_limit)
            print(status)
            clientTCP.send("@" + status)

        elif int(instruction) == constants.INST_SENSOR_CALIBRATE_IN:
            print(":COMMAND>>calibrate sensor in")
            reading = self.get_calibration(256)
            self.in_limit = int(reading)
            status = "slave %s>> calibrated inside limit to:%d" % (sys.argv[1], self.in_limit)
            print(status)
            clientTCP.send("@" + status)
        # else:
            # print(":COMMAND>>skipping instruction:", instruction)
