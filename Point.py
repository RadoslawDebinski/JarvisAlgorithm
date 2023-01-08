import numpy as np

class Point():
    def __init__(self, xSpan, ySpan, triangleBase, triangleH):
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








