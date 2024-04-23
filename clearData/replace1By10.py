import csv

def replace1by10(source):
    with open(source, newline='') as f:
        reader = csv.reader(f)
        SP500Data = list(reader)


    for index, spdata in enumerate(SP500Data):

        month = ''
        
        try:
            month = spdata[0].split(';')[0].split("/")[1]

        except:
            print('no slash detected')

        if month == '1':
            SP500Data[index] = [spdata[0].split(';')[0].split("/")[0] + '/' + '10' + ';' + spdata[0].split(';')[1] + ';' + spdata[0].split(';')[2]]

    return SP500Data