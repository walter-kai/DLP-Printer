# Walt Yao
# December 2014
from __future__ import print_function

class message_structure:
    def __init__(self, copy=None):

        if copy == None:
            self.instruction = ""
            self.motor_id = ""
            self.distance_travel = ""
            self.direction = ""
            self.sensor_on = ""
            self.img_file = ""

            # optional
            self.resolution = ""
            self.exposure_time = ""

        else:
            self.instruction = copy.instruction
            self.motor_id = copy.motor_id
            self.distance_travel = copy.distance_travel
            self.direction = copy.direction
            self.sensor_on = copy.sensor_on
            self.img_file = copy.img_file
            # optioncopy.
            self.resolution = copy.resolution
            self.exposure_time = copy.exposure_time

    def output_print(self):
        print(":message>>STRUCTURE PRINTOUT")
        print(":message>>instruction:", self.instruction)
        print(":message>>motor_id:", self.motor_id)
        print(":message>>distance:", self.distance_travel)
        print(":message>>direction:", self.direction)
        print(":message>>sensor?:", self.sensor_on)
        print(":message>>resolution:", self.resolution)
        print(":message>>exposure time:", self.exposure_time)
        print(":message>>img file:", self.img_file)
        print(":message>>")

    def encode(self):
        message = "#" + ",".join([self.motor_id, str(self.instruction), self.distance_travel, str(self.direction), self.sensor_on, self.resolution, self.exposure_time, self.img_file])
        message = message + "!"
        print(":msg_struct>>", message)
        return message

    def decode(self, in_string):
        # example string
        # AB,C,D,E,[F],[G!
        # A = # is an instruction, @ is feedback
        # B = motor id
        # C = instruction
        # D = distance
        # E = direction
        # F = sensor on/off
        # G = resolution
        # H = exposure time

        print("Received str:", in_string)
        if (in_string[0] == "#" or in_string[0] == "@") and in_string[len(in_string)-1] == "!":
            # chop off the #
            in_string = in_string[1:-1]
            argv = in_string.split(",")
            if len(argv) > 0:
                self.motor_id = argv.pop(0)
            if len(argv) > 0:
                self.instruction = argv.pop(0)
            if len(argv) > 0:
                self.distance_travel = argv.pop(0)
            if len(argv) > 0:
                self.direction = int(argv.pop(0))
            if len(argv) > 0:
                self.sensor_on = argv.pop(0)
            if len(argv) > 0:
                self.resolution = argv.pop(0)
            if len(argv) > 0:
                self.exposure_time = argv.pop(0)
            if len(argv) > 0:
                self.img_file = argv.pop(0)
        else:
            print("invalid command:", in_string)
