import numpy
import cv2
import time
import serial
import sys
import pyglet

######### TODO ##########
# 1. Projector offsets.
# 2. Create cross section image. (DONE)
# 3. Spruce cross section.
# 4. Spruce cross section creation task.
# 5. Setting the linear table speed through firmware. (NOT NECESSARY)
# 6. Potentially controlling the resin pump. 
#########################

### CONFIGURATION ###
spruceSliceCount = 1
sliceCount = 5
sliceThickness = 250
delayMs = 1000
mainScreenWidth = 1920
projector1ScreenWidth = 1024
startPosition = sliceCount * sliceThickness
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
cv2.namedWindow("1", cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty("1", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
cv2.namedWindow("2", cv2.WND_PROP_FULLSCREEN)          
cv2.setWindowProperty("2", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)

img = cv2.imread("blank.jpg")
cv2.imshow("1",img)
cv2.moveWindow("1", mainScreenWidth, 0)
cv2.waitKey(1)

img1 = cv2.imread("blank.jpg")
cv2.imshow("2",img1)
cv2.moveWindow("2", mainScreenWidth + projector1ScreenWidth, 0)
cv2.waitKey(1)

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

restart = input("Move back to start? type 1 for yes")
if(restart == 1):
    command = "M" + str(startPosition) + " XY"
    ser.write(command)
    if "OK" in ser.readline(): 
         print "move finished"
    command = "M" + str(spruceSliceCount * sliceThickness) + "X"
    ser.write(command)
    if "OK" in ser.readline(): 
        print "move finished"

# 3.
for i in range(0, spruceSliceCount):
    # a.
    img = cv2.imread("square.jpg")
    cv2.imshow("1",img)
    cv2.moveWindow("1", mainScreenWidth, 0)
    cv2.waitKey(1)
    img1 = cv2.imread("square.jpg")
    cv2.imshow("2",img1)
    cv2.moveWindow("2", mainScreenWidth + projector1ScreenWidth, 0)
    # b.
    cv2.waitKey(delayMs)
    # d.
    command = "M" + str(-1 * sliceThickness) + " X"
    ser.write(command)
    if "OK" in ser.readline(): 
        print "move finished"
    # c.
    img = cv2.imread("blank.jpg")
    cv2.imshow("1",img)
    cv2.moveWindow("1", mainScreenWidth, 0)
    cv2.waitKey(1)
    img1 = cv2.imread("blank.jpg")
    cv2.imshow("2",img1)
    cv2.moveWindow("2", mainScreenWidth + projector1ScreenWidth, 0)
    cv2.waitKey(delayMs)

# 4.
for i in range(0, sliceCount):
    # a.
    img = cv2.imread("square.jpg")
    cv2.imshow("1",img)
    cv2.moveWindow("1", mainScreenWidth, 0)
    cv2.waitKey(1)
    img1 = cv2.imread("square.jpg")
    cv2.imshow("2",img1)
    cv2.moveWindow("2", mainScreenWidth + projector1ScreenWidth, 0)
    # b.
    cv2.waitKey(delayMs)
    # d.
    command = "M" + str(-1 * sliceThickness) + " X" + "Y"
    ser.write(command)
    if "OK" in ser.readline(): 
        print "move finished"
    # c.
    img = cv2.imread("blank.jpg")
    cv2.imshow("1",img)
    cv2.moveWindow("1", mainScreenWidth, 0)
    cv2.waitKey(1)
    img1 = cv2.imread("blank.jpg")
    cv2.imshow("2",img1)
    cv2.moveWindow("2", mainScreenWidth + projector1ScreenWidth, 0)
    cv2.waitKey(delayMs)

#5.
ser.close()

img = cv2.imread("blank.jpg")
cv2.imshow("1",img)
cv2.moveWindow("1", mainScreenWidth, 0)
cv2.waitKey(1)
img1 = cv2.imread("blank.jpg")
cv2.imshow("2",img1)
cv2.moveWindow("2", mainScreenWidth + projector1ScreenWidth, 0)
print "power down projectors and hit 'enter' to continue"
cv2.waitKey(delayMs)
cv2.destroyAllWindows()

finishMessage = "print finished with " + str(sliceCount) + " slices at a slice thickness of " + str(abs(sliceThickness)) + " resulting in an object of length " + str(abs(sliceThickness) * sliceCount)
print finishMessage





