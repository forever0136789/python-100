#a的集合存储a的可能对手
a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
a-=set('x')
c-=set(['x','z'])
for i in a:
    for j in b:
        for k in c:
            #判断i,j,k是否不同
            if len(set([i,j,k]))==3:
                print('a:%s,b:%s,c:%s'%(i,j,k))
