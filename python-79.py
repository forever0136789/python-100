#法一
l=['baaa','aaab','aaba','aaaa','abaa']
l.sort()
print(l)

#法二
str1 = input('input string:\n')
str2 = input('input string:\n')
str3 = input('input string:\n')
if str1 > str2 : str1,str2 = str2,str1
if str1 > str3 : str1,str3 = str3,str1
if str2 > str3 : str2,str3 = str3,str2
print(str1,str2,str3)
