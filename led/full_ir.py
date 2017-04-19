import led
import time

print "Full IR LED Demo by Dennis Goldschmidt"

try:
    light = led.BrightPI(1)
    light.Reset();
    for times in range(100):
        light.blink(light.IR1, 1)
except IOError as io:
    print ("I/O Error ({0})".format(io));
    print " ex: sudo python demo.py"
