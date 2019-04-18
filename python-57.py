from tkinter import *
 
canvas = Canvas(width=300, height=300, bg='green')   
canvas.pack(expand=YES, fill=BOTH)                  
x0 = 263
y0 = 263
y1 = 275
x1 = 275
for i in range(19):
    #实际上画的是线段，这里19条连成了一个更长的线段
    canvas.create_line(x0,y0,x1,y1, width=1, fill='red')
    x0 = x0 - 5
    y0 = y0 - 5
    x1 = x1 + 5
    y1 = y1 + 5
mainloop()
