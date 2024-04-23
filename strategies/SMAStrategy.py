import sys
sys.path.insert(1, r'C:\Users\Megaport\OneDrive - ESTIA\Divers\python')

from indicators.movingAverage import sma
from otherFunctions.generateCoefficients import generateCoefficients
from otherFunctions.generateArrayOfDividendDistributionMonths import generateArrayOfDividendDistributionMonths
from otherFunctions.mean import meanF

def generateArrayOfOrderDecisionFromSMA(price, SMA, lenght):

    lenOfArrays = len(SMA)
    arrayOfOrderDecision = [0 for x in range(lenOfArrays)]

    for index, sma in enumerate(SMA):

        if index <= lenght:
            arrayOfOrderDecision[index] = 0

        else:
            if SMA[index - 1] < price[index - 1]:
                arrayOfOrderDecision[index] = 1

            else: 
                arrayOfOrderDecision[index] = 0

    return arrayOfOrderDecision




def smaMarketTiming(price, SMAlenght, reinvestDividends=None, dividends=None, date=None, buyEnable=True, sellEnable=True):

    lenOfArrays = len(price)
    smaMTstrategy = [0 for x in range(lenOfArrays)]

    SMA = sma(price, SMAlenght)
    arrayOfOrderDecision = generateArrayOfOrderDecisionFromSMA(price, SMA, SMAlenght)
    coefficients = generateCoefficients(price)


    if reinvestDividends and buyEnable and not sellEnable:

        arrayOfDividendDistributionMonths = generateArrayOfDividendDistributionMonths(date)
        priceBeforeDividends = [0 for x in range(lenOfArrays)]
        earnedDividends = [0 for x in range(lenOfArrays)]

        for index, amstr in enumerate(smaMTstrategy):

            if index <= 6: 
                smaMTstrategy[index] = 1

            else:
                priceBeforeDividends[index] = coefficients[index] * smaMTstrategy[index - 1]

                if arrayOfDividendDistributionMonths[index] == 1:
                    earnedDividends[index] = priceBeforeDividends[index] * meanF(dividends, index - 2, index) / 4


                if arrayOfOrderDecision[index] == 1:
                    smaMTstrategy[index] = priceBeforeDividends[index]

                else:
                    smaMTstrategy[index] = smaMTstrategy[index - 1]


                if arrayOfDividendDistributionMonths[index] == 1 and arrayOfOrderDecision[index - 1]:
                    smaMTstrategy[index] += earnedDividends[index]





    if not reinvestDividends and buyEnable and not sellEnable:

            for index, amstr in enumerate(smaMTstrategy):

                if index <= 6: 
                    smaMTstrategy[index] = 1

                else:

                    if arrayOfOrderDecision[index] == 0:
                        smaMTstrategy[index] = smaMTstrategy[index - 1] * coefficients[index]

                    else:
                        smaMTstrategy[index] = smaMTstrategy[index - 1]








    if not reinvestDividends and buyEnable and sellEnable:

            for index, amstr in enumerate(smaMTstrategy):

                if index <= 6: 
                    smaMTstrategy[index] = 1

                else:

                    if arrayOfOrderDecision[index] == 0:
                        smaMTstrategy[index] = smaMTstrategy[index - 1] * coefficients[index]

                    else:
                        smaMTstrategy[index] = smaMTstrategy[index - 1] * (2 - coefficients[index])
                        


    return smaMTstrategy