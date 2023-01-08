import numpy as np

class JarAlg():
    def __init__(self, pointsx, pointsy):
        self.pointsx = pointsx
        self.pointsy = pointsy

    def _findStart(self):
        startId, iter = int(0), int(0)
        for i in self.pointsy:
            if i < self.pointsy[startId]:
                startId = iter
            iter += 1
        return startId

    def _findTop(self):
        topId, iter = int(0), int(0)
        for i in self.pointsy:
            if i > self.pointsy[topId]:
                topId = iter
            iter += 1
        return topId


    def calculate(self):
        startId = JarAlg._findStart(self)
        topId = JarAlg._findTop(self)
        topRiched = False

        hullX, hullY = [], []
        hullX.append(self.pointsx[startId])
        hullY.append(self.pointsy[startId])

        while True:
            angles = []
            for i in range(0,len(self.pointsy)):
                angles.append(np.arctan2(self.pointsy[i] - self.pointsy[startId], self.pointsx[i] - self.pointsx[startId]))

            if self.pointsy[startId] == self.pointsy[topId]:
                topRiched = True
            if topRiched:
                nextId = np.argmin(angles)
            else:
                angles = np.array(angles)
                moreZeroAnglesId = angles > 0.0
                minVal = np.amin(angles[moreZeroAnglesId == True])
                nextId = int(np.where(angles == minVal)[0])

                
            if nextId == startId:
                break
            hullX.append(self.pointsx[nextId])
            hullY.append(self.pointsy[nextId])
            startId = nextId

        return hullX, hullY


