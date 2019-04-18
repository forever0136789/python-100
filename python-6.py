def fib(n):
    if n==1 or n==2:
        return 1
    a,b=1,1
    for i in range(2,n):
        a,b=b,a+b
    return b
print(fib(10))

#递归
def fib1(n):
    if n==1 or n==2:
        return 1
    return fib1(n-1)+fib1(n-2)
print(fib1(10))

#输出前10个数
def fib2(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    f=[1,1]
    for i in range(2,n):
        f.append(f[-1]+f[-2])
    return f
print(fib2(10))
