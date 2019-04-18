l=[]
for i in range(10):
    a=int(input('输入一个数'))
    l.append(a)

num=len(l)
for i in range(num):
    for j in range(i,num):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
