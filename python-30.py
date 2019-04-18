n=input('输入五位数：')
i=0
j=len(n)-1
#标志位，为真代表是回文数
flag=True
while i<j:
    if n[i]!=n[j]:
        flag=False
        print('不是回文数')
        break
    i+=1
    j-=1
if flag==True:
    print('是回文数')

