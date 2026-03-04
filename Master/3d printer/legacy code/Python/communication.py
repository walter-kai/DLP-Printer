import serial
import time

ser = serial.Serial()
ser.port = 6
ser.baudrate = 115200

ser.open()
time.sleep(2)

print ser.write("X-1000 Y-1000")

if "OK" in ser.readline(): 
    print "ok"
ser.close()
