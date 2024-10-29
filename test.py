import turtle

turtle.tracer(0,0)
turtle.speed(3)
#this area is compleatly usless, dont pay attention. its my testing area. also I was bored so

#this bassicly just changes how dense the forests are, you can make it go wild if you change it above 7, 1-5 makes some cool changes
density = 5


def mountain1(x, y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()
   turtle.left(80)
   turtle.forward(10)
   turtle.right(5)
   turtle.forward(10)
   turtle.right(100)
   turtle.forward(3)
   turtle.left(100)
   turtle.forward(20)
   turtle.right(120)
   turtle.forward(5)
   turtle.left(120)
   turtle.forward(15)
   turtle.left(10)
   turtle.forward(10)
   turtle.right(150)
   turtle.forward(7)
   turtle.left(150)
   turtle.forward(20)
   turtle.right(160)
   
   turtle.forward(20)
   turtle.left(100)
   turtle.forward(4)
   turtle.right(110)
   turtle.forward(15)
   turtle.left(120)
   turtle.forward(7)
   turtle.right(110)
   turtle.forward(20) 
   turtle.left(150)
   turtle.forward(6)
   turtle.right(150)
   turtle.forward(30)
def mountain2():
   
   turtle.left(80)
   turtle.forward(7)
   turtle.right(2)
   turtle.forward(7)
   turtle.right(110)
   turtle.forward(4)
   turtle.left(110)
   turtle.forward(8)
   turtle.right(115)
   turtle.forward(4)
   turtle.left(120)
   turtle.forward(15)
   turtle.left(7)
   turtle.forward(9)
   turtle.right(145)
   turtle.forward(5)
   turtle.left(145)
   turtle.forward(9)
   turtle.right(160)


   turtle.forward(20)
   turtle.left(100)
   turtle.forward(4)
   turtle.right(110)
   turtle.forward(15)
   turtle.left(120)
   turtle.forward(7)
   turtle.right(110)
   turtle.forward(20)
   turtle.left(150)
   turtle.forward(6)
   turtle.right(150)
   turtle.forward(30)
def mountain3():
   
   turtle.right(80)
   turtle.forward(7)
   turtle.left(2)
   turtle.forward(7)
   turtle.left(110)
   turtle.forward(4)
   turtle.right(110)
   turtle.forward(8)
   turtle.left(115)
   turtle.forward(4)
   turtle.right(120)
   turtle.forward(15)
   turtle.right(7)
   turtle.forward(9)
   turtle.left(145)
   turtle.forward(5)
   turtle.right(145)
   turtle.forward(9)
   turtle.left(160)


   turtle.forward(20)
   turtle.right(100)
   turtle.forward(4)
   turtle.left(110)
   turtle.forward(15)
   turtle.right(120)
   turtle.forward(7)
   turtle.left(110)
   turtle.forward(20)
   turtle.right(150)
   turtle.forward(6)
   turtle.left(150)
   turtle.forward(30)
def keep(x, y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()
   turtle.forward(5)
   turtle.left(90)
   turtle.forward(7)
   turtle.left(90)
   turtle.forward(10)
   turtle.left(90)
   turtle.forward(4)
   #first pylong 
   turtle.right(90)
   turtle.forward(8)
   turtle.right(90)
   #middle 
   turtle.forward(4)
   turtle.left(90)
   turtle.forward(10)
   turtle.left(90)
   turtle.forward(7)
   #second pylon
   turtle.left(90)
   turtle.forward(5)
   turtle.right(90)
   turtle.forward(30)
   turtle.left(90)
   #right before door
   turtle.forward(7)
   turtle.left(90)

   
   turtle.forward(5)
   for i in range (180):
       turtle.right(1)
       turtle.forward(0.05)
    
   turtle.forward(5)
   #door
   turtle.left(90)
   turtle.forward(5)
   turtle.left(90)
   turtle.forward(30)
   turtle.left(90)
   turtle.forward(19)
   #finishing
def tree1():

   for i in range(360):
        turtle.forward(0.1)
        turtle.right(1)
def foresttool():
   for i in range(3):
    for e in range(4):
        turtle.down()
        tree1()
        turtle.left(90)
        turtle.up()
        turtle.forward((5*((e+density)/2))/1.29)
    turtle.up()
    turtle.forward(28)
def riverstraight():
   
   turtle.forward(26)
   turtle.up()
   turtle.left(90)
   turtle.forward(9)
   turtle.left(90)
   turtle.down()
   turtle.forward(25)
   turtle.up()
   turtle.left(90)
   turtle.forward(8)
   turtle.left(90)
   turtle.forward(25)
   turtle.down()
   
def riverturn():
  
    
   for i in range(90):
      turtle.forward(0.3)
      turtle.left(1)
   turtle.left(90)
   turtle.up()   
   turtle.forward(10)
   turtle.down()
   turtle.left(90)
   for i in range(90):
      turtle.forward(0.15)
      turtle.right(1)
   turtle.up()
   turtle.left(180)
   for i in range(90):
      turtle.left(1)
      turtle.forward(0.15)
   turtle.right(90)
   turtle.forward(10)
   turtle.down()
   turtle.left(90)
      
def mountaintool1():
    #all you need to start a chain with mountain
   turtle.setheading(90)
   turtle.up()
   turtle.forward(25)
   turtle.left(90)
   turtle.forward(10)
   turtle.down()
   turtle.setheading(0)
def mountaintool2():
   #use this for the first mountain in mountain 3
   turtle.setheading(180)
   turtle.up()
   turtle.forward(52)
   turtle.right(90)
   turtle.forward(20)
   turtle.down()
   turtle.setheading(180)
def mountaintool3():
   #after using mountain tool 2 use this to infinitly do the chain
   turtle.setheading(90)
   turtle.up()
   turtle.forward(25)
   turtle.right(90)
   turtle.forward(10)
   turtle.down()
   turtle.setheading(180)


def tree2(x, y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()
   for i in range(360):
        turtle.forward(0.1)
        turtle.right(1)
def g():  
   turtle.setheading(0)
def signature(x, y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()
   turtle.setheading(90)
   turtle.forward(10)
   turtle.right(140)
   turtle.forward(11.547)
   turtle.left(140)
   turtle.forward(10)
   g()
   turtle.forward(2)
   for i in range(180):
      turtle.forward(0.05)
      turtle.right(1)
   turtle.forward(2)
   turtle.left(135)
   turtle.forward(6.05)
def goto(x, y):
   turtle.up()
   turtle.goto(x, y)
   turtle.down()











         



turtle.up()

turtle.goto(1000,1000)


turtle.update()


turtle.exitonclick()