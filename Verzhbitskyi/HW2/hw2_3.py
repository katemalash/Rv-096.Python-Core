import turtle

circle = turtle.Turtle()
circle.shape("turtle")
circle.pensize(5)
circle.pencolor("black")
circle.color("black", "yellow")
circle.begin_fill()

circle.penup()
circle.goto(0, -200)
circle.pendown()
circle.circle(200)
circle.end_fill()

circle.begin_fill()
circle.penup()
circle.goto(-80, 80)
circle.color("black")
circle.pendown()
circle.circle(30)
circle.end_fill()

circle.begin_fill()
circle.penup()
circle.goto(80, 80)
circle.color("black")
circle.pendown()
circle.circle(30)
circle.end_fill()

circle.pensize(5)
circle.penup()
circle.goto(-130,-30)
circle.pendown()
circle.seth(-80)
circle.circle(130,160)


window = turtle.Screen()
window.mainloop()