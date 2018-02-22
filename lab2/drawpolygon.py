'''
drawpolygon.py
Draws a polygon in the Turtle window.
'''

def drawPolygon(aTurtle, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        aTurtle.forward(sideLength)
        aTurtle.right(turnAngle)
