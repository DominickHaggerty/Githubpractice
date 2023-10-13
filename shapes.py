import turtle

hex = turtle.Turtle()
s = turtle.Turtle()
t =turtle.Turtle()

#prep
hex.penup()
hex.left(90)
hex.forward(200)
hex.pendown()

s.penup()
s.right(90)
s.forward(200)
s.pendown()

t.penup()
t.forward(200)
t.pendown()

for x in range(6):
    hex.forward(100)
    hex.right(60)

for x in range(3):
    t.right(120) 
    t.forward(100)

for x in range(4):
    s.forward(100)
    s.right(90)



turtle.Screen().exitonclick()

