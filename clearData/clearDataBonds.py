import csv

def clearDataBonds(bonds_path_file):

    with open(bonds_path_file, newline='') as f:
        reader = csv.reader(f)
        bondsData = list(reader)

    lenOfArrays = len(bondsData)
    bondPrice = [0 for x in range(lenOfArrays)]

    for index, bData in enumerate(bondsData):

        if index > 0:
            bondPrice[index - 1] = float(bData[0])
        

    return bondPrice

    