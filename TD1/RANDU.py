import csv

def RANDU(seed):
    return (65539 * seed) % (2 ** 31)

def rel(x1, x2):
    return (6 * x2 - 9 * x3) % (2 ** 31)

def integerToRational(x):
    return x / (2 ** 31)

seed = 123456
temp = seed
x1 = seed
x2 = False
# create csv file and store in a variable
csvfile = open('RANDU_123456_extended.csv', 'w', newline='')
for i in range(0, 1000):
    rng = RANDU(temp)    
    temp = rng
    line = [rng, ""]
    if x2:
        line[1] = rel(x2, x1)
        x1 = x2    
    x2 = rng
    print(rng)
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(line)


