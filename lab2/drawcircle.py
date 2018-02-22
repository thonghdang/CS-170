'''
drawcircle.py
Draws a circle in the Turtle window.
'''

def drawCircle(aTurtle, radius):
    circumference = 2 * 3.1415 * radius 
    sideLength = circumference / 360
    
    aTurtle.left(90)
    aTurtle.up()
    aTurtle.forward(radius)
    aTurtle.right(90)
    aTurtle.down()
    
    for i in range(360):
        aTurtle.forward(sideLength)
        aTurtle.right(1)

    aTurtle.up()
    aTurtle.right(90)
    aTurtle.forward(radius)
    aTurtle.down()

    
