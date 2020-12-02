from visualization import x, y
import numpy as np
from random import randint
import matplotlib.pyplot as plt

plt.style.use('ggplot')


def distance(x1, y1, x2, y2):
    return np.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


citiesAll = []
for i in range(0, len(x)):
    citiesAll.append(i)

minDist = 100000
minList = []

for i in range(0, 70000):
    dist = 0
    passedCities = []
    passedCities.append(0)
    while len(passedCities) < len(x):
        remainedCities = list(set(citiesAll) - set(passedCities))
        cityNum1 = randint(0, len(remainedCities) - 1)
        cityNum2 = randint(0, len(remainedCities) - 1)
        cityNum3 = randint(0, len(remainedCities) - 1)
        cityNum4 = randint(0, len(remainedCities) - 1)
        cityNum5 = randint(0, len(remainedCities) - 1)
        d1 = distance(x[passedCities[-1]], y[passedCities[-1]],
                      x[remainedCities[cityNum1]], y[remainedCities[cityNum1]])
        d2 = distance(x[passedCities[-1]], y[passedCities[-1]],
                      x[remainedCities[cityNum2]], y[remainedCities[cityNum2]])
        d3 = distance(x[passedCities[-1]], y[passedCities[-1]],
                      x[remainedCities[cityNum3]], y[remainedCities[cityNum3]])
        d4 = distance(x[passedCities[-1]], y[passedCities[-1]],
                      x[remainedCities[cityNum4]], y[remainedCities[cityNum4]])
        d5 = distance(x[passedCities[-1]], y[passedCities[-1]],
                      x[remainedCities[cityNum5]], y[remainedCities[cityNum5]])
        if d1 == min(d1, d2, d3, d4, d5):
            cityNum = cityNum1
        else:
            if d2 == min(d1, d2, d3, d4, d5):
                cityNum = cityNum2
            else:
                if d3 == min(d1, d2, d3, d4, d5):
                    cityNum = cityNum3
                else:
                    if d4 == min(d1, d2, d3, d4, d5):
                        cityNum = cityNum4
                    else:
                        cityNum = cityNum5
        passedCities.append(remainedCities[cityNum])
    for j in range(1, len(passedCities)):
        dist += distance(x[passedCities[j]], y[passedCities[j]],
                         x[passedCities[j - 1]], y[passedCities[j - 1]])
    dist += distance(x[0], y[0], x[passedCities[j]], y[passedCities[j]])
    if dist < minDist:
        minDist = dist
        minList = passedCities

print(minDist)
print(minList)
for i in range(0, len(x)):
    plt.plot(x[i], y[i], marker='*', color="red")
for i in range(1, len(minList)):
    plt.plot([x[minList[i]], x[minList[i - 1]]], [y[minList[i]], y[minList[i - 1]]], color="blue")
plt.plot([x[minList[0]], x[minList[-1]]], [y[minList[0]], y[minList[-1]]], color="blue")
plt.savefig("randomSearch.png")
plt.show()
