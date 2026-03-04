#For use with the ADS1015
#Analog to digital conversion

import RPi.GPIO as GPIO

# Tell the GPIO library to use
# Broadcom GPIO references
GPIO.setmode(GPIO.BOARD)

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
  