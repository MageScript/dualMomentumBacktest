from otherFunctions.mean import meanF
from otherFunctions.generateArrayOfDividendDistributionMonths import generateArrayOfDividendDistributionMonths
from otherFunctions.generateCoefficients import generateCoefficients
from clearData.clearDataBonds import clearDataBonds


def calculateAccMom(price, period=None, atSignal=None):

    lenOfArrays = len(price)
    accMomScores = [0 for x in range(lenOfArrays)]

    if period == 'monthly':
        period = 1

    if period == 'daily':
        period = 30
    

    for index, pr in enumerate(price):

        if index >= 6:

            momentum6 = pr / price[index - period*6] - 1
            momentum3 = pr / price[index - period*3] - 1
            momentum1 = pr / price[index - period] - 1

            accMomScores[index] = 100 * (momentum1 + momentum3 + momentum6) / 3

        else: 
            accMomScores[index] = None


    return accMomScores




def generateArrayOfOrderDecisionFromAccMomScores(accMomScores):

    lenOfArrays = len(accMomScores)
    arrayOfOrderDecision = [0 for x in range(lenOfArrays)]

    for index, ams in enumerate(accMomScores):

        if index <= 6:
            arrayOfOrderDecision[index] = 0

        else:
            if accMomScores[index - 1] > 0:
                arrayOfOrderDecision[index] = 1

            else: 
                arrayOfOrderDecision[index] = 0

    return arrayOfOrderDecision





def accMomStrategy(price, period=None, buyEnable = None, sellEnable = None, reinvestDividends = None, dividends = None, date = None):

    lenOfArrays = len(price)
    accMomStrategyPrice = [0 for x in range(lenOfArrays)]

    accMomScores = calculateAccMom(price, period=period)
    arrayOfOrderDecision = generateArrayOfOrderDecisionFromAccMomScores(accMomScores)
    coefficients = generateCoefficients(price)


    if reinvestDividends and buyEnable and not sellEnable:

        arrayOfDividendDistributionMonths = generateArrayOfDividendDistributionMonths(date)
        priceBeforeDividends = [0 for x in range(lenOfArrays)]
        earnedDividends = [0 for x in range(lenOfArrays)]

        for index, amstr in enumerate(accMomStrategyPrice):

            if index <= 6: 
                accMomStrategyPrice[index] = 1

            else:
                priceBeforeDividends[index] = coefficients[index] * accMomStrategyPrice[index - 1]

                if arrayOfDividendDistributionMonths[index] == 1:
                    earnedDividends[index] = priceBeforeDividends[index] * meanF(dividends, index - 2, index) / 4


                if arrayOfOrderDecision[index] == 1:
                    accMomStrategyPrice[index] = priceBeforeDividends[index]

                else:
                    accMomStrategyPrice[index] = accMomStrategyPrice[index - 1]


                if arrayOfDividendDistributionMonths[index] == 1 and arrayOfOrderDecision[index - 1]:
                    accMomStrategyPrice[index] += earnedDividends[index]





    if reinvestDividends and buyEnable and sellEnable:

        arrayOfDividendDistributionMonths = generateArrayOfDividendDistributionMonths(date)
        priceBeforeDividends = [0 for x in range(lenOfArrays)]
        earnedDividends = [0 for x in range(lenOfArrays)]


        for index, amstr in enumerate(accMomStrategyPrice):

            if index <= 6: 
                accMomStrategyPrice[index] = 1

            else:
                priceBeforeDividends[index] = coefficients[index] * accMomStrategyPrice[index - 1]

                if arrayOfDividendDistributionMonths[index] == 1:
                    earnedDividends[index] = priceBeforeDividends[index] * meanF(dividends, index - 2, index) / 4


                if arrayOfOrderDecision[index] == 1:
                    accMomStrategyPrice[index] = priceBeforeDividends[index]

                else:
                    accMomStrategyPrice[index] = accMomStrategyPrice[index - 1] / coefficients[index]


                if arrayOfDividendDistributionMonths[index] == 1 and arrayOfOrderDecision[index - 1] and arrayOfOrderDecision[index] == 1:
                    accMomStrategyPrice[index] += earnedDividends[index]






    if not reinvestDividends and buyEnable and not sellEnable:


        for index, amstr in enumerate(accMomStrategyPrice):

            if index <= 6: 
                accMomStrategyPrice[index] = 1

            else:

                if arrayOfOrderDecision[index] == 1:
                    accMomStrategyPrice[index] = accMomStrategyPrice[index - 1] * coefficients[index]

                else:
                    accMomStrategyPrice[index] = accMomStrategyPrice[index - 1]

    





    if not reinvestDividends and buyEnable and sellEnable:


        for index, amstr in enumerate(accMomStrategyPrice):

            if index <= 6: 
                accMomStrategyPrice[index] = 1

            else:

                if arrayOfOrderDecision[index] == 1:
                    accMomStrategyPrice[index] = accMomStrategyPrice[index - 1] * coefficients[index]

                else:
                    accMomStrategyPrice[index] = accMomStrategyPrice[index - 1] * (2 - coefficients[index])


    return accMomStrategyPrice











def accDualMomStrategy(spPrice, bondPrice,  reinvestDividends = None, dividends = None, date = None):

    lenOfArrays = len(spPrice)
    accDualMomStrategyPrice = [0 for x in range(lenOfArrays)]

    accMomScores = calculateAccMom(spPrice, period='monthly')
    arrayOfOrderDecision = generateArrayOfOrderDecisionFromAccMomScores(accMomScores)
    SPcoefficients = generateCoefficients(spPrice)
    bondCoefficients = generateCoefficients(bondPrice)


    if reinvestDividends:

        arrayOfDividendDistributionMonths = generateArrayOfDividendDistributionMonths(date)
        priceBeforeDividends = [0 for x in range(lenOfArrays)]
        earnedDividends = [0 for x in range(lenOfArrays)]

        for index, amstr in enumerate(accDualMomStrategyPrice):

            if index <= 6: 
                accDualMomStrategyPrice[index] = 1

            else:
                priceBeforeDividends[index] = SPcoefficients[index] * accDualMomStrategyPrice[index - 1]

                if arrayOfDividendDistributionMonths[index] == 1:
                    earnedDividends[index] = priceBeforeDividends[index] * meanF(dividends, index - 2, index) / 4


                if arrayOfOrderDecision[index] == 1:
                    accDualMomStrategyPrice[index] = priceBeforeDividends[index]

                else:
                    accDualMomStrategyPrice[index] = accDualMomStrategyPrice[index - 1] * bondCoefficients[index]


                if arrayOfDividendDistributionMonths[index] == 1 and arrayOfOrderDecision[index - 1]:
                    accDualMomStrategyPrice[index] += earnedDividends[index]



    return accDualMomStrategyPrice