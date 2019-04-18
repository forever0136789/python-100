a = int(input('input a number:'))
b = a >> 4
#bin取二进制
print('a右移四位：',bin(b))
print('~0:',~0)
print('~0<<4',bin(~0<<4))
c = ~(~0 << 4)
d = b & c
print('d:',d)
