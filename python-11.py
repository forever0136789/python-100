f1,f2=1,1
print('%d\t%d\t'%(f1,f2),end='')
for i in range(2,21):
    if i%3==0:
        print()
    f1,f2=f2,f1+f2
    print('%d\t'%f2,end='')
