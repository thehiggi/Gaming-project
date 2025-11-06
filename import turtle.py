import turtle


screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

left_pad = turtle.Turtle()
left_pad.shape("square")
left_pad.color("white")
left_pad.penup()
left_pad.goto(-450,0)

screen.mainloop()
