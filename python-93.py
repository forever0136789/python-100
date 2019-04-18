import time
#浮点数计算的秒数返回当前的CPU时间。
#用来衡量不同程序的耗时，比time.time()更有用。
start = time.clock()
for i in range(100):
    print(i)
end = time.clock()
print('different is %6.3f' % (end - start))
