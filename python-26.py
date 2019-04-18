def f(n):
    return n*f(n-1) if n>1 else 1

print(f(5))
