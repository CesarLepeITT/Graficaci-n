from turtle import *

def draw_eyes():
    for steps in range(30):
        for c in ('blue', 'red', 'green'):
            color(c)
            forward(steps)
            right(30)

def draw_smile():
    setheading(-60)
    circle(120, 120)
    setheading(0)
    


pu()
setpos(-100, 0)
pd()

posInicial = pos()

draw_eyes()

pu()
posaux = pos()
setpos((posaux[0], posaux[1] - 20))
pd()

print(pos())
draw_smile()

posfinal = pos()

pu()
setpos(posfinal[0], posInicial[1])
pd()


draw_eyes()
        
exitonclick()