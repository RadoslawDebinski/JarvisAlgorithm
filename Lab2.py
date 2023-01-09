import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import Point as pt
import JarvisAlgorithm as ja

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
    ptX.append(point.xPos)
    ptY.append(point.yPos)
    ptX.append(point.xPos1)
    ptY.append(point.yPos1)
    ptX.append(point.xPos2)
    ptY.append(point.yPos2)

JA = ja.JarAlg(ptX,ptY)
hullX, hullY = JA.calculate()

fig, ax = plt.subplots()
ax.set_xlim(-xSpan-frame, xSpan+frame)
ax.set_ylim(-ySpan-frame, ySpan+frame)

#points, = ax.plot(ptX, ptY, 'bo', markersize=2)
hullDataX = []
hullDataY = []
#hullData, = ax.plot([], [], marker='o', color='green', markersize=3)
triangles = []
for _ in range(0, pointsAmount):
    triangles.append(ax.plot([], [], marker='o', color='black', markersize=3)[0])

def anime(frame):
    triX = []
    triY = []

    i = 0
    for point in ptStruct:
        point = point + point.movVect
        ptStruct[i] = point
        triX.append([point.xPos, point.xPos1, point.xPos2, point.xPos])
        triY.append([point.yPos, point.yPos1, point.yPos2, point.yPos])
        i += 1

    for x, y, i in zip(triX, triY, range(0, pointsAmount)):
        triangles[i].set_data(x, y)
    # hullDataX.append(hullX[frame])
    # hullDataY.append(hullY[frame])
    # hulldata.set_data(hullDataX, hullDataY)

anim = FuncAnimation(fig, anime, frames=400, interval=100)
plt.title('Second laboratory WNO')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()