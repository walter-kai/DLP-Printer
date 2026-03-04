# Walt Yao
# January 2015
from __future__ import print_function
__author__ = 'Yaoza'
import os
import constants
from xml.etree import ElementTree as ET
from devices.message_structure import message_structure

class XmlPresetsReader():
    def __init__(self):

        self.msg_struct_matrix = []

        # check if settings file exist
        if os.path.isfile(constants.PRESET_FILENAME):
            print("xml>> file ", constants.PRESET_FILENAME, " exists")
            self.tree = ET.parse(constants.PRESET_FILENAME)
            self.root = self.tree.getroot()
            self.extract_from_root()

        else:
            print("xml>> make new file")
            self.root = ET.Element("presets")
            # set settings defaults

        # for mat in self.msg_struct_matrix:
        #     mat[1].output_print()

    def save_to_file(self):
        print("xml>> rewrite new file")
        self.root = ET.Element("presets")
        # print("test", self.msg_struct_matrix)
        # msg_struct_tuple = self.msg_struct_matrix[len(self.msg_struct_matrix)-1]

        for msg_struct_tuple in self.msg_struct_matrix:

            preset = ET.SubElement(self.root, msg_struct_tuple[0])
            # print("loop", msg_struct_tuple)

            msg_struct = message_structure(msg_struct_tuple[1])
            #write
            attribute_element = ET.SubElement(preset, "instruction")
            attribute_element.text = msg_struct.instruction
            attribute_element = ET.SubElement(preset, "motor_id")
            attribute_element.text = msg_struct.motor_id
            attribute_element = ET.SubElement(preset, "distance")
            attribute_element.text = msg_struct.distance_travel
            attribute_element = ET.SubElement(preset, "direction")
            attribute_element.text = msg_struct.direction
            attribute_element = ET.SubElement(preset, "sensor")
            attribute_element.text = msg_struct.sensor_on
            attribute_element = ET.SubElement(preset, "resolution")
            attribute_element.text = msg_struct.resolution
            attribute_element = ET.SubElement(preset, "exposure_time")
            attribute_element.text = msg_struct.exposure_time
            attribute_element = ET.SubElement(preset, "img_file")
            attribute_element.text = msg_struct.img_file

        self.tree = ET.ElementTree(self.root)

        self.tree.write(constants.PRESET_FILENAME)
        print(constants.PRESET_FILENAME + " saved")


    def extract_from_root(self):
        # clear the matrix
        self.msg_struct_matrix = []
        # print("rpres:", self.root)

        for preset in self.root:
            # create the message struct and build it
            message = message_structure()
            msg_struct = []
            # print("preset tag:", preset.tag)
            msg_struct.append(preset.tag)
            for attribute in preset:
                # print("attribute:", attribute.tag)
                if attribute.tag == "instruction":
                    message.instruction = attribute.text
                elif attribute.tag == "motor_id":
                    message.motor_id = attribute.text
                elif attribute.tag == "distance":
                    message.distance_travel = attribute.text
                elif attribute.tag == "direction":
                    message.direction = attribute.text
                elif attribute.tag == "sensor":
                    message.sensor_on = attribute.text
                elif attribute.tag == "resolution":
                    message.resolution = attribute.text
                elif attribute.tag == "exposure_time":
                    message.exposure_time = attribute.text
                elif attribute.tag == "img_file":
                    message.img_file = attribute.text
            # join it to msg_struct
            # print("***Found preset in file")
            # message.output_print()
            msg_struct.append(message)
            # print msg_struct[0]
            self.msg_struct_matrix.append(msg_struct)

    def remove(self, index):
        # print("removing:" , index)
        # print("stuff in matrix", self.msg_struct_matrix[index][0])
        del self.msg_struct_matrix[index]
        self.save_to_file()

    def add(self, preset_name, message_struct):
        # print("adding", preset_name, message_struct.img_file)
        self.msg_struct_matrix.append([preset_name, message_struct])
        # print("checkmartrixadd=", self.msg_struct_matrix)

        self.save_to_file()

    def write(self, attribute, value):
        if self.new_file:
            attribute_element = self.root.find(attribute)
            if attribute_element is None:
                attribute_element = ET.SubElement(self.root, attribute)
            attribute_element.text = value

        else:
            attribute_element = ET.SubElement(self.root, attribute)
            attribute_element.text = value
            # wrap it in an ElementTree instance, and save as XML
            self.tree = ET.ElementTree(self.root)

        self.tree.write(self.filename)
        print(self.filename + " saved")

    def __len__(self):
        return len(self.msg_struct_matrix)

    def get_name(self, index):
        return self.msg_struct_matrix[index][0]

    def get(self, index):
        # print("getting",self.msg_struct_matrix[index][0], self.msg_struct_matrix[index][1])
        return self.msg_struct_matrix[index][1]

    def get_names(self):
        names = []
        # print("msg_struct:", self.msg_struct_matrix)
        for msg_struct in self.msg_struct_matrix:
            names.append(msg_struct[0])

        return names