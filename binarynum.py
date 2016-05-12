"""
Binary Number Manipulation
"""


class BinaryNum:

    def __init__(self, integer_val, si=1, wl=8, fl=0):
        """
            BinaryNum(integer_val)
            integer_val - An integer value that is valid for the specified wordlength
            si (optional default=1)- Signed (0 = unsigned 1 = signed) 
            wl (optional default=8) - WordLength (number of bits)
            fl  (optional default=0) - Fractional Length (where is the decimal point)
        """
        
        self.dec = integer_val
        self.si = si
        self.wl = wl
        self.fl = fl
        
        self.check()
        self.rwv = self.calc_rwv() #Real world value
        self.bin = self.to_bin()
        
    def check(self):
        """Check input arguments make sense"""
        
        # Check that sign is 1 or 0
        if not (self.si==0 or self.si==1):
            raise Exception("Sign must be 1 or 0")
        
        # Check that integer number can be represented in word length
        wl = self.wl
        max = 2**wl-1
        min = 0        
        
        if self.dec > max or self.dec <min:
            raise Exception("Integer value", self.dec, " must be between,", max,"and", min)

    def calc_rwv(self):
        """Calculate Real World Value"""
        
        rwv = float(self.dec)
        wl = self.wl
        fl = self.fl
        
        # Convert sign
        if self.si and self.dec > (2**(wl-1)-1):
            rwv =rwv-2**wl;
            
        # Divide by fractional length
        rwv = rwv/2**fl
        
        return (rwv)
    
    def to_bin(self):
        """Create Binary String from decimal value"""
        
        bin_value = bin(self.dec)[2:] # The 0b is dropped
        # Zero pad
        bin_value = '{:0>{}}'.format(bin_value,self.wl)
        
        return (bin_value)
        
    def slice(self, msb, lsb,  si=0,  fl=0):
        """Slice a range of bits from the result"""
        if msb < lsb:
            raise Exception("Msb ", msb, "must be greater than Lsb", lsb)
        if msb>self.wl-1:
            raise Exception("Msb ", msb, "must be less than wl-1",  self.wl-1)
            
        wl = msb-lsb+1
        bin_flip = self.bin[::-1]
        new_bin=bin_flip[lsb:msb+1]
        new_bin = new_bin[::-1]
        dec_new=int(new_bin, 2)
        bnew=BinaryNum(dec_new, si, wl, fl)
        
        return bnew
        
    def concat(b2, b1,  si=0,  fl=0):
        """
            Concatenate two BinaryNum objects. 
            This is the same behavior as the verilog concat operator
            {'1000','1010'} -> '100010101'
        """
        
        if not isinstance(b1, BinaryNum) or not isinstance(b2, BinaryNum):
            raise Exception("Inputs to concat must be of class BinaryNum")
        
        d2=b2.dec
        d1=b1.dec

        dnew = d2*(2**b1.wl)+d1
        wl_new = b2.wl+b1.wl;

        bnew=BinaryNum(dnew, si, wl_new, fl)
        return bnew
        
