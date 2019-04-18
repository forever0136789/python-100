#法一
l=[1,10,100,1000,10000,100000]
for i in range(len(l)//2):
    l[i],l[len(l)-1-i]=l[len(l)-1-i],l[i]
print(l)

#法二
l=[1,10,100,1000,10000,100000]
l.reverse()
print(l)
