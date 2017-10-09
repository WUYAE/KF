import turtle

turtle.hideturtle()
turtle.color('red')
turtle.begin_fill()
for i in range(2):
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
turtle.up()
turtle.color('red')
turtle.end_fill()
#矩形

turtle.goto(16,128)
turtle.down()
turtle.color('yellow','yellow')
turtle.begin_fill()
for i in range(5):
    turtle.forward(48)
    turtle.right(144)
turtle.up()
turtle.end_fill()
#大星星

turtle.goto(80,144)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(217)
turtle.forward(8)
turtle.right(162)
turtle.begin_fill()
for i in range(5):
    turtle.forward(16)
    turtle.right(144)
turtle.end_fill()
#第一个小星星
    
turtle.up()
turtle.goto(96,128)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(172)
turtle.forward(8)
turtle.right(170)
turtle.begin_fill()
for i in range(5):
    turtle.forward(16)
    turtle.right(144)
turtle.end_fill()
#第二个小星星

turtle.up()
turtle.goto(96,106)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(164)
turtle.forward(8)
turtle.right(164)
turtle.begin_fill()
for i in range(5):
    turtle.forward(16)
    turtle.right(144)
turtle.end_fill()
#第三个小星星

turtle.up()
turtle.goto(80,88)
turtle.down()
turtle.color('yellow','yellow')
turtle.left(141)
turtle.forward(8)
turtle.right(162)
turtle.begin_fill()
for i in range(5):
    turtle.forward(16)
    turtle.right(144)
turtle.up()
turtle.end_fill()
turtle.done()
#第四个小星星
