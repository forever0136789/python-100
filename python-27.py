#s字符串,字符位置
def output(num,s):
    if num==0:
        return 
    print(s[num-1])
    output(num-1,s)

s=input('输入字符：')
num=len(s)
output(num,s)
