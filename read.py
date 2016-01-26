import csv

def readFile():

    dataSet = []

    #9 = Wheel Base (86.6 to 120.9)
    #10 = Length (141.1 to 208.1)
    #11 = Width (60.3 to 72.3)
    #12 = Height (47.8 to 59.8)
    #16 = Engine Size
    #21 = HorsePower
    #25 = Price (Prediction)
    with open('dataset/imports-85.data', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            #dataSet.append([1, row[9], row[10], row[11], row[12], row[21], row[25]])
            dataSet.append([1, float(row[16])/326, float(row[21])/288, row[25]])

    return dataSet
