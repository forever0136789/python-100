a,b=1,2
s=0
for i in range(20):
    s+=b/a
    a,b=b,a+b
print(s)
