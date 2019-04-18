year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))
months=[0,31,59,90,120,151,181,212,243,273,304,334]
#判断是否为闰年
if year%400==0 or year%4==0 and year%100!=0:
    months[2]=60
sum=months[month-1]+day
print('第%d天'%sum)
