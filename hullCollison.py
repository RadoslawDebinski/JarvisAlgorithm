import numpy as np
import Point as pt

class hullCollision():
    def __init__(self, point, hullDataX, hullDataY):
        self.point = point
        self.hullDataX = hullDataX
        self.hullDataY = hullDataY
        
    def detCol(self):
        if np.absolute(np.amax([self.point.xPos, self.point.xPos1, self.point.xPos2])) >= 100 or np.absolute(np.amax([self.point.yPos, self.point.yPos1, self.point.yPos2])) >= 100:
            alpha = np.radians(180)
            rotMat = np.array(((np.cos(alpha), -np.sin(alpha)),
                          (np.sin(alpha), np.cos(alpha))))
            self.point.xPos = self.point.xPos - self.point.xPos2
            self.point.xPos1 = self.point.xPos1 - self.point.xPos2
            self.point.yPos = self.point.yPos - self.point.yPos2
            self.point.yPos1 = self.point.yPos1 - self.point.yPos2
            self.point.xPos, self.point.yPos = np.dot(rotMat, np.array(((self.point.xPos), (self.point.yPos))))
            self.point.xPos1, self.point.yPos1 = np.dot(rotMat, np.array(((self.point.xPos1), (self.point.yPos1))))
            self.point.xPos = self.point.xPos + self.point.xPos2
            self.point.xPos1 = self.point.xPos1 + self.point.xPos2
            self.point.yPos = self.point.yPos + self.point.yPos2
            self.point.yPos1 = self.point.yPos1 + self.point.yPos2
            self.point.movVect = [-movVect[0], -movVect[1]]
            return point
        else:
            return point