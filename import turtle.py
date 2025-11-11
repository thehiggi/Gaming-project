import turtle

#creation of the screen
screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

#creation of left paddle
left_pad = turtle.Turtle()
left_pad.shape("square")
left_pad.color("white")
left_pad.penup()
left_pad.goto(-450,0)
left_pad.shapesize(stretch_len=1,stretch_wid=5)

#creation of right paddle
right_pad = turtle.Turtle()
right_pad.shape("square")
right_pad.color("white")
right_pad.penup()
right_pad.goto(450,0)
right_pad.shapesize(stretch_len=1,stretch_wid=5)


#this just keeps the screen open instead of instantly closing
screen.mainloop()
