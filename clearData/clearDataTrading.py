import csv

def clearDataTrading(intrument_path_file):

    with open(intrument_path_file, newline='') as f:
        reader = csv.reader(f)
        intrumentData = list(reader)

    lenOfArrays = len(intrumentData)
    dateDataCleared = [0 for x in range(lenOfArrays)]
    priceDataCleared = [0 for x in range(lenOfArrays)]

    for index, pricedata in enumerate(intrumentData):

        splitedData = pricedata[0].split(';')

        dateDataCleared[index] = splitedData[0] + ',' + splitedData[1]
        priceDataCleared[index] = float(splitedData[2])


    return dateDataCleared, priceDataCleared