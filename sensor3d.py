import smbus
import binarynum as bn

class Sensor3D:


    def __init__(self, addr):
        self.addr = addr
        
        self.i2c = smbus.SMBus(1)
        self.x=0
        self.y=0
        self.x=0       
        
    def read_angle(self):
        
        try:
            data = self.i2c.read_i2c_block_data(0x60,0x28,8)
        except:
            print("I2C Read Failed!")
            data = [0, 0, 0, 0, 0, 0, 0, 0]
        
        self.xyz = self.parse_xyz(data)
        
    def parse_xyz(self, data):
        
        # Slice the bits from the 8 bytes of data
        
        msb_x = bn.BinaryNum(data[0], 0, 8)
        msb_y = bn.BinaryNum(data[1], 0, 8)
        msb_z = bn.BinaryNum(data[2], 0, 8)
        
        #lsb_b3 = bn.BinaryNum(data[4], 0, 8)
        lsb_b2 = bn.BinaryNum(data[5], 0, 8)
        lsb_b1 = bn.BinaryNum(data[6], 0, 8)
        #lsb_b0 = bn.BinaryNum(data[7], 0, 8)
        
        lsb_x = lsb_b2.slice(3, 0)
        lsb_y = lsb_b1.slice(7, 4)
        lsb_z = lsb_b1.slice(3, 0)
        
        #Concat the results
        self.x = bn.BinaryNum.concat(msb_x, lsb_x, 1, 12).rwv
        self.y = bn.BinaryNum.concat(msb_y, lsb_y, 1, 12).rwv
        self.z = bn.BinaryNum.concat(msb_z, lsb_z, 1, 12).rwv
        
    def __str__(self):
        str1 = 'x='+str(self.x)+' y='+str(self.y)+' z='+str(self.z)
        return str1 
