import numpy as np #import functions
import matplotlib.pyplot as plt
import os

os.chdir("/Users/drewmacklin/Documents/GitHub/project-2-drewmackin1") #create path

def openckdfile(): #opens csv and converts to the 1*n arrays
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(a): #normalizes data to be between 0 and 1
    max = np.max(a)
    min = np.min(a)
    return (a-min)/(max-min)

def testCase(): #creates two random numbers between 0 and 1 that represent glucose and hemoglobin values
    testglucose = np.random.random_sample() 
    testhemoglobin = np.random.random_sample()
    return testglucose, testhemoglobin

def calculateDistanceArray(testGlucose, testHemoglobin): #finds the distance between the point and all the data points
    distances = np.zeros((0,1)) #creates an empty array
    for i in range(len(glucose)): #for every data point
        distance = np.sqrt((glucose[i]-testGlucose)**2+(hemoglobin[i]-testHemoglobin)**2) #find the distance between it and the test point
        distances = np.append(distances, distance) #append this distance to the empty array
    return distances #return the array

def nearestNeighborClassifier(a): #finds the nearest point
    nearestNeighborIndex = np.argmin(a) #finds the index of the nearest neighbor
    ckdclass = classification[nearestNeighborIndex] #uses the index to find that point's classification
    return ckdclass #returns the classification of the nearest point

def kNearestNeighborClassifier(k,a): #finds the average of the k nearest neighbors
    total = 0 #initialize the total values of the neighbors classifications
    for i in range(k): #for every value between 0 and k 
        nearestNeighborIndex = np.argmin(a) #finds the index of the nearest neighbor
        total += classification[nearestNeighborIndex]#adds the classification to total
        np.delete(a,nearestNeighborIndex) #deletes the smallest distance and repeats k times (ie finds the second smallest distance next time)
    average = total/k #finds the average value of classification across k points
    if average <.5: #if the average is less than .5, classify the point as 0
        return 0 
    if average >=.5: #if the average is greater than .5 classify the point as 1
        return 1
    
def graphTestCase(testGlucose,testHemoglobin): #graphs the test case and the data
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "b.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.plot(testHemoglobin,testGlucose, "g.", markersize = 30) #graphs the test case
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

glucoseraw, hemoglobinraw, classification = openckdfile() #open the csv
glucose = normalizeData(glucoseraw) #normalize glucose
hemoglobin = normalizeData(hemoglobinraw) #normalize hemoglobin

a = testCase()[0] #store the random value
b = testCase()[1] #store the random value
graphTestCase(a,b) #graph the test case over the data
print(nearestNeighborClassifier(calculateDistanceArray(a,b))) #print the value of nearestneighbor
print(kNearestNeighborClassifier(3,calculateDistanceArray(a,b))) #print the value of knearestneighbor

#def graphData(): #this code is unnecessary with the graphTestCase function, but this graphs only the data and not the test case
#    plt.figure()
#    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
#    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
#    plt.xlabel("Hemoglobin")
#    plt.ylabel("Glucose")
#    plt.legend()
#    plt.show()
