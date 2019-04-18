#全局变量
num = 2
def autofunc():
    #局部变量，作用域只在函数内
    num = 1
    print ('internal block num = %d' % num)
    num += 1
for i in range(3):
    print ('The num = %d' % num)
    num += 1
    autofunc()
