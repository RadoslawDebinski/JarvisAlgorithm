import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Point as pt
import JarvisAlgorithm as ja
import hullCollison

xSpan = 100
ySpan = 100
triangleBase = 5
triangleH = 5
frame = 2
pointsAmount = 20

ptStruct = []
ptX, ptY = [], []
for _ in range (0,pointsAmount):
    point = pt.Point(xSpan,ySpan, triangleBase, triangleH)
    ptStruct.append(point)

fig, ax = plt.subplots()
ax.set_xlim(-xSpan-frame, xSpan+frame)
ax.set_ylim(-ySpan-frame, ySpan+frame)


hullDataX = []
hullDataY = []
hull, = ax.plot([], [], marker='o', color='green', markersize=2)
triangles = []
for _ in range(0, pointsAmount):
    triangles.append(ax.plot([], [], marker='o', color='black', markersize=1)[0])

start = []
firstLatch = True
topsCount = 0

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
        hC = hullCollison(point, hullDataX, hullDataY)
        point = hC.detCol()
        ptStruct[i] = point
        triX.append([point.xPos, point.xPos1, point.xPos2, point.xPos])
        pointsX.append([point.xPos, point.xPos1, point.xPos2])
        triY.append([point.yPos, point.yPos1, point.yPos2, point.yPos])
        pointsY.append([point.yPos, point.yPos1, point.yPos2])
        i += 1

    for x, y, i in zip(triX, triY, range(0, pointsAmount)):
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
        hull.set_data(np.concatenate([hullDataX, np.linspace(hullDataX[-1],hullX, 3)]),
                      np.concatenate([hullDataY, np.linspace(hullDataY[-1],hullY, 3)]))


anim = FuncAnimation(fig, anime, frames=400, interval=2000)
plt.title('Second laboratory WNO')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()