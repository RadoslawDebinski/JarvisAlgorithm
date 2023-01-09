import numpy as np

class JarAlg():
    def __init__(self, pointsx, pointsy):
        self.pointsx = np.concatenate(pointsx, axis = 0)
        self.pointsy = np.concatenate(pointsy, axis = 0)
        # self.pointsx = np.stack(pointsx)
        # self.pointsy = np.stack(pointsy)

    def findStart(self):
        startId, iter = int(0), int(0)
        for i in self.pointsy:
            if i < self.pointsy[startId]:
                startId = iter
            iter += 1
        return [self.pointsx[startId], self.pointsy[startId]]

    def _findTop(self, start):
        self.start
        tempPoitsY = list(self.pointsy)
        tempPoitsY.append(start[1])
        topId, iter = int(0), int(0)
        for i in tempPoitsY:
            if i > tempPoitsY[topId]:
                topId = iter
            iter += 1
        return topId


    def calculate(self, start):
        self.start = start
        topId = JarAlg._findTop(self, self.start)
        topRiched = False

        angles = []
        for i in range(0,len(self.pointsy)):
            angles.append(np.arctan2(self.pointsy[i] - start[1], self.pointsx[i] - start[0]))

        if topId == len(self.pointsy):
            topRiched = True
        if topRiched:
            nextId = np.argmin(angles)
        else:
            angles = np.array(angles)
            moreZeroAnglesId = angles > 0.0
            minVal = np.amin(angles[moreZeroAnglesId == True])
            nextId = int(np.where(angles == minVal)[0])

        return [self.pointsx[nextId], self.pointsy[nextId]]


