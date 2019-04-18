a=809
for i in range(10,100):
    b=i*a
    #8*i最起码是两位数，9*i不会是4位数
    if b>=1000 and b<10000 and 8*i<100 and 9*i>=100:
        print(b,' = 800 * ', i, ' + 9 * ', i)
