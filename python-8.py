for i in range(1,10):
    for j in range(1,i+1):
        #print默认换行，end参数置空则不换行
        print('%d * %d = %d\t'%(i,j,i*j),end='')
    print('\n')
