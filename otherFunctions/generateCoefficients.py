def generateCoefficients(price):

    lenOfArrays = len(price)
    coefficients = [0 for x in range(lenOfArrays)]

    for index, pr in enumerate(price):

        if index > 0:
            coefficients[index] = price[index] / price[index - 1]

    return coefficients