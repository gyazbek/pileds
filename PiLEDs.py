# PiLEDs is free software; you can redistribute it as you wish and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PiLEDs is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# @author	gyazbek (github)
# @modified	dec 7, 2015
#
import argparse ## Import Argparse for argument parsing
import time	## Import time library for sleep functionality
import RPi.GPIO as GPIO ## Import GPIO library

## Use argparse to parse any arguments passed in
parser = argparse.ArgumentParser() 
parser.add_argument('-p',  nargs='+', type=int)
args = parser.parse_args()

## Change PINS to the ones you wish to test, or optionally use the -p argument
## i.e. -p 2 3 18
PINS = [11,16]

## If arguments for specifing the pins is passed in, we use them instead
if args.p:
	PINS = args.p
	print PINS, " pins passed for testing"
else:
	print "No PIN arguments specified, proceeding with the following: ", PINS


GPIO.setmode(GPIO.BOARD) ## Use board numbering

## Setup GPIOs for output
GPIO.setup(PINS, GPIO.OUT)

## Try/Catch to do proper cleanup on exit
try:
	## Infinite Loop while program is running
	while(True):
		## Itterate through PINS and toggle them on, wait 1 second, and off
		for PIN in PINS:
			GPIO.output(PIN,True) ## Turn on GPIO pin
			time.sleep(1)
			GPIO.output(PIN,False)
			time.sleep(1)

except:
	GPIO.cleanup()
