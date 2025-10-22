from turtle import *

timmy = Turtle()
timmy.speed(10)

def koch_curve(n, step):
    if n == 0:
        timmy.forward(step)
        return
    else:
        koch_curve(n-1, step/3)
        timmy.left(60)
        koch_curve(n-1,step/3)
        timmy.right(120)
        koch_curve(n-1,step/3)
        timmy.left(60)
        koch_curve(n-1,step/3)

for i in range(3):
    koch_curve(3,100)
    timmy.right(120)

done()