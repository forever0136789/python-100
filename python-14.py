#存放各质数
l=[]
n=int(input('输入一正整数：'))
if n==1:
    print(n)
#用n的副本，不改变n
m=n
i=2
while i<=m:
    if i==m:
        l.append(i)
        break
    elif m%i==0:
        l.append(i)
        m=int(m/i)
        i=2
    else:
        i+=1
print('%d=%s'%(n,'*'.join([str(i) for i in l])))
