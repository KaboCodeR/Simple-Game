import turtle

wn = turtle.Screen()
turtle = turtle.Turtle()

wn.bgcolor("black")
turtle.shape("square")
turtle.color("white")

def gotomiddle():
  turtle.goto(0, 0)
  
  
while True:
  turtle.goto(-150, 150)
  gotomiddle()
