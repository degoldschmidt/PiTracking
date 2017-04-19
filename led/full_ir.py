import led
import time

print "Full IR LED Demo by Dennis Goldschmidt"

try:
    light = led.BrightPI(1)
    light.Reset();
    light.IR_1_On();
    time.sleep(0.5);
    light.IR_2_On();
    time.sleep(0.5);
    light.IR_3_On();
    time.sleep(0.5);
    light.IR_4_On();
    time.sleep(0.5);
    light.IR_4_Off();
    time.sleep(0.5);
    light.IR_3_Off();
    time.sleep(0.5);
    light.IR_2_Off();
    time.sleep(0.5);
    light.IR_1_Off();
    time.sleep(0.5);
    light.Led_All_Off();
except IOError as io:
    print ("I/O Error ({0})".format(io));
    print " ex: sudo python demo.py"
