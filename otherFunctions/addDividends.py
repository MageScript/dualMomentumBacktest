import csv
from otherFunctions.generateCoefficients import generateCoefficients
from otherFunctions.mean import meanF

def addDividends(date, price, dividends):

    lenOfArrays = len(price)
    dividendReinvestedSP500 = [0 for x in range(lenOfArrays)]
    coefficients = generateCoefficients(price)
    dividendsEarned = [0 for x in range(lenOfArrays)]

    for index, pr in enumerate(price):
        
        if index <= 1:
            dividendReinvestedSP500[index] = pr


        if index == 2:
            dividendsEarned[index] = meanF(price, index - 2, index) * meanF(dividends, index - 2, index) / 4
            dividendReinvestedSP500[index] = dividendsEarned[index] + pr


        if index > 2 and index < 5:
            dividendReinvestedSP500[index] = dividendReinvestedSP500[index - 1] * coefficients[index]


        indexDate = date[index]
        indexMonth = indexDate.split('/')[1]

        if index >= 5 and (indexMonth == "03" or indexMonth == "06" or indexMonth == "09" or indexMonth == "12"):
            dividendReinvestedSP500[index] = dividendReinvestedSP500[index - 1] * coefficients[index]          
            dividendsEarned[index] = meanF(dividendReinvestedSP500, index - 2, index) * meanF(dividends, index - 2, index) / 4
            dividendReinvestedSP500[index] += dividendsEarned[index]        

        elif index >= 5:
            dividendReinvestedSP500[index] = dividendReinvestedSP500[index - 1] * coefficients[index]


    return dividendReinvestedSP500