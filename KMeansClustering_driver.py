#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np
import mathplotlib as plt

k = #choose a k value. Ensure that it is the same in the driver and the function code

glucoseraw, hemoglobinraw, classification = kmc.openckdfile()
glucose = normalizeData(glucoseraw)
hemoglobin = normalizeData(hemoglobinraw)

startvalsgluc = np.zeros((k))
startvalshemo = np.zeros((k))
for j in range(k):
    startvalsgluc[j] = kmc.randomCentroids()
    startvalshemo[j] = kmc.randomCentroids()

newvals = kmc.update(startvalsgluc, startvalshemo)
centroidNumber = ["A"]*k
for j in range(k):
    centroidNumber[j] = "$"+ str(j+1) + "$"
    
for j in range(k):
    plt.plot(startvalsgluc[j],startvalshemo[j], marker=".", markersize = 30)
    plt.plot(startvalsgluc[j],startvalshemo[j], marker=str(centroidNumber[j]), color= "white")
plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1")
plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
plt.xlabel("Glucose")
plt.ylabel("Hemoglobin")
plt.legend()
plt.show()

for j in range(k):
     plt.plot(newvals[0][j],newvals[1][j], marker=".", markersize = 30)
     plt.plot(newvals[0][j],newvals[1][j], marker=str(centroidNumber[j]), color= "white")
plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1")
plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
plt.xlabel("Glucose")
plt.ylabel("Hemoglobin")
plt.legend()
plt.show()

for i in range(10):
    newvals = update(newvals[0], newvals[1])
    for j in range(k):
        plt.plot(newvals[0][j],newvals[1][j], marker=".", markersize = 30)
        plt.plot(newvals[0][j],newvals[1][j], marker=str(centroidNumber[j]), color= "white")
    plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1")
    plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
    plt.xlabel("Glucose")
    plt.ylabel("Hemoglobin")
    plt.legend()
    plt.show()

predictions = kmc.nearestCentroid(kmc.calculateDistanceArray(newvals[0], newvals[1]))
truePositive = 0
falsePositive = 0
trueNegative = 0
falseNegative = 0
for i in range(len(glucose)):
    if(predictions[i] == classification[i] and predictions[i] == 0):
        truePositive += 1
    if(predictions[i] == classification[i] and predictions[i] == 1):
        trueNegative += 1
    if(predictions[i] == 1 and classification[i] == 0):
        falsePositive+= 1
    if(predictions[i] == 0 and classification[i] == 1):
         falseNegative += 1
print(truePositive, falsePositive, trueNegative,falseNegative)
