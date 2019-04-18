#默认列表元素从小到大
la=[1,10,100,1000,10000,100000]
a=int(input('输入一个数：'))
la.append(a)
i=0
while i<(len(la)-1):
    if a<=la[i]:
        break
    else:
        i+=1
#列表中元素依次后移
for j in range(len(la)-2,i-1,-1):
        la[j+1]=la[j]
la[i]=a
print(la)
    
