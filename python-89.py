s=input('输入一四位数：')
a=[]
for i in range(4):
    a.append((int(s[i])+5)%10)
a[0],a[3]=a[3],a[0]
a[1],a[2]=a[2],a[1]
print(''.join([str(x) for x in a]))
