# Walt Yao
# November 2014
from __future__ import print_function
import sys
import threading
import constants
import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 12)
from devices.imageLoader import ImageLoader

class Motor:

    sleepTime = 0.005
    pinPulseOut = 7
    pinDirOut = 11
    running = True

    def __init__(self):
        # set up BOARD GPIO numbering
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinDirOut, GPIO.OUT)
        GPIO.setup(self.pinPulseOut, GPIO.OUT)

        self.direction_text = ""
        self.direction = 0
        print("loading image loader")
        self.image = ImageLoader()

    def stop(self):
        self.running = False
        sleep(.1)

    def quit_image(self):
        if self.image is not None:
            print("quitting pygame")
            self.image.quit()

    def set_parameters(self, direction, load_image):
        self.direction = int(direction)
        if len(load_image) > 0:
            print("Loading image:", load_image)
            self.image.set_image(load_image)
        # print("THIS IS DIRECTION:", direction)
        if self.direction == constants.INST_MOTOR_MOVE_BACK:
            GPIO.output(self.pinDirOut, GPIO.HIGH)
            self.direction_text = "back (cc)"
            self.sleepTime = 0.01
        else:
            GPIO.output(self.pinDirOut, GPIO.LOW)
            self.direction_text = "forward (c)"
            self.sleepTime = 0.005

    def flash_image(self, msg_struct, clientTCP):

        if self.image is not None:
            self.image.load()
            sleep(float(msg_struct.exposure_time))
            self.image.blank()
            # self.image.check_event()
        status = "slave %s>> flashing %s for %s seconds" % (sys.argv[1], msg_struct.img_file, msg_struct.exposure_time)
        print(status)
        clientTCP.send("@" + status)

    def turn_motor(self, distance_microns, clientTCP):
        # we assume this calculation to convert distance to rotation angle of the motor
        rotation_angle = distance_microns / (70+(44/75))

        status = "slave %s>> turning %d degrees, %s" % (sys.argv[1], rotation_angle, self.direction_text)
        print(status)
        # clientTCP.send("@" + status)

        # currently it takes 1600 loops to make a 360 rotation
        total_count = 1600 * rotation_angle / 360
        count = 0

        # initialize the pin to LOW
        GPIO.output(self.pinPulseOut, GPIO.LOW)
        # loop for the pulse duration divided by sleep time
        while count < total_count and self.running:
            GPIO.output(self.pinPulseOut, GPIO.HIGH)
            sleep(self.sleepTime)
            GPIO.output(self.pinPulseOut, GPIO.LOW)
            count = count + 1

    def action_non_stop_limit(self):
        self.running = True
        while self.running:
            GPIO.output(self.pinPulseOut, GPIO.HIGH)
            sleep(self.sleepTime)
            GPIO.output(self.pinPulseOut, GPIO.LOW)

    def action_step(self, msg_struct, clientTCP):

        current_length = 0.0
        total_length = float(msg_struct.distance_travel) * 10000
        resolution = int(msg_struct.resolution)
        self.running = True
        percent_done = 0

        while percent_done < 101 and self.running and current_length != (float(msg_struct.distance_travel) * 10000):

            current_length = current_length + resolution
            percent_done = 100 * float(current_length) / float(total_length)
            sleep(float(msg_struct.exposure_time))
            self.turn_motor(resolution, clientTCP)

            status = "slave %s>> %d microns of %d microns complete (%f percent)" % (sys.argv[1], current_length, total_length, percent_done)
            print(status)
            clientTCP.send("@" + status)

        self.stop()

    def action_step_image(self, msg_struct, clientTCP):

        current_length = 0.0
        total_length = float(msg_struct.distance_travel) * 10000
        resolution = int(msg_struct.resolution)
        self.running = True
        percent_done = 0

        while percent_done < 101 and self.running and current_length != (float(msg_struct.distance_travel) * 10000):

            current_length = current_length + resolution
            percent_done = 100 * float(current_length) / float(total_length)
            # if self.image is not None:
            self.turn_motor(10000, clientTCP)
            self.set_parameters(constants.INST_MOTOR_MOVE_FRWD, "")
            self.turn_motor(10000-resolution, clientTCP)
            self.flash_image(msg_struct, clientTCP)
            self.set_parameters(constants.INST_MOTOR_MOVE_BACK, "")
                # self.image.load()
                # print("sleeping for:", msg_struct.exposure_time)
                # sleep(float(msg_struct.exposure_time))
                # self.image.blank()
            # else:
            #     sleep(float(msg_struct.exposure_time))
            #     self.turn_motor(resolution, clientTCP)
            status = "slave %s>> %d microns of %d microns complete (%f percent)" % (sys.argv[1], current_length, total_length, percent_done)
            print(status)
            clientTCP.send("@" + status)

        self.stop()

    def action_move_distance_x(self, msg_struct, clientTCP):
        # convert distance travel of cm to microns
        distance_microns = float(msg_struct.distance_travel) * 10000
        # total_rotation_degrees = 5 * distance_microns / 100
        self.running = True
        self.turn_motor(distance_microns, clientTCP)
        self.stop()


class MotorImageThread(threading.Thread):

    def __init__(self):
        # threading.Thread.__init__(self)

        self.instruction = None
        self.motor = Motor()
        self.running = True

        # set the pin number output
        self.pinPulseOut = 7
        self.pinDirOut = 11


    def stop(self):
        print("Stopping motor thread!")
        self.motor.stop()
        # self.motor.quit_image()

    # def run(self):
    #     true = True
    #     self.running = true
    #     # set up pins to output
    #     GPIO.setup(self.pinPulseOut, GPIO.OUT)
    #     GPIO.setup(self.pinDirOut, GPIO.OUT)


    def load_instruction(self, msg_struct, clientTCP):

        inst_number = int(msg_struct.instruction)

        if inst_number == constants.INST_MOTOR_STEP:
            print(":COMMAND>>stepping motor")
            self.motor.set_parameters(msg_struct.direction, "")
            self.motor.action_step(msg_struct, clientTCP)

        elif inst_number == constants.INST_MOTOR_FLASH_IMAGE:
            print(":COMMAND>>flashing image")
            self.motor.set_parameters(msg_struct.direction, msg_struct.img_file)
            self.motor.action_flash_image(msg_struct, clientTCP)

        elif inst_number == constants.INST_MOTOR_MOVE:
            print(":COMMAND>>moving motor")
            self.motor.set_parameters(msg_struct.direction, "")
            self.motor.action_move_distance_x(msg_struct, clientTCP)

        elif inst_number == constants.INST_MOTOR_STEP_IMAGE:
            print(":COMMAND>>stepping motor with image")
            self.motor.set_parameters(msg_struct.direction, msg_struct.img_file)
            self.motor.action_step_image(msg_struct, clientTCP)

        elif inst_number == constants.INST_MOTOR_STOP:
            print(":COMMAND>>stop motor")
            self.motor.stop()

        # else:
        #     raise NameError('invalid COMMAND')