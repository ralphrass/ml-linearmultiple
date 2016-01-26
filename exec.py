import read as r
import numpy as np

dataSet = r.readFile()

M = float(len(dataSet))
ALPHA = 0.0003
CONVERGENCE_LIMIT = 1
ITERATIONS_LIMIT = M*20*4

def initializeParameters():
    Ts = []
    #nr of features, -1 to remove the prediction feature (Y column)
    nrFeatures = len(dataSet[0]) -1
    for i in range(nrFeatures):
        Ts.append(float(0))
    return Ts

#Ts is the Theta values vector and X is the feature values for a given record
def calcHypotesis(Ts, X):
    hx = float(np.dot(X, Ts))
    return hx

#return the features values for a given record (except the last one - Y column)
def xEs(Ts, row):
    xVector = []
    for X in range(0, len(Ts)):
        xVector.append(float(row[X]))
    return xVector

#Ts: a vector with Theta values
def costFunction(Ts):
    SUM = 0
    for row in dataSet:
        Y = float(row[len(Ts)])
        xVector = xEs(Ts, row)
        SUM += (calcHypotesis(Ts, xVector) - Y) ** 2
    cost = 1/(2*M) * SUM
    return cost

#gradient descent iterations
def gradientDescent(Ts):
    nrIterations = 0
    while True:
        cost = costFunction(Ts)
        sums = initializeParameters()
        for row in dataSet:
            Y = float(row[len(Ts)])
            xVector = xEs(Ts, row)
            #sum for every parameter Theta (wich match the nr of X columns)
            for j in range(len(Ts)):
                sums[j] += calcHypotesis(Ts, xVector) - Y * float(row[j])
                #.append(calcHypotesis(Ts, xVector) - Y * Xi)

        #update Theta values
        for j in range(len(Ts)):
            Ts[j] = Ts[j] - ALPHA * 1/M * sums[j]

        newCost = costFunction(Ts)

        print Ts, abs(newCost - cost)

        if (abs(newCost - cost) < CONVERGENCE_LIMIT):
            break
        elif (nrIterations == ITERATIONS_LIMIT):
            break

        nrIterations += 1

Ts = initializeParameters()
#print Ts
#print costFunction(Ts)
gradientDescent(Ts)

"""while True:

    SUM_THETA_0, SUM_THETA_1 = 0, 0
    cost = costFunction(THETA_0, THETA_1)
    for row in dataSet:
        X = getValue(row, 0)
        Y = getValue(row, 1)
        H0 = THETA_0 + THETA_1 * X
        SUM_THETA_0 += H0 - Y
        SUM_THETA_1 += (H0 - Y) * X

    THETA_0 = THETA_0 - (ALPHA * (1/M)) * SUM_THETA_0
    THETA_1 = THETA_1 - (ALPHA * (1/M)) * SUM_THETA_1

    newCost = costFunction(THETA_0, THETA_1)

    if (abs(newCost - cost) < CONVERGENCE_LIMIT):
        break
    elif (nrIterations == ITERATIONS_LIMIT):
        break

    nrIterations += 1

X = raw_input('Wich base-value do you want to use to make a prediction? ')

print 'Predicted value is', int(h0), 'the loop was executed', nrIterations, 'times'

"""
