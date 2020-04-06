import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir("/Users/drewmacklin/Documents/GitHub/project-2-drewmackin1")

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(a):
    max = np.max(a)
    min = np.min(a)
    return (a-min)/(max-min)

def testCase():
    testglucose = np.random.random_sample() 
    testhemoglobin = np.random.random_sample()
    return testglucose, testhemoglobin

def calculateDistanceArray(testGlucose, testHemoglobin):
    distances = np.zeros((0,1))
    for i in range(len(glucose)):
        distance = np.sqrt((glucose[i]-testGlucose)**2+(hemoglobin[i]-testHemoglobin)**2)
        distances = np.append(distances, distance)
    return distances

def nearestNeighborClassifier(a):
    nearestNeighborIndex = np.argmin(a)
    ckdclass = classification[nearestNeighborIndex]
    return ckdclass

def kNearestNeighborClassifier(k,a):
    total = 0
    for i in range(k):
        nearestNeighborIndex = np.argmin(a)
        total += classification[nearestNeighborIndex]
        np.delete(a,nearestNeighborIndex)
    average = total/k
    if average <.5:
        return 0
    if average >=.5:
        return 1
    
def graphTestCase(testGlucose,testHemoglobin):
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "b.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(testHemoglobin,testGlucose, "g.", markersize = 30) 
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

glucoseraw, hemoglobinraw, classification = openckdfile()
glucose = normalizeData(glucoseraw)
hemoglobin = normalizeData(hemoglobinraw)

a = testCase()[0]
b = testCase()[1]
graphTestCase(a,b)
print(nearestNeighborClassifier(calculateDistanceArray(a,b)))
print(kNearestNeighborClassifier(3,calculateDistanceArray(a,b)))

#def graphData():
#    plt.figure()
#    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
#    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
#    plt.xlabel("Hemoglobin")
#    plt.ylabel("Glucose")
#    plt.legend()
#    plt.show()
