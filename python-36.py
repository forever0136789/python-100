lower=int(input('输入区间最小值：'))
upper=int(input('输出区间最大值：'))
for num in range(lower,upper+1):
    if num==1:
        continue
    i=2
    while i<num:
        if num%i==0:
            break
        i+=1
    if i==num:
        print(num)
        
    
        
