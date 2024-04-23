def sma(priceData, numberOfPeriod):

    movingAverage = [0 for x in range(len(priceData))]
    somme = 0

    for index, pricedata in enumerate(priceData):
        if index >= numberOfPeriod - 1:

            for a in range(0, numberOfPeriod):
                somme = somme + priceData[index - a]
            sma = somme / numberOfPeriod
            somme = 0

            movingAverage[index] = sma

        if index < numberOfPeriod - 1:
            movingAverage[index] = None

    return movingAverage