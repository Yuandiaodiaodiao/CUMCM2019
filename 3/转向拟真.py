import matplotlib.pyplot as plt
import numpy as np
import math

carl = 4.415
carw = 1.674
box = 20
plt.xlim((-box, box))
plt.ylim((-box, box))


def drawline(x1, y1, x2, y2):
    x = [[x1, x2]]  # 要连接的两个点的坐标
    y = [[y1, y2]]
    for i in range(len(x)):
        plt.plot(x[i], y[i], color='r', )
        # plt.scatter(x[i], y[i], color='b')


def drawcar(xo, yo, angle):
    gca = plt.gca()
    # car=plt.Rectangle((1,1),carl,carw)
    # gca.add_patch(car)

    anglePi = -angle * math.pi / 180.0
    cosA = math.cos(anglePi)
    sinA = math.sin(anglePi)
    x = xo + carl / 2
    y = yo + carw / 2
    x1 = x - 0.5 * carw
    y1 = y - 0.5 * carl

    x0 = x + 0.5 * carw
    y0 = y1

    x2 = x1
    y2 = y + 0.5 * carl

    x3 = x0
    y3 = y2

    x0n = (x0 - x) * cosA - (y0 - y) * sinA + x
    y0n = (x0 - x) * sinA + (y0 - y) * cosA + y

    x1n = (x1 - x) * cosA - (y1 - y) * sinA + x
    y1n = (x1 - x) * sinA + (y1 - y) * cosA + y

    x2n = (x2 - x) * cosA - (y2 - y) * sinA + x
    y2n = (x2 - x) * sinA + (y2 - y) * cosA + y

    x3n = (x3 - x) * cosA - (y3 - y) * sinA + x
    y3n = (x3 - x) * sinA + (y3 - y) * cosA + y
    drawline(x0n, y0n, x1n, y1n)
    drawline(x1n, y1n, x2n, y2n)
    drawline(x2n, y2n, x3n, y3n)
    drawline(x0n, y0n, x3n, y3n)


x = np.arange(-box, box)
y1 = 0 + 0 * x
y2 = 3.5 + 0 * x
y3 = 7 + 0 * x
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
for x in range(-3, 3):
    drawcar(x * 5, 1, 60)
# for x in range(-3, 3):
#     drawcar(x * 5, 4.5, 90)

plt.show()
