//#include "mmapGpio.h"
#include "stdio.h"
#include "time.h"

int main(void){

	while (1) {// toggle pin as fast as possible
		printf("%d", rcTime(4));
	}

	return 0;
}

int rcTime(int PiPin){
	mmapGpio rpiGpio; // instantiate an instance of the mmapGpio class
	rpiGpio.setPinDir(PiPin, mmapGpio::OUTPUT); // set GPIO17 to output
	rpiGpio.writePinLow(PiPin); // set GPIO17 to output
	sleep(.5);

	rpiGpio.setPinDir(PiPin, mmapGpio::INPUT); // set GPIO17 to input
	// loop a counter until the PiPin is HIGH
	int counter = 0;
	while (rpiGpio.readPin(PiPin) != mmapGpio::HIGH)
		counter++;

	return counter;
}