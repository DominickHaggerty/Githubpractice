import turtle

tL = turtle.Turtle()
tT = turtle.Turtle()
tR = turtle.Turtle()



#prep phase
tL.color("gold")
tL.width(10)
tL.penup()
tL.backward(250)
tL.right(90)
tL.forward(200)

tT.color("gold")
tT.width(10)
tT.penup()
tT.left(90)
tT.forward(200)

tR.color("gold")
tR.width(10)
tR.penup()
tR.forward(250)
tR.right(90)
tR.forward(200)

#-------------------------------------------------------------

#Left Triangle
tL.pendown()
tL.left(148)
tL.forward(228)
tL.right(115)
tL.forward(230)
tL.right(123)
tL.forward(240)

#Top Triangle
tT.pendown()
tT.left(148)
tT.forward(232)
tT.left(122)
tT.forward(228)
tT.left(119)
tT.forward(228)

#Right Triangle
tR.pendown()
tR.right(145)
tR.forward(235)
tR.left(115)
tR.forward(228)
tR.left(120)
tR.forward(240)




turtle.Screen().exitonclick()



