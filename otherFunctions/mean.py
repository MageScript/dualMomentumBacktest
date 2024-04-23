def meanF(values, lowIndex, highIndex):
    indexRange = highIndex - lowIndex
    sum = 0
    for ite in range (lowIndex, highIndex):
        sum += values[ite]
    mean = sum / indexRange
    return mean