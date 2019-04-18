from collections import *
#deque双向队列；两端都可以操作的序列，在序列的前后你都可以执行添加或删除操作。
la=[1,2,3,4,5,6,7,8,9]
deq=deque(la,maxlen=len(la))
print(la)
#把右边元素放在左边,参数为选右边的几个元素
deq.rotate(int(input('rotate:')))
print(list(deq))
