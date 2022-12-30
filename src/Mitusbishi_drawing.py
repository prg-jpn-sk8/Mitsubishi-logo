from turtle import *

title("Mitsubishi")

goto(0, 0)

hideturtle()

pencolor("red")

speed(0.75)

begin_fill()
for x in range(3):
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    fillcolor("red")

end_fill()

penup()
goto(-265, -220)
pendown()
pencolor("black")
write("MITSUBISHI", font=("Verdana", 70))
done()
