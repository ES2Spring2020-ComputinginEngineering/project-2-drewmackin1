import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np
import mathplotlib as plt

k = #choose a k value. Ensure that it is the same in the driver and the function code

glucoseraw, hemoglobinraw, classification = kmc.openckdfile() #calls the openfile function in kmc
glucose = kmc.normalizeData(glucoseraw) #calls the normalize function in kmc
hemoglobin = kmc.normalizeData(hemoglobinraw) #calls the normalize function in kmc

startvalsgluc = np.zeros((k)) #create empty array of length K
startvalshemo = np.zeros((k)) #create empty array of length K
for j in range(k): #for each value of 0 to k-1
    startvalsgluc[j] = kmc.randomCentroids() #add a number between 0 and 1 as a glucose value for the jth centroid
    startvalshemo[j] = kmc.randomCentroids() #add a number between 0 and 1 as a hemoglobin value for the jth centroid

newvals = kmc.update(startvalsgluc, startvalshemo) #the new centroids are equal to the first centroids after being updated
centroidNumber = ["A"]*k #create and array length k of string
for j in range(k): #for each index in the array
    centroidNumber[j] = "$"+ str(j+1) + "$" #have the value in each index equal to itself plus one in between two $s
    
for j in range(k): #for every centroid
    plt.plot(startvalsgluc[j],startvalshemo[j], marker=".", markersize = 30) #plot a colored dot at its center
    plt.plot(startvalsgluc[j],startvalshemo[j], marker=str(centroidNumber[j]), color= "white") #plot white number at its center
plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1") #plot the data
plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0") #plot the data
plt.xlabel("Glucose") #label the graph
plt.ylabel("Hemoglobin")
plt.legend()
plt.show() #show the graph

for j in range(k): #for every centroid
     plt.plot(newvals[0][j],newvals[1][j], marker=".", markersize = 30) #plot the new centroid dot
     plt.plot(newvals[0][j],newvals[1][j], marker=str(centroidNumber[j]), color= "white") #and number
plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1") #and data
plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
plt.xlabel("Glucose") #and labels
plt.ylabel("Hemoglobin")
plt.legend()
plt.show()

for i in range(10): #for 10 iterations
    newvals = kmc.update(newvals[0], newvals[1]) #update the value of newvals using the update function
    for j in range(k): #for every centroid
        plt.plot(newvals[0][j],newvals[1][j], marker=".", markersize = 30) #plot it
        plt.plot(newvals[0][j],newvals[1][j], marker=str(centroidNumber[j]), color= "white") #plot it
    plt.plot(glucose[classification==1],hemoglobin[classification==1], "g.", label = "Data 1") #and the data
    plt.plot(glucose[classification==0],hemoglobin[classification==0], "k.", label = "Data 0")
    plt.xlabel("Glucose") #and the labels
    plt.ylabel("Hemoglobin")
    plt.legend()
    plt.show()

predictions = kmc.nearestCentroid(kmc.calculateDistanceArray(newvals[0], newvals[1])) #create and array of the points with the corresponding nearest centroid's classification
truePositive = 0 #initialize values
falsePositive = 0
trueNegative = 0
falseNegative = 0
for i in range(len(glucose)):
    if(predictions[i] == classification[i] and predictions[i] == 0): #if both classify it as 0
        truePositive += 1 #it is a true positive
    if(predictions[i] == classification[i] and predictions[i] == 1): #if both classify it as 1
        trueNegative += 1 #it is a true negative
    if(predictions[i] == 1 and classification[i] == 0): #the prediction is 1 and the classification is 0
        falsePositive+= 1 #it is a false positive
    if(predictions[i] == 0 and classification[i] == 1): #the prediction is 0 and the classification is 1
         falseNegative += 1 #it is a false negative
print(truePositive, falsePositive, trueNegative,falseNegative) #print the values
