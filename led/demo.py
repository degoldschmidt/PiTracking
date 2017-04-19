import led
import time

print "BrightPI Demo by Pierre Martel"

try:
    light = BrightPILed.BrightPI(1)
    light.Reset();
    light.Led_1_On();
    time.sleep(0.5);
    light.Led_2_On();
    time.sleep(0.5);
    light.Led_3_On();
    time.sleep(0.5);
    light.Led_4_On();
    time.sleep(0.5);
    light.Led_4_Off();
    time.sleep(0.5);
    light.Led_3_Off();
    time.sleep(0.5);
    light.Led_2_Off();
    time.sleep(0.5);
    light.Led_1_Off();
    time.sleep(0.5);
    light.Led_All_On();
    time.sleep(0.5);
    for x in range(0, 15):
        light.Led_All_Brightness(x);
        time.sleep(0.1);
    light.Led_All_Off();
except IOError as io:
    print ("I/O Error ({0})".format(io));
    print " ex: sudo python demo.py"
