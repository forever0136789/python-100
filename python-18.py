from functools import reduce
num=int(input('被加数字：'))
n=int(input('加几次？'))
#存放加数
l=[]
a=0
for i in range(n):
    a+=num*(10**i)
    print(a)
    l.append(a)
he=reduce(lambda x,y:x+y,l)
print('和：%d'%he)
