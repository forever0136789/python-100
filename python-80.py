#最小能被四整除的数是4
x=4
i=0
j=1
#找j,i计次（保证5个x均是4的倍数）
while i<5:   
    if x%4!=0:
        i=0
        j+=1
        x=4*j
        continue
    else:
        i+=1
        x=x/4*5+1    
print(x)

