import numpy as np

class Point():
    def __init__(self, xSpan, ySpan, triangleBase, triangleH):
        if(xSpan > 0 and ySpan > 0 and triangleBase > 0 and triangleH > 0):
            self.xSpan = xSpan
            self.ySpan = ySpan
            self.triangleBase = triangleBase
            self.triangleH = triangleH
            self.xPos = np.random.uniform(-self.xSpan,self.xSpan)
            self.yPos = np.random.uniform(-self.ySpan,self.ySpan)

            base = np.random.uniform(2,self.triangleBase)
            height = np.random.uniform(2,self.triangleH)
            side = np.sqrt(np.square(base/2) + np.square(height))

            alpha = np.radians(np.random.uniform(0, 359))
            beta = np.arctan2(height,base/2)
            gamma = alpha - beta

            self.xPos1 = self.xPos + np.cos(alpha)*base
            self.yPos1 = self.yPos + np.sin(alpha)*base

            self.xPos2 = self.xPos + np.cos(gamma) * side
            self.yPos2 = self.yPos + np.sin(gamma) * side

            baseMidX = self.xPos + self.xPos1
            baseMidY = self.yPos + self.yPos1
            self.movVect = [self.xPos2 - baseMidX, self.yPos2 - baseMidY]
        else:
            self.xPos = 0
            self.yPos = 0
            self.xPos1 = 0
            self.yPos1 = 0
            self.xPos2 = 0
            self.yPos2 = 0
            self.movVect = [0,0]

    def __add__(self, mov):
        temp = Point(0,0,0,0)
        temp.xPos = self.xPos + mov[0]
        temp.yPos = self.yPos + mov[1]
        temp.xPos1 = self.xPos1 + mov[0]
        temp.yPos1 = self.yPos1 + mov[1]
        temp.xPos2 = self.xPos2 + mov[0]
        temp.yPos2 = self.yPos2 + mov[1]
        temp.movVect = self.movVect

        return temp








