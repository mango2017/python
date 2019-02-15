# -*- coding: UTF-8 -*-

# 海龟画图
import turtle

t = turtle.Pen()
t.width(10)


t.pencolor('red')
t.fillcolor('green')
t.begin_fill()
t.circle(100)
t.end_fill()



t.penup()
t.goto(220,0)
t.color('black')
t.pendown()
t.circle(100)

t.penup()
t.goto(440,0)
t.color('red')
t.pendown()
t.circle(100)

t.penup()
t.goto(110,-120)
t.color('yellow')
t.pendown()
t.circle(100)

t.penup()
t.goto(330,-120)
t.color('green')
t.pendown()
t.circle(100)

turtle.done()

