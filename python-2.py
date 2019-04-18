i=int(input('当月利润：'))
arr=[100,60,40,20,10,0]
rat=[0.01,0.015,0.03,0.05,0.075,0.1]
#总提成
r=0
for idx in range(6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print('区间提成：%.4f 万元'%((i-arr[idx])*rat[idx]))
        i=arr[idx]
print('总提成：%.4f 万元'%r)
