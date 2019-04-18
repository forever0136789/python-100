n=int(input('输入游戏人数：\n'))
#记录每个人状态，1代表未被淘汰
num=[]
for i in range(n):
    num.append(1)
#存储游戏进行次数
i=0
#所报数字
k=0
#记录第几个人报数（从0开始）
m=0
#由于最后剩余1人，游戏最多玩n-1次
while i<n-1:
    #未淘汰才有资格报数
    if num[m]!=0:
        k+=1
    #判断是否该淘汰了
    if k==3:
        num[m]=0
        k=0
        i+=1
    m+=1
    #判断是否到了最后一人
    if m==n:
        m=0

m=0
while num[m]==0:
    m+=1
#实际中人的编号从1开始，故加一
print(m+1)
