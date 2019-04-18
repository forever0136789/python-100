#取x,y最大值
Max=lambda x,y:x*(x>=y)+y*(y>x)
Min=lambda x,y:x*(x<=y)+y*(y<x)

a=int(input('a:'))
b=int(input('b:'))

print(Max(a,b))
print(Min(a,b))
