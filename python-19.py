from functools import reduce
#存储完数
l=[]
#存储某数的因子,1必是因子
y={1}
for num in range(2,1000):
    for i in range(2,num):
        if num%i==0:
            y.add(i)
            y.add(num//i)
    if reduce(lambda a,b:a+b,y)==num:
        l.append(num)
    y={1}
print(l)
