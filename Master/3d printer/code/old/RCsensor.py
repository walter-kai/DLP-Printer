#!/usr/local/bin/python

# Reading an analogue sensor with
# a single GPIO pin

# Author : Matt Hawkins
# Distribution : Raspbian
# Python : 2.7
# GPIO   : RPi.GPIO v3.1.0a

import RPi.GPIO as GPIO, time, datetime, timeit

# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BCM)

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

# Define function to measure charge time
def RCtime (PiPin):
  measurement = 0
  # Discharge capacitor
  GPIO.setup(PiPin, GPIO.OUT)
  GPIO.output(PiPin, GPIO.LOW)
  time.sleep(.5)

  GPIO.setup(PiPin, GPIO.IN)

  waitSigWrapper = wrapper(WaitSignalHigh, PiPin)
  totTime = timeit.timeit(waitSigWrapper, number=1)
  # Count loops until voltage across
  # capacitor reads high on GPIO
  
  return totTime

def WaitSignalHigh (PiPin):
	while True:
		if(GPIO.input(PiPin) == GPIO.HIGH):
			break
	return

  
# Main program loop
while True:
	 
	print RCtime(4)
  