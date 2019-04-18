la=[3,2,5,7,8,1,5]
#取出最大值的下标
m=la.index(max(la))
la[0],la[m]=la[m],la[0]
#取出最小值
i=la.index(min(la))
la[-1],la[i]=la[i],la[-1]
print(la)
