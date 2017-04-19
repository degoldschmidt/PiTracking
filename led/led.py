# MODULE BY PIERRE MARTEL                           #
# brightpi.codeplex.com                             #
# Distribute under Microsoft Public License (MS-PL) #
# Beta Version 0.1                                  #

import smbus
import time


class BrightPI:
    BrighPiAddress = 0x70;
    AddressControl = 0x00;
    IR1  = 0x01;
    LED1 = 0x02;
    IR2  = 0x03;
    LED2 = 0x04;
    LED3 = 0x05;
    IR3  = 0x06;
    LED4 = 0x07;
    IR4  = 0x08;
    AddressAllLed  = 0x09;
    maxBrightness = 0x32;

    def __init__(self,I2CPORT_value):
        try:
            self.I2CPORT = I2CPORT_value
            self.bus = smbus.SMBus(self.I2CPORT)
        except ValueError:
            print ("BrightPI initialization error")

    def readState(self, address):
            return self.bus.read_byte_data(self.BrighPiAddress, address);

    def Blink(self, address, freq):
        self.On(address)
        time.sleep(1/freq)
        self.Off(address)
        time.sleep(1/freq)

    def On(self, address):
        try:
            mask = address;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Activation ValueError : {0}".format(ve))

    def Off(self, address):
        try:
            mask = address;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Deactivation ValueError : {0}".format(ve))


    def setBrightness(self, address, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress, address, level);
        except IOError as io:
            print ("Led 1 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Brightness ValueError : {0}".format(ve))

    def Led_All_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressAllLed,level);
        except IOError as io:
            print ("All Led Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("All Led Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("All Led Brightness ValueError : {0}".format(ve))

    def Led_All_On(self):
        try:
            mask = 0x5a;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("All Led On Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("All Led On Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("All Led On Brightness ValueError : {0}".format(ve))

    def Led_All_Off(self):
        try:
            mask = ~0x5a;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("All Led Off Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("All Led Off Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("All Led Off Brightness ValueError : {0}".format(ve))

    def Reset(self):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,0x00);
        except IOError as io:
            print ("Reset IOError : {0}".format(io))
        except TypeError as te:
            print ("Reset TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Reset ValueError : {0}".format(ve))
