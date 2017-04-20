import led
import time
import argparse

print "Full IR LED Demo by Dennis Goldschmidt"

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--freq", type=int, default=1,
	help="Frequency of blinking")
args = vars(ap.parse_args())

def blink(_led, freq=1):
    time.sleep(0.5/freq)
    _led.On(_led.IR1)
    time.sleep(0.5/freq)
    _led.Off(_led.IR1)

try:
    light = led.BrightPI(1)
    light.Reset();
    light.On(light.IR1)
    light.On(light.IR2)
    light.On(light.IR3)
    light.On(light.IR4)

    for i in range(32):
        light.setBrightness(light.IR1, i)
        light.setBrightness(light.IR2, i)
        light.setBrightness(light.IR3, i)
        light.setBrightness(light.IR4, i)
        time.sleep(1)

    while True:
        #blink(light, args["freq"])
        pass

except IOError as io:
    print ("I/O Error ({0})".format(io));
    print " ex: sudo python demo.py"
