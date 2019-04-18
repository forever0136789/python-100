for i in range(2,85):
    #保证j为整数
    if 168%i==0:
        j=168/i
        #保证m,n均为整数
        if i>j and (i+j)%2==0 and (i-j)%2==0:
            m=(i+j)/2
            n=(i-j)/2
            x=n*n-100
            print(x)
