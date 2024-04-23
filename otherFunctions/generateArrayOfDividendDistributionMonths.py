def generateArrayOfDividendDistributionMonths(date):

    lenOfArrays = len(date)
    arrayOfDividendDistributionMonths = [0 for x in range(lenOfArrays)]

    for index, dt in enumerate(date):

        month = dt.split('/')[1]

        if month == '03' or month == '06' or month == '09' or month == '12':
            arrayOfDividendDistributionMonths[index] = 1

        else:
            arrayOfDividendDistributionMonths[index] = 0

    return arrayOfDividendDistributionMonths