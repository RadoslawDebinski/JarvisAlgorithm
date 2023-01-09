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

            base = np.random.uniform(4,self.triangleBase)
            height = np.random.uniform(4,self.triangleH)
            side = np.sqrt(np.square(base/2) + np.square(height))

            alpha = np.radians(np.random.uniform(0, 359))
            beta = np.arctan2(height,base/2)
            gamma = alpha - beta

            self.xPos1 = self.xPos + np.cos(alpha)*base
            self.yPos1 = self.yPos + np.sin(alpha)*base

            self.xPos2 = self.xPos + np.cos(gamma) * side
            self.yPos2 = self.yPos + np.sin(gamma) * side

            baseMidX = (self.xPos + self.xPos1)/2
            baseMidY = (self.yPos + self.yPos1)/2
            self.movVect = [baseMidX - self.xPos2, baseMidY - self.yPos2]
        else:
            self.xPos = 0
            self.yPos = 0
            self.xPos1 = 0
            self.yPos1 = 0
            self.xPos2 = 0
            self.yPos2 = 0
            self.movVect = [0,0]

    def _mapBorderCheck(self, xPos, yPos, xPos1, yPos1, xPos2, yPos2, movVect):
        if np.absolute(np.amax([xPos, xPos1, xPos2])) >= 100 or np.absolute(np.amax([yPos, yPos1, yPos2])) >= 100:
            alpha = np.radians(180)
            rotMat = np.array(((np.cos(alpha), -np.sin(alpha)),
                          (np.sin(alpha), np.cos(alpha))))
            xPos = xPos - xPos2
            xPos1 = xPos1 - xPos2
            yPos = yPos - yPos2
            yPos1 = yPos1 - yPos2
            xPos, yPos = np.dot(rotMat, np.array(((xPos), (yPos))))
            xPos1, yPos1 = np.dot(rotMat, np.array(((xPos1), (yPos1))))
            xPos = xPos + xPos2
            xPos1 = xPos1 + xPos2
            yPos = yPos + yPos2
            yPos1 = yPos1 + yPos2
            return xPos, xPos1, yPos, yPos1, [-movVect[0], -movVect[1]]
        else:
            return xPos, xPos1, yPos, yPos1, movVect

    def __add__(self, mov):
        temp = Point(0,0,0,0)
        temp.xPos = self.xPos + mov[0]
        temp.yPos = self.yPos + mov[1]
        temp.xPos1 = self.xPos1 + mov[0]
        temp.yPos1 = self.yPos1 + mov[1]
        temp.xPos2 = self.xPos2 + mov[0]
        temp.yPos2 = self.yPos2 + mov[1]
        temp.xPos, temp.xPos1, temp.yPos, temp.yPos1, temp.movVect = temp._mapBorderCheck(temp.xPos, temp.yPos,
                                                                                          temp.xPos1, temp.yPos1,
                                                                                          temp.xPos2, temp.yPos2,
                                                                                          mov)
        return temp








