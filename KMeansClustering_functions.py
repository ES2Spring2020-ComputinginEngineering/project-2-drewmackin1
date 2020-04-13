import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir("/Users/drewmacklin/Documents/GitHub/project-2-drewmackin1")

k = 3

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(a):
    max = np.max(a)
    min = np.min(a)
    return (a-min)/(max-min)

def randomCentroids():
    random = np.random.random_sample() 
    return random

def calculateDistanceArray(ckgluc,ckhemo):
    distancesK = np.zeros((len(glucose),k))
    for j in range(k):
        for i in range(len(glucose)):
            distanceK = np.sqrt((glucose[i]-ckgluc[j])**2+(hemoglobin[i]-ckhemo[j])**2)
            distancesK[i][j] = distanceK
    return distancesK

def nearestCentroid(a): 
    groupj = np.zeros((len(glucose)))
    for i in range(len(glucose)):
        j = np.argmin(a[i])
        groupj[i] = j
    return groupj

def newCentroid(a):    
    totalgluc = np.zeros((k)) 
    totalhemo = np.zeros((k))
    averagegluc = np.zeros((k))
    averagehemo = np.zeros((k))
    countgluc = np.zeros((k))
    counthemo = np.zeros((k))
    for i in range(len(a)):
        j = int(a[i])
        totalgluc[j] += glucose[i]
        totalhemo[j] += hemoglobin[i]
        countgluc[j] += 1
        counthemo[j] += 1
    for j in range(len(totalgluc)):
        if (countgluc[j] > 0):
            averagegluc[j] = totalgluc[j]/countgluc[j]
            averagehemo[j] = totalhemo[j]/counthemo[j]
    return averagegluc, averagehemo

def update(ckgluc,ckhemo):
    distarrs = calculateDistanceArray(ckgluc,ckhemo)
    nearcents = nearestCentroid(distarrs)
    newCentroids = newCentroid(nearcents) 
    return newCentroids

glucoseraw, hemoglobinraw, classification = openckdfile()
glucose = normalizeData(glucoseraw)
hemoglobin = normalizeData(hemoglobinraw)

startvalsgluc = np.zeros((k))
startvalshemo = np.zeros((k))
for j in range(k):
    startvalsgluc[j] = randomCentroids()
    startvalshemo[j] = randomCentroids()

newvals = update(startvalsgluc, startvalshemo)
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

predictions = nearestCentroid(calculateDistanceArray(newvals[0], newvals[1]))
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
