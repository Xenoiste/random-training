import csv
from math import ceil

def middleSquare(seed, seedLength):
    square = seed ** 2
    temp = str(square)
    squareLength = len(temp)
    rng = temp[squareLength // 2 - seedLength // 2 : squareLength // 2 + ceil(seedLength / 2)]
    return int(rng)

if __name__ == "__main__": 
    seed = 123456
    seedLength = len(str(seed))
    temp = seed
    # create csv file and store in a variable
    csvfile = open('123456.csv', 'w', newline='')
    for i in range(0, 1000):
        square = temp ** 2
        temp = str(square)
        squareLength = len(temp)
        # rng = temp[squareLength // 2 - 2 : squareLength // 2 + 2]
        # round up
        rng = temp[squareLength // 2 - seedLength // 2 : squareLength // 2 + ceil(seedLength / 2)]
        print(rng)
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([rng])
        temp = int(rng)
