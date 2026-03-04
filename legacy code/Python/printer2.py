import numpy
import cv2
import time
import serial
import sys
import pyglet
import timeit

######### TODO ##########
# 1. Projector offsets.
# 2. Create cross section image. (DONE)
# 3. Spruce cross section.
# 4. Spruce cross section creation task.
# 5. Setting the linear table speed through firmware. (NOT NECESSARY)
# 6. Potentially controlling the resin pump. 
#########################

### CONFIGURATION ###
spruceSliceCount = 32
sliceCount = 32
sliceThickness = 200
delayMs = 1000
mainScreenWidth = 1920
projector1ScreenWidth = 1024
startPosition = sliceCount * sliceThickness
waitTime = 25
initialWaitTime = 600
sliceCounter = 0
#####################

### (assume sprocket is formed, TODO)
# 1. Initialize serial connection to arduino.
# 2. Initialize monitor connection to both projectors. (show blank)
# 3. Run sprew routine
# 4. Start print (repeat)
#   a. show slices 
#   b. delay 5000ms
#   c. show blank
#   d. move X and Y sliceSize (mm)
# 5. Close serial, set projector blank and waitKey(0), destroyallwindows
###

# 2.

# 1.
port = input("Type port number for arduino: ");
ser = serial.Serial()
ser.port = port - 1
ser.baudrate = 115200
ser.open()
time.sleep(2)

if ser.isOpen == False:
    print "error connecting to arduino"
    sys.exit()

print ""
start = timeit.timeit()
print"print started"
print ""

#restart = input("Move back to start? type 1 for yes")
#if(restart == 1):
#    command = "M" + str(startPosition) + " XY"
#    ser.write(command)
#    if "OK" in ser.readline(): 
#         print "move finished"
#    command = "M" + str(spruceSliceCount * sliceThickness) + "X"
#    ser.write(command)
#    if "OK" in ser.readline(): 
#        print "move finished"

#platform = pyglet.window.get_platform()
#display = platform.get_default_display()
#screen = display.get_screens()[1]
#print screen
#window = pyglet.window.Window(None, None, sys.argv[0], False, 0, True, True, True, display, screen, None, None)
#image = pyglet.resource.image('sprocket.jpg')
#@window.event
#def on_draw():
#    window.clear()
#    image.blit(0,0)
#pyglet.app.run()
print "Starting inital base slice"
time.sleep(initialWaitTime)
# 3.
print ""
print "Starting pre print cycle"
for i in range(0, spruceSliceCount):
    # a.
    # b.
    # d.
    command = "M" + str(-1 * sliceThickness) + " X"
    ser.write(command)
    sliceCounter += 1
    if "OK" in ser.readline():
        print "slice " + str(sliceCounter) + " finished"
    # c.
    time.sleep(waitTime)
    # 4.
print ""
print "starting main print cycle"
print ""
for i in range(0, sliceCount):
    # a.
    # b.
    # d
    command = "M" + str(-1 * sliceThickness) + " X" + "Y"
    ser.write(command)
    sliceCounter += 1
    if "OK" in ser.readline(): 
        print "slice " + str(sliceCounter) + " finished"
        
    # c.
    time.sleep(waitTime)
#5.
ser.close()
#window.close()
finishMessage = "print finished with " + str(sliceCount) + " slices at a slice thickness of " + str(abs(sliceThickness)) + " resulting in an object of length " + str(abs(sliceThickness) * sliceCount)
end = timeit.timeit()
seconds = end - start
minutes = seconds / 60
print "print took " + str(minutes) + " minutes or " + str(seconds)
print finishMessage





