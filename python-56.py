from tkinter import *
#指定canvas组件宽度、高度、背景色
canvas=Canvas(width=800,height=600,bg='yellow')
#将canvas添加到主窗口
canvas.pack(expand=YES,fill=BOTH)
k=1
j=1
for i in range(26):
    canvas.create_oval(310-k,250-k,310+k,250+k,width=1)
    k+=j
    j+=0.3
#让以上工作起来
mainloop()
