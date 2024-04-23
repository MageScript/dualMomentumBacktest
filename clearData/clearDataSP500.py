def clearData(SP500Data):

    lenOfArrays = len(SP500Data)
    dateDataCleared = [0 for x in range(lenOfArrays)]
    priceDataCleared = [0 for x in range(lenOfArrays)]
    dividendsCleared = [0 for x in range(lenOfArrays)]

    for index, pricedata in enumerate(SP500Data):

        splitedData = pricedata[0].split(';')

        dateDataCleared[index] = splitedData[0]
        priceDataCleared[index] = float(splitedData[1])
        dividendsCleared[index] = float(splitedData[2]) / 100


    return dateDataCleared, priceDataCleared, dividendsCleared