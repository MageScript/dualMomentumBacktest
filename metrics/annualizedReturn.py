from otherFunctions.numberOfYearCounter import numberOfYearCounter

def annualizedReturn(price):

    lastIndex = len(price) - 1
    profitFactor = price[lastIndex] / price[0]
    numberOfYear = numberOfYearCounter(price)
    annualizedReturn = profitFactor**(1 / numberOfYear) - 1
    annualizedReturnPercentage = round(annualizedReturn * 100, 2)

    return annualizedReturn, annualizedReturnPercentage