# MODULE BY PIERRE MARTEL                           #
# brightpi.codeplex.com                             #
# Distribute under Microsoft Public License (MS-PL) #
# Beta Version 0.1                                  #

import smbus


class BrightPI:
    BrighPiAddress = 0x70;
    AddressControl = 0x00;
    AddressIR1  = 0x01;
    AddressLED1 = 0x02;
    AddressIR2  = 0x03;
    AddressLED2 = 0x04;
    AddressLED3 = 0x05;
    AddressIR3  = 0x06;
    AddressLED4 = 0x07;
    AddressIR4  = 0x08;
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

    def IR_1_On(self):
        try:
            mask = 0x01;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Activation ValueError : {0}".format(ve))

    def IR_1_Off(self):
        try:
            mask = ~0x01;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Deactivation ValueError : {0}".format(ve))


    def IR_1_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressIR1,level);
        except IOError as io:
            print ("Led 1 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Brightness ValueError : {0}".format(ve))

    def IR_2_On(self):
        try:
            mask = 0x03;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Activation ValueError : {0}".format(ve))

    def IR_2_Off(self):
        try:
            mask = ~0x03;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Deactivation ValueError : {0}".format(ve))


    def IR_2_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressIR2,level);
        except IOError as io:
            print ("Led 1 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Brightness ValueError : {0}".format(ve))

    def IR_3_On(self):
        try:
            mask = 0x06;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Activation ValueError : {0}".format(ve))

    def IR_3_Off(self):
        try:
            mask = ~0x06;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Deactivation ValueError : {0}".format(ve))


    def IR_3_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressIR3,level);
        except IOError as io:
            print ("Led 1 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Brightness ValueError : {0}".format(ve))

    def IR_4_On(self):
        try:
            mask = 0x08;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Activation ValueError : {0}".format(ve))

    def IR_4_Off(self):
        try:
            mask = ~0x08;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Deactivation ValueError : {0}".format(ve))


    def IR_4_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressIR4,level);
        except IOError as io:
            print ("Led 1 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Brightness ValueError : {0}".format(ve))

    def Led_1_On(self):
        try:
            mask = 0x02;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Activation ValueError : {0}".format(ve))

    def Led_1_Off(self):
        try:
            mask = ~0x02;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 1 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Deactivation ValueError : {0}".format(ve))


    def Led_1_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressLED1,level);
        except IOError as io:
            print ("Led 1 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 1 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 1 Brightness ValueError : {0}".format(ve))

    def Led_2_On(self):
        try:
            mask = 0x08;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 2 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 2 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 2 Activation ValueError : {0}".format(ve))


    def Led_2_Off(self):
        try:
            mask = ~0x08;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 2 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 2 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 2 Deactivation ValueError : {0}".format(ve))

    def Led_2_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressLED2,level);
        except IOError as io:
            print ("Led 2 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 2 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 2 Brightness ValueError : {0}".format(ve))

    def Led_3_On(self):
        try:
            mask = 0x10;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 3 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 3 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 3 Activation ValueError : {0}".format(ve))

    def Led_3_Off(self):
        try:
            mask = ~0x10;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 3 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 3 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 3 Deactivation ValueError : {0}".format(ve))

    def Led_3_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressLED3,level);
        except IOError as io:
            print ("Led 3 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 3 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 3 Brightness ValueError : {0}".format(ve))

    def Led_4_On(self):
        try:
            mask = 0x40;
            result = self.readState(self.AddressControl) | mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 4 Activation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 4 Activation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 4 Activation ValueError : {0}".format(ve))


    def Led_4_Off(self):
        try:
            mask = ~0x40;
            result = self.readState(self.AddressControl) & mask;
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressControl,result);
        except IOError as io:
            print ("Led 4 Deactivation IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 4 Deactivation TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 4 Deactivation ValueError : {0}".format(ve))

    def Led_4_Brightness(self, level):
        try:
            self.bus.write_byte_data(self.BrighPiAddress,self.AddressLED4,level);
        except IOError as io:
            print ("Led 4 Brightness IOError : {0}".format(io))
        except TypeError as te:
            print ("Led 4 Brightness TypeError : {0}".format(te))
        except ValueError as ve:
            print ("Led 4 Brightness ValueError : {0}".format(ve))

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
