import turtle as tu
x = 0
y = 0

tu.hideturtle()
def GG (x, y, color1):
    counter = 0
    tu.begin_fill()
    while counter < 1:
        tu.bgcolor('black')
        tu.speed(500)
        tu.pensize(500)
        tu.pu()
        tu.setposition(x, y)
        tu.pd()
        tu.pencolor(color1)
        tu.forward(2000)
        tu.right(90)
        tu.forward(500)
        tu.right(90)
        tu.forward(2000)
        tu.right(90)
        tu.forward(500)
        counter = counter+1
    tu.end_fill()


GG(-1000, -500, 'lime')
        


x = 0
y = 0

def WMstand (x, y, color1):
    counter = 0
    tu.begin_fill()
    while counter < 1:
        tu.bgcolor('Black')
        tu.pensize(1)
        tu.pu()
        tu.setposition(x, y)
        tu.pd()
        tu.pencolor(color1)
        tu.forward(1)
        tu.right(120)
        tu.forward(100)
        tu.right(90)
        tu.backward(100)
        tu.right(45)
        tu.forward(150)
        tu.backward(1)
        counter = counter+1
    tu.end_fill()

WMstand (-100,100, 'brown')
WMstand (200, 150, 'brown')
WMstand (-300, -100, 'brown')


x = 0
y = 0

def WM (x, y, colour1, colour2, colour3):
    counter = 1
    while counter < 10:
        tu.speed(20000)
        tu.pu()
        tu.setposition(x, y)
        tu.pd()
        tu.pencolor(colour1)
        tu.right(45)
        tu.forward(50)
        tu.left(45)
        tu.forward(50)
        tu.right(45)
        tu.setposition(x,y)
        tu.pencolor(colour2)
        tu.right(45)
        tu.forward(50)
        tu.left(45)
        tu.forward(50)
        tu.right(45)
        tu.setposition(x,y)
        tu.pencolor(colour3)
        tu.right(45)
        tu.forward(50)
        tu.left(45)
        tu.forward(50)
        tu.right(45)
        counter = counter+1
        tu.pu()

WM(-100, 100, 'blue', 'red', 'purple')
WM(200, 150, 'lime', 'orange', 'yellow')
WM(-300, -100, 'purple', 'violet', 'light blue')


def hulk (x, y, color1, pensize1):
    counter = 0
    tu.pu()
    while counter < 2:
        tu.pencolor(color1)
        tu.pensize(pensize1)
        tu.setposition(x, y)
        tu.pd()
        counter = counter+1
    
hulk(300, -172, 'lime', 40)
hulk(310, -195, 'lime', 30)
hulk(290, -195, 'lime', 30)
hulk(310, -195, 'green', 6)
hulk(290, -195, 'green', 6)
hulk(300, -210, 'lime', 20)
hulk(300, -218, 'lime', 20)
hulk(310, -223, 'purple', 15)
hulk(293, -223, 'purple', 15)
hulk(300, -223, 'purple', 15)
hulk(310, -230, 'purple', 15)
hulk(293, -230, 'purple', 15)
hulk(310, -240, 'lime', 15)
hulk(293, -240, 'lime', 15)
hulk(321, -193, 'lime', 20)
hulk(279, -193, 'lime', 20)
hulk(277, -190, 'lime', 20)









