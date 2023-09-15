import random
from RNG import middleSquare
from math import sqrt

initialSeed = 127634

def d(x, y):
    d = sqrt(x**2 + y **2)
    if d <= 1:
        return 1
    else:
        return 0

def superMiddleSquare():
    if (not("seed" in locals())): seed = initialSeed
    seed = middleSquare(seed, 10)
    return seed / (10 ** len(str(seed)))


# def calcPI():
#     n = 10 ** 6
#     somme = 0
#     for i in range(n):
#         somme += d(random.random(), random.random())
#     resultat = somme * 4 / n
#     print(resultat)

def calcPI(randomFunction):
    n = 10 ** 2
    somme = 0
    for i in range(n):
        somme += d(randomFunction(), randomFunction())
    resultat = somme * 4 / n
    print(resultat)

calcPI(superMiddleSquare)
print("3.14159265358979323846264338327950288419716939937510")
