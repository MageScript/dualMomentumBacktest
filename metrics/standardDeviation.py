from statistics import mean
from sys import stderr
from otherFunctions.mean import meanF

def standardDeviation(price):

    numberOfPoints = len(price)
    mean = meanF(price, 0, numberOfPoints)
    sum = 0

    for pr in price:
        sum += abs(pr - mean)**2

    stdDeviation = sum / (numberOfPoints - 1)

    stdDeviation = stdDeviation**(1/2)

    stdDeviation *= 100

    stdDeviation /= mean
    
    return stdDeviation