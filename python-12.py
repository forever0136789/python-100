from math import sqrt
#素数数量
num=0
#为1是=时代表是素数(默认是素数)
status=1
for i in range(101,200,2):
    k=int(sqrt(i+1))
    for j in range(2,k+1):
        if i%j==0:
            status=0
            break
    if status==1:
        num+=1
        print(i)
    status=1
        
print('素数有：%d个'%num)
