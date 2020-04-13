import numpy as np #import functions
import matplotlib.pyplot as plt
import os

os.chdir("/Users/drewmacklin/Documents/GitHub/project-2-drewmackin1") #create path
k = 3 #set k value

def openckdfile(): #opens csv and returns values as 1*n arrays
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification 

def normalizeData(a): #normalizes data from 0 to 1
    max = np.max(a)
    min = np.min(a)
    return (a-min)/(max-min)

def randomCentroids(): #creates and returns a random number from 0 to 1
    return np.random.random_sample()

def calculateDistanceArray(ckgluc,ckhemo): #calculates the distance between every point and every centroid and returns an n*k array
    distancesK = np.zeros((len(glucose),k))#initializes an empty n*k array
    for j in range(k): #for every k value
        for i in range(len(glucose)): #for every n value
            distanceK = np.sqrt((glucose[i]-ckgluc[j])**2+(hemoglobin[i]-ckhemo[j])**2) #distance = euclidian distance function
            distancesK[i][j] = distanceK #append it to the empty array
    return distancesK #return the array

def nearestCentroid(a): #takes in the array created by calculate distance array and finds the nearest centroid
    groupj = np.zeros((len(glucose))) #creates and empty array of length n
    for i in range(len(glucose)): #for every value up to n
        j = np.argmin(a[i]) #find the smallest value of distance in each row of the passed in array and record its index (centroid number)
        groupj[i] = j #append the centroid number to the empty array
    return groupj #return the array

def newCentroid(a):    #takes in the nearest centroid array and returns the location of the average of each centroids group
    totalgluc = np.zeros((k)) #initialize the total glucose in each centroid group to 0
    totalhemo = np.zeros((k)) #initialize the total hemoglobin in each centroid group to 0
    averagegluc = np.zeros((k)) #initialize the average glucose in each centroid group to 0
    averagehemo = np.zeros((k)) #initialize the average hemoglobin in each centroid group to 0
    countgluc = np.zeros((k)) #initialize the total number of points in each centroid group to 0
        j = int(a[i]) #j is the integer value of the value in each box (the number associated with the nearest centroid)
        totalgluc[j] += glucose[i] #the total glucose of centroid j increases by the amount of glucose associated with the point in the centroid's group
        totalhemo[j] += hemoglobin[i] #the total hemoglobin of centroid j increases by the amount of hemoglobin associated with the point in the centroid's group
        countgluc[j] += 1 #increase the count by 1 (this will be used to calculate the average as totalvalue/number of data points = average
    for j in range(len(totalgluc)): #for everything in the total arrays
        if (countgluc[j] > 0): #ensure not to divide by zero
            averagegluc[j] = totalgluc[j]/countgluc[j] #find the average value of glucose in each centroid group
            averagehemo[j] = totalhemo[j]/countgluc[j] #find the average value of hemoglobin in each centroid group
    return averagegluc, averagehemo #return the new average values and these are the new centroids

def update(ckgluc,ckhemo): #updates the centroid location by calling each function in succession
    distarrs = calculateDistanceArray(ckgluc,ckhemo)
    nearcents = nearestCentroid(distarrs)
    newCentroids = newCentroid(nearcents) 
    return newCentroids

glucoseraw, hemoglobinraw, classification = openckdfile() #calls the openfile function
glucose = normalizeData(glucoseraw) #calls the normalize function
hemoglobin = normalizeData(hemoglobinraw) #calls the normalize function

startvalsgluc = np.zeros((k)) #create empty array of length K
startvalshemo = np.zeros((k)) #create empty array of length K
for j in range(k): #for each value of 0 to k-1
    startvalsgluc[j] = kmc.randomCentroids() #add a number between 0 and 1 as a glucose value for the jth centroid
    startvalshemo[j] = kmc.randomCentroids() #add a number between 0 and 1 as a hemoglobin value for the jth centroid

newvals = update(startvalsgluc, startvalshemo) #the new centroids are equal to the first centroids after being updated
centroidNumber = ["A"]*k #create and array length k of string
for j in range(k): #for each index in the array
    centroidNumber[j] = "$"+ str(j+1) + "$" #have the value in each index equal to itself plus one in between two $s
    
plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1") #plot the data
plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0") #plot the data
plt.xlabel("Glucose") #label the graph
plt.ylabel("Hemoglobin")
plt.legend()
for j in range(k): #for every centroid
    plt.plot(startvalsgluc[j],startvalshemo[j], marker=".", markersize = 30) #plot a colored dot at its center
    plt.plot(startvalsgluc[j],startvalshemo[j], marker=str(centroidNumber[j]), color= "white") #plot white number at its center
plt.show() #show the graph

plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1") #and data
plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
plt.xlabel("Glucose") #and labels
plt.ylabel("Hemoglobin")
plt.legend()
for j in range(k): #for every centroid
     plt.plot(newvals[0][j],newvals[1][j], marker=".", markersize = 30) #plot the new centroid dot
     plt.plot(newvals[0][j],newvals[1][j], marker=str(centroidNumber[j]), color= "white") #and number
plt.show()

for i in range(10): #for 10 iterations
    newvals = update(newvals[0], newvals[1]) #update the value of newvals using the update function
    plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1") #and the data
    plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
    plt.xlabel("Glucose") #and the labels
    plt.ylabel("Hemoglobin")
    plt.legend()
    for j in range(k): #for every centroid
        plt.plot(newvals[0][j],newvals[1][j], marker=".", markersize = 30) #plot it
        plt.plot(newvals[0][j],newvals[1][j], marker=str(centroidNumber[j]), color= "white") #plot it
    plt.show()

predictions = nearestCentroid(calculateDistanceArray(newvals[0], newvals[1])) #create and array of the points with the corresponding nearest centroid's classification
truePositive = 0 #initialize values
falsePositive = 0
trueNegative = 0
falseNegative = 0
for i in range(len(glucose)):
    if(predictions[i] == classification[i] and predictions[i] == 0):truePositive += 1 # if both classify it as 0, it is a true positive
    if(predictions[i] == classification[i] and predictions[i] == 1): trueNegative += 1 #if both classify it as 1 it is a true negative
    if(predictions[i] == 1 and classification[i] == 0):falsePositive+= 1 #the prediction is 1 and the classification is 0, it is a false positive
    if(predictions[i] == 0 and classification[i] == 1):falseNegative += 1 #the prediction is 0 and the classification is 1, it is a false negative
print(truePositive, falsePositive, trueNegative,falseNegative) #print the values
