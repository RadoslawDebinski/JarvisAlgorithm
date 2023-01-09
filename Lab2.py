import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Triangle as tr
import JarvisAlgorithm as ja

xSpan = 100
ySpan = 100
triangleBase = 5
triangleH = 5
frame = 20
trianglesAmount = 20
collArea = 3
fear = 2

ptStruct = []
ptX, ptY = [], []
for _ in range (0,trianglesAmount):
    point = tr.Triangle(xSpan,ySpan, triangleBase, triangleH)
    ptStruct.append(point)

fig, ax = plt.subplots()
ax.set_xlim(-xSpan-frame, xSpan+frame)
ax.set_ylim(-ySpan-frame, ySpan+frame)


hullDataX = []
hullDataY = []
hull, = ax.plot([], [], marker='o', color='green', markersize=2)
triangles = []
for _ in range(0, trianglesAmount):
    triangles.append(ax.plot([], [], marker='o', color='black', markersize=1)[0])

start = []
firstLatch = True
topsCount = 0

def hullCollision(point, hullDataX, hullDataY):
    collision = False
    if hullDataX != []: #point.xPos1 <= i + collArea and point.xPos1 >= i - collArea
        for i, j in zip(hullDataX,hullDataY):
            if (((point.xPos <= i + collArea and point.xPos >= i - collArea) and
                (point.yPos <= j + collArea and point.yPos >= j - collArea)) or
                ((point.xPos1 <= i + collArea and point.xPos1 >= i - collArea) and
                 (point.yPos1 <= j + collArea and point.yPos1 >= j - collArea))):

                collision = True
                if (np.absolute(np.amax([point.xPos, point.xPos1, point.xPos2])) >= 100 or
                    np.absolute(np.amax([point.yPos, point.yPos1, point.yPos2])) >= 100):
                    collision = False

        if collision:
            alpha = np.radians(180)
            rotMat = np.array(((np.cos(alpha), -np.sin(alpha)),
                               (np.sin(alpha), np.cos(alpha))))
            point.xPos = point.xPos - point.xPos2
            point.xPos1 = point.xPos1 - point.xPos2
            point.yPos = point.yPos - point.yPos2
            point.yPos1 = point.yPos1 - point.yPos2
            point.xPos, point.yPos = np.dot(rotMat, np.array(((point.xPos), (point.yPos))))
            point.xPos1, point.yPos1 = np.dot(rotMat, np.array(((point.xPos1), (point.yPos1))))
            point.xPos = point.xPos + point.xPos2
            point.xPos1 = point.xPos1 + point.xPos2
            point.yPos = point.yPos + point.yPos2
            point.yPos1 = point.yPos1 + point.yPos2
            point.movVect = [-point.movVect[0], -point.movVect[1]]
            return point
        else: return point
    else: return point

def anime(frame):
    global start
    global firstLatch
    global topsCount

    triX, pointsX = [[], []]
    triY, pointsY = [[], []]

    hullDataX, hullDataY = [list(hull.get_xdata()), list(hull.get_ydata())]

    i = 0
    for point in ptStruct:
        point = point + point.movVect
        point = hullCollision(point, list(hull.get_xdata()), list(hull.get_ydata()))
        ptStruct[i] = point
        triX.append([point.xPos, point.xPos1, point.xPos2, point.xPos])
        pointsX.append([point.xPos, point.xPos1, point.xPos2])
        triY.append([point.yPos, point.yPos1, point.yPos2, point.yPos])
        pointsY.append([point.yPos, point.yPos1, point.yPos2])
        i += 1

    for x, y, i in zip(triX, triY, range(0, trianglesAmount)):
        triangles[i].set_data(x, y)

    JA = ja.JarAlg(np.array(pointsX),np.array(pointsY))
    if firstLatch:
        start = JA.findStart()
        hullX, hullY = start[0], start[1]
        firstLatch = False
        hullDataX.append(hullX)
        hullDataY.append(hullY)
        hull.set_data(hullDataX, hullDataY)
    else:
        start = [hullDataX[-1],hullDataY[-1]]
        hullX, hullY, topsCount = JA.calculate(start, topsCount)
        hull.set_data(np.concatenate([hullDataX, np.linspace(hullDataX[-1],hullX, 200)]),
                      np.concatenate([hullDataY, np.linspace(hullDataY[-1],hullY, 200)]))


anim = FuncAnimation(fig, anime, frames=4000, interval=200)
plt.title('Second laboratory WNO')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()