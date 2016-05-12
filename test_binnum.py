import binarynum as bn

b1 = bn.BinaryNum(342, 1, 10, 0)

print(b1.rwv, b1.bin)

b2 = b1.slice(4, 1, 1)
print(b2.bin, b2.rwv)

b3 = bn.BinaryNum.concat(b2, b1)
print(b3.bin, b3.rwv, b3.wl, b2.wl, b1.wl)


b4 = bn.BinaryNum(342, 1, 10, 10)
print(b4.rwv, b4.fl)
