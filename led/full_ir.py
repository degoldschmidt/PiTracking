import led
import time

print "Full IR LED Demo by Dennis Goldschmidt"

def blink(_led):
    time.sleep(0.5)
    _led.On(_led.IR1)
    time.sleep(0.5)
    _led.Off(_led.IR1)

try:
    light = led.BrightPI(1)
    light.Reset();

    blink(light)
    blink(light)
    blink(light)
    blink(light)
    blink(light)

except IOError as io:
    print ("I/O Error ({0})".format(io));
    print " ex: sudo python demo.py"
