import random

def f(x: float) -> float:
    return x**2

a = 0
b = 1
n = 1000000000
somme = 0

def integrale():
    for i in range(n):
        somme += f(random.random() * (b - a) + a)

    resultat = somme * (b - a) / n
    print(resultat)

