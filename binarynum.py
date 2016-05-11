"""
Binary Number Manipulation
"""


class BinaryNum:

    def __init__(self, integer_val, si=1, wl=8, fl=0):
        
        self.dec = integer_val
        self.si = si
        self.wl = wl
        self.fl = fl
        
        self.check_limit()
        self.rwv = self.calc_rwv() #Real world value
        self.bin = self.to_bin()
        
    def check_limit(self):
        """Check that integer number can be represented in word length"""
        wl = self.wl
        max = 2**wl-1
        min = 0        
        
        if self.dec > max or self.dec <min:
            raise Exception("Integer value", self.dec, " must be between,", max,"and", min)

    def calc_rwv(self):
        """Calculate Real World Value"""
        
        rwv = self.dec
        wl = self.wl
        fl = self.fl
        
        # Convert sign
        if self.si and self.dec > (2**(wl-1)-1):
            rwv =rwv-2**wl;
            
        # Divide by fractional length
        rwv = rwv/2**fl
        
        return (rwv)
    
    def to_bin(self):
        bin_value = bin(self.dec)[2:] # The 0b is dropped
        # Zero pad
        bin_value = '{:0>{}}'.format(bin_value,self.wl)
        
        return (bin_value)
        
    def bit_get(self, msb, lsb):
        """Slice a range of bits from the result"""
        if msb < lsb:
            raise Exception("Msb ", msb, "must be greater than Lsb", lsb)
        
        self.dec
