from turtle import *

penup()
goto(200,0)
pendown()
color('red', 'yellow')
begin_fill()
speed('fastest')
while True:
    forward(200)
    left(91)
    x,y=pos()
    if abs(x-200)<1 and abs(y)<1:
        break
end_fill()
penup()
color('red', 'yellow')
goto(-200,0)
pendown()
begin_fill()
speed('fastest')
while True:
    forward(200)
    left(115)
    x,y=pos()
    if abs(x+200)<1 and abs(y)<1:
        break
end_fill()
done()
