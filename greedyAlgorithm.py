import numpy as np
from visualization import x, y
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def distance(x1, y1, x2, y2):
    return np.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


for i in range(0, len(x)):
    plt.plot(x[i], y[i], marker='*', color="red")
passedCities = []
passedCities.append(0)
j = 0
minDistCity = 0
counter = 0
totalDist = 0
while counter < len(x) - 1:
    i = minDistCity
    minDist = 100000
    minDistCity = 0
    for j in range(1, len(x)):
        if (j != i) and not (j in passedCities):
            dist = distance(x[i], y[i], x[j], y[j])
            if dist < minDist:
                minDist = dist
                minDistCity = j
    print(minDistCity)
    passedCities.append(minDistCity)
    totalDist += minDist
    counter += 1
    plt.plot([x[i], x[minDistCity]], [y[i], y[minDistCity]], color="blue")
print(totalDist)
plt.plot([x[0], x[minDistCity]], [y[0], y[minDistCity]], color="blue")
plt.savefig("greedy.png")
plt.show()



