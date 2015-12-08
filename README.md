# PiLEDs
PiLEDs is a basic python script to dynamically test GPIO outputs by sequentially toggling all specified GPIO pins

PiLEDs is named after LEDs, since that is the most common component used to test pinout. 

## Usage
Copy script anywhere, modify the pins specified in the script, and run with appropriate permissions

    sudo python PiLEDs.py

You can optionally pass in the pins as an argument -p, which bypasses the one defined inside the script
    sudo python PiLEDs.py -p 11 14 16 18
