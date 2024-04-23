def returnBarChart(price):

    lenOfArrays = len(price)
    returnBC = [0 for x in range(lenOfArrays)]

    for index, pr in enumerate(price):

        if index > 0:

            returnBC[index] = ((pr / price[index-1]) - 1) * 100

    return returnBC