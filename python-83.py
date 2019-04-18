#奇数总数
sum=0
s=0
#统计到7位数
for i in range(1,8):
    if i==1:
        s=4
        sum=4
    elif i==2:
        s=7*4
        sum+=s
    else:
        s=7*4*(8**(i-2))
        sum+=s
    print('%d位数有：%d个'%(i,s))
print('sum=',sum)
