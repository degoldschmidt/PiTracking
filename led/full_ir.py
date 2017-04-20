import led
import time
import argparse

print("Full IR LED Demo by Dennis Goldschmidt")

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--freq", type=int, default=1,
	help="Frequency of blinking")
ap.add_argument("-ir", "--ir", nargs='*', help="IR Channels to use")
args = vars(ap.parse_args())

IR1  = 0x01;
LED1 = 0x02;
IR2  = 0x03;
LED2 = 0x04;
LED3 = 0x05;
IR3  = 0x06;
LED4 = 0x07;
IR4  = 0x08;
AddressAllLed  = 0x09;

"""
def blink(_led, freq=1):
    time.sleep(0.5/freq)
    _led.On(_led.IR1)
    time.sleep(0.5/freq)
    _led.Off(_led.IR1)
"""

try:
    light = led.BrightPI(1)
    light.Reset()
    light.IR_All_On()
    """
    for i in range(32):
        print("Brightness level ->", i)
        light.setBrightness(IR1, i)
        light.setBrightness(IR2, i)
        light.setBrightness(IR3, i)
        light.setBrightness(IR4, i)
        time.sleep(1)
    """
    while True:
        #blink(light, args["freq"])
        pass

except IOError as io:
    print ("I/O Error ({0})".format(io))
    print (" ex: sudo python demo.py")
