for i in range(4):
    for j in range(3-i):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    #换行
    print()

for i in range(3):
    for j in range(i+1):
        print(' ',end='')
    for j in range(5-2*i):
        print('*',end='')
    print()
