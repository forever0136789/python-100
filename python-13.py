for n in range(100,1000):
    #获取n的百位数字
    i=int(n/100)
    #获取n的十位数字
    j=int(n/10) %10
    #获取n的个位数字
    k=n%10
    if n==i**3+j**3+k**3:
        print(n)
    
