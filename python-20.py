#记录每次落地前最高高度（上一次反弹高度）
h=100
#记录落地时经历路程
total=100
#i代表第i次落地
for i in range(2,11):
    h=h/2
    total+=2*h
print('共经过：%fm'%total)
print('第十次反弹：%fm'%(h/2))
