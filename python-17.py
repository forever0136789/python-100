string=input('请输入字符串：')
alp,dig,spa,oth=0,0,0,0
for i in range(len(string)):
    if string[i].isalpha():
        alp+=1
    elif string[i].isdigit():
        dig+=1
    elif string[i].isspace():
        spa+=1
    else:
        oth+=1
print('alpha:%d'%alp)
print('digit:%d'%dig)
print('space:%d'%spa)
print('other:%d'%oth)

