#除数
b=int(input('输入一数：'))
#记录被除数中9的个数
num=1
#被除数
a=9
while a%b!=0:
    a=10*a+9
    num+=1
print('%d个9可以被%d整除'%(num,b))
print('%d/%d=%d'%(a,b,a/b))
