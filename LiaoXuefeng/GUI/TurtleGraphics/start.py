from turtle import *

def drawStart(x, y):
    pu() #抬起画笔
    goto(x,y) #将画笔移动到坐标为x,y的位置
    pd() #放下画笔
    # set heading: 0  改变行进方向（绝对角度，正西方为基准）
    seth(0)
    for i in range(5):
        fd(40)
        rt(144)

for x in range(0, 250, 50):
    drawStart(x, 0)

done()