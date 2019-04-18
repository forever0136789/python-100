#num代表行数
def yhsj(num):
    r=[[1]]
    for i in range(1,num):
        r.append(list(map((lambda x,y:x+y),[0]+r[-1],r[-1]+[0])))
    return r

a=yhsj(10)
for i in a:
    print(i)
