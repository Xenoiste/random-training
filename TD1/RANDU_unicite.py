import csv

class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

def RANDU(seed):
    return (65539 * seed) % (2 ** 31)

def rel(x1, x2):
    return (6 * x2 - 9 * x1) % (2 ** 31)

def integerToRational(x):
    return x / (2 ** 31)

seed = 13579
n = 1000000
temp = seed
listOfRationalsRNG = []
# listOfRationalsRNG.append(integerToRational(seed))

# create csv file and store in a variable
csvfile = open('RANDU_temp.csv', 'w', newline='')
for i in range(n):
    rng1 = RANDU(temp)    
    rng2 = RANDU(rng1)
    temp = rng2
    point = Point(integerToRational(rng1), integerToRational(rng2))
    line = [point.x, point.y]  
    #print(integerToRational(rng1), integerToRational(rng2))
    # csvwriter = csv.writer(csvfile)
    # csvwriter.writerow(line)
    listOfRationalsRNG.append(point)

div = 10
repartition = []
for i in range(div):
    repartition.append([])
    for j in range(div):
        repartition[i].append(0)
for i in range(len(listOfRationalsRNG)):
    val = listOfRationalsRNG[i].x
    axis = listOfRationalsRNG[i].y
    y = div - 1 - int(val / (1/div))
    x = int(axis / (1/div))
    repartition[y][x] += 1

for tab in repartition:
    print(tab)

