import led
import time

print "Full IR LED Demo by Dennis Goldschmidt"

try:
    light = led.BrightPI(1)
    light.Reset();

    time.sleep(0.5);
    light.On(light.IR1);
    time.sleep(0.5);
    light.Off(light.IR1);
    
except IOError as io:
    print ("I/O Error ({0})".format(io));
    print " ex: sudo python demo.py"
