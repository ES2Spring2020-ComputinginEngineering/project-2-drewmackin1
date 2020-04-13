The NearestNeighbor classification code is able to be run by itself and can be copied into spyder and run once the path is changed to the path that would function on the user's computer and it requires that the user have a csv file called "ckd.csv" that is accessible by the path. 

I wrote the K-means clustering all on one file, so the K-meansClustering_Functions includes all the code that is in the driver and should be run by itself. I have not tested the code in the driver to see if it functions because it is much simpler to just run the code in the functions folder. As with the NearestNeighbor, the user of the code must change the path in order for the code to be able to access the csv file required to run the code. 

For detailed function overviews in each file please see the comments in the code as well as the report.

NearestNeighbor:
opencdkfile(no arguments, returns 3 1*158 arrays of glucose hemoglobin classification respectively)
normalizeData(argument: array of any length, returns an array where the smallest value is zero and the largest is one)
testCase(no arguments, returns two random numbers between 0 and 1)
calculateDistanceArray(arguments:two integers, calculates distance between the point described by the integers and every point on the graph and returns an array of these distances)
nearestNeighborClassifier(takes the array from testCase(1*158) and finds the index of the minimum value and uses that and the classification array to classify the test case as 0 or 1, returns 0 or 1)
kNearestNeighborClassifier(takes in k and the calculateDistanceArray return, it finds the k smallest values in the array and averages them the rounds to determine what k nearest neighbors classifications are)
graphTestCase(takes in two integers and graphs them over the data)
glucose hemoglobin classification are global arrays.


K means clustering
k is a global integer
opencdkfile(no arguments, returns 3 1*158 arrays of glucose hemoglobin classification respectively)
normalizeData(argument: array of any length, returns an array where the smallest value is zero and the largest is one)
randomCentroids(no arguments, returns random value between 0 and 1)
calculateDistanceArray(arugments: two arrays, calculates distance between the points given by arrays and all the points, returns n*k array of distances where n is the number of data points)
nearestCentroid(arguments:n*k array, finds the nearest centroid to each point and returns a 1*n array)
newCentroid(arugments:1*n array, averages the glucose and hemoglobin or each group and gets new coordinates for centroid. returns two arrays of length k)
update(arguments: two arrays of length k, calls each function in succession beginning and ending with the same arguments allowing iterations over three functions)


