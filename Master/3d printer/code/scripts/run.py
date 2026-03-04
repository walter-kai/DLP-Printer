# Walt Yao
# January 2015

#importing wx files
import wx
import constants

#import the newly created GUI file
import gui.gui as gui

from communicationThread import *

#importing 3d printer stuff
from devices.message_structure import message_structure
from devices.xmlPresetsReader import XmlPresetsReader

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class MainWindow(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)

        # initialize preset
        self.XmlPresetsReader = XmlPresetsReader()
        names = self.XmlPresetsReader.get_names()
        if len(names) > 0:
            for name in names:
                self.combobox_presets.Append(name)

        # setup tcp connection
        # don't start this until you have the slaves up or else you'll hang here
        self.com_thread1 = CommunicationThread(1)
        self.com_thread2 = CommunicationThread(2)
        self.com_thread1.start()
        self.com_thread2.start()

        self.resolution.SetValue('100')
        self.exposure.SetValue('1')
        self.distance.SetValue('0.1')

        self.combobox_selection = 0

        self.process_time()
        self.image_file.SetPath("/home/pi/3d printer/code/scripts/devices/images/hand.png")

    def set_fields(self, message_struct):
        # message_struct.output_print()

        self.instruction.SetSelection(int(message_struct.instruction))
        self.resolution.SetValue(message_struct.resolution)
        self.exposure.SetValue(message_struct.exposure_time)
        self.distance.SetValue(message_struct.distance_travel)
        self.direction.SetSelection(int(message_struct.direction))

        if message_struct.motor_id == "0":
            self.motor_left.SetValue(False)
            self.motor_right.SetValue(False)
            self.motor_both.SetValue(True)
        elif message_struct.motor_id == "1":
            self.motor_left.SetValue(False)
            self.motor_right.SetValue(True)
            self.motor_both.SetValue(False)
        if message_struct.motor_id == "2":
            self.motor_left.SetValue(True)
            self.motor_right.SetValue(False)
            self.motor_both.SetValue(False)

        # print("sensor_on:", message_struct.sensor_on)
        if message_struct.sensor_on == "y":
            self.sensor_on.SetValue(True)
        else:
            self.sensor_on.SetValue(False)

        self.image_file.SetPath(message_struct.img_file)

        self.process_time()
        # self.image_file.SetPath("/home/pi/3d printer/code/scripts/devices/images/hand.png")

    def build_message_structure(self):

        msg_struct = message_structure()
        msg_struct.img_file = self.image_file.GetPath()

        if self.motor_both.GetValue():
            msg_struct.motor_id = "0"
        elif self.motor_right.GetValue():
            msg_struct.motor_id = "1"
        elif self.motor_left.GetValue():
            msg_struct.motor_id = "2"

        msg_struct.direction = str(self.direction.GetSelection())

        if self.sensor_on.GetValue():
            msg_struct.sensor_on = "y"
        else:
            msg_struct.sensor_on = "n"

        # now populate the msg_struct
        msg_struct.instruction = str(self.instruction.GetSelection())

        msg_struct.distance_travel = self.distance.GetValue()

        msg_struct.resolution = self.resolution.GetValue()
        msg_struct.exposure_time = self.exposure.GetValue()

        return msg_struct

    def process_time(self):
        # print 'rpcessing'
        distance = self.distance.GetValue()
        resolution = self.resolution.GetValue()
        exposure = self.exposure.GetValue()
        if len(distance) > 0 and len(resolution) > 0 and len(exposure) > 0 and int(resolution) > 0:
            #evaluate the string in 'text' and put the answer back.0
            distance_microns = float(distance) * 10000
            number_clicks = distance_microns / int(resolution)
            total_seconds = int(number_clicks * float(exposure))

            total_mins = int(total_seconds / 60)

            self.total_time.SetValue(str(total_mins) + " minutes, " + str(total_seconds % 60) + " seconds")

    # load preset
    def preset_load( self, event ):
        # print("load preset", self.combobox_presets.GetSelection())
        self.set_fields(self.XmlPresetsReader.get(self.combobox_presets.GetSelection()))

    # delete preset
    def preset_delete( self, event ):
        preset_name = self.combobox_presets.GetValue()
        if len(preset_name) > 0:

            selection = self.combobox_presets.GetSelection()
            if selection >= 0:
                self.combobox_selection = selection

            if self.combobox_selection >= len(self.XmlPresetsReader):
                self.combobox_selection -= 1

            print("my selection is:", self.combobox_selection)

            self.XmlPresetsReader.remove(self.combobox_selection)
            self.combobox_presets.Delete(self.combobox_selection)

            if self.combobox_selection >= len(self.XmlPresetsReader):
                self.combobox_selection -= 1

            self.set_fields(self.XmlPresetsReader.get(self.combobox_selection))
            self.combobox_presets.SetValue(self.XmlPresetsReader.get_name(self.combobox_selection))



    # save preset
    def preset_save(self, event ):

        preset_name = self.combobox_presets.GetValue()

        if len(preset_name) > 0:
            if not preset_name[0].isdigit():
                message_structure = self.build_message_structure()
                self.XmlPresetsReader.add(preset_name, message_structure)

                self.combobox_presets.Append(preset_name)
                self.combobox_presets.SetValue("")

    # set the sensor reading to the limit value
    def sensor_calibrate_in( self, event ):
        print("CALIBRATE IN")
        message_structure = self.build_message_structure()
        message_structure.instruction = str(constants.INST_SENSOR_CALIBRATE_IN)
        self.com_thread1.socket_port.write(message_structure.encode())
        self.com_thread2.socket_port.write(message_structure.encode())

    def sensor_calibrate_out(self, event ):
        print("CALIBRATE OUT")
        message_structure = self.build_message_structure()
        message_structure.instruction = str(constants.INST_SENSOR_CALIBRATE_OUT)
        self.com_thread1.socket_port.write(message_structure.encode())
        self.com_thread2.socket_port.write(message_structure.encode())

    def calculate_time(self,event):
        self.process_time()

    def stop_printer(self, event ):
        print("STOP")
        message_structure = self.build_message_structure()
        message_structure.instruction = str(constants.INST_MOTOR_STOP)
        self.com_thread1.socket_port.write(message_structure.encode())
        self.com_thread2.socket_port.write(message_structure.encode())


    def execute_printer(self, event):

        message_structure = self.build_message_structure()
        print("EXECUTING PRINTER")
        message_structure.output_print()
        self.com_thread1.socket_port.write(message_structure.encode())
        self.com_thread2.socket_port.write(message_structure.encode())

    #what to when 'Solve' is clicked
    #wx calls this function with and 'event' object
    #put a blank string in text when 'Clear' is clicked
    def clearFunc(self,event):
        self.total_time.SetValue(str(''))

#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)

#create an object of CalcFrame
frame = MainWindow(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()