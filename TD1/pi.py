import random
import matplotlib.pyplot as plt
import numpy as np
from RNG import middleSquare
from math import sqrt, ceil
from RANDU import randu

SEED = 127634

def randomMiddleSquareNumbers(n, seed = random.randint(0, 10 ** 6)):
    list = []
    temp = seed
    for i in range(n):
        temp = middleSquare(temp, len(str(seed)))
        list.append(temp)
    return list

def randomRandomNumbers(n):
    list = []
    for i in range(n):
        list.append(random.random())
    return list

def randomRanduNumbers(n, seed = random.randint(0, 10 ** 6)):
    list = []
    temp = seed
    for i in range(n):
        temp = randu(temp)
        list.append(temp)
    return list

def d(x, y):
    d = x**2 + y**2
    if d <= 1:
        return 1
    else:
        return 0

def calcPI(randomNumbers):
    n = len(randomNumbers)//2
    somme = 0
    for i in range(0, n*2, 2):
        somme += d(random.random(), random.random())
    resultat = somme * 4 / n
    return resultat

# print(calcPI(randomMiddleSquareNumbers(10 ** 3)))
# print(calcPI(randomRandomNumbers(10 ** 6)))
# print(calcPI(randomRanduNumbers(10 ** 6)))

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()
ax.set_title('PI')
ax.scatter(1, 1, s=1,)

n = 10 ** 2
randomNumbers = randomRandomNumbers(n * 2)
for i in range(0, n * 2, 2):
    if d(randomNumbers[i], randomNumbers[i + 1]) == 1:
        ax.scatter(randomNumbers[i], randomNumbers[i + 1], s=1, color='red')
    else:
        ax.scatter(randomNumbers[i], randomNumbers[i + 1], s=1, color='blue')
plt.show()