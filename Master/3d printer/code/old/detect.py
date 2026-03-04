#!/usr/bin/env python2.7  
# demo of "BOTH" bi-directional edge detection  
# script by Alex Eames http://RasPi.tv  
# http://raspi.tv/?p=6791  

from Adafruit_ADS1x15 import ADS1x15
from time import sleep     # this lets us have a time delay (see line 12)

import sys
sys.path.insert(0, '/3d printer/scripts/adafruit/Adafruit_ADS1x15')




pga = 6144
sps = 8
adc = ADS1x15(ic=0x00)


print "When pressed, you'll see: Rising Edge detected on 18"
print "When released, you'll see: Falling Edge detected on 18"
while True:
   print "reading: %d" % adc.readADCSingleEnded(0, pga, sps)
   sleep(0.25)         # wait 30 seconds
print "Time's up. Finished!"

