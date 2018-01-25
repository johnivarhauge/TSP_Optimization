#!/usr/bin/python 
from random import randint

def generatepath(path, cityamount):

        notvisited = range(0,cityamount)
        for x in range(0,cityamount):
                notvisitedrandom = randint(0,len(notvisited)-1)
                path[x] = notvisited[notvisitedrandom]
                del(notvisited[notvisitedrandom])
        return 0

def calculatecost(cityamount, costmatrix, path):
        cost=0
        for x in range((len(path)-1)):
                cost = cost + costmatrix[path[x]][path[x+1]]
        cost = cost + costmatrix[path[cityamount-1]][path[0]]

        return cost

pathgenerated = 0
matrixgenerated = 0
cost = 0

while(1):
	if (cost != 0):
		print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nlowest cost so far: " + str(cost) +"...\n"
	print "Chose between the following options for TSP: \n"
	print "1. generate new matrix"
	print "2. random_method"
	print "3. random_iterative"
	print "4. greedy_method"
	print "5. greedy_improvement\n"
 
	print "end with ctrl-c\n"

	choice = int(raw_input(""));
	if (choice == 1):
		cityamount = int(raw_input("\nAmount of cities: \n"))
		costmatrix = [[0 for x in range(cityamount)] for y in range(cityamount)]
		for x in range(cityamount):
                	for y in range(cityamount):
                        	if (x > y):
                                	costmatrix[x][y] = randint(1,10)
                                	costmatrix[y][x] = costmatrix[x][y]
		matrixgenerated = 1
		pathgenerated = 0
		print "\nCity matrix has been generated with " + str(cityamount) + " cities\n"

	elif (choice == 2 and matrixgenerated == 1):
		path = [0 for x in range(0, cityamount)]
		generatepath(path, cityamount)
		pathgenerated = 1
		
	elif (choice == 3 and matrixgenerated == 1):
		iterations = 1000 
		#int(raw_input("\nAmount of iterations: "))
		bestpath = [0 for x in range(0, cityamount)]
		generatepath(bestpath, cityamount)
		cost = calculatecost(cityamount, costmatrix, bestpath)
		print "\nfirst path:" + str(cost) 
		path = [0 for x in range(0, cityamount)]
		for x in range(iterations):
                	generatepath(path, cityamount)
                	cost = calculatecost(cityamount, costmatrix, path)
                	if (cost < calculatecost(cityamount, costmatrix, bestpath)):
                        	bestpath=list(path)
		path=list(bestpath)
		pathgenerated = 1

	elif (choice == 4 and matrixgenerated == 1):
 		path = [0 for x in range(0, cityamount)]
		city=randint(0,cityamount)
       		path[0]=city
        	notvisited = range(0,cityamount)
        	del(notvisited[city])
        	for x in range(0, len(notvisited)):
                	bestpath=10
                	bestpos=0
                	for y in range(0,len(notvisited)):
                        	if (bestpath>costmatrix[path[x]][notvisited[y]]):
                                	bestpath=costmatrix[path[x]][notvisited[y]]
                                	bestpos=y
                	path[x+1]=notvisited[bestpos]
                	del(notvisited[bestpos])
		pathgenerated = 1

	elif (choice == 5):
		if (pathgenerated == 1):
			improvement_iterations = 1000 
			#int(raw_input("\nHow many iterations without change before ending improvement?\n")) + 1
			counter=0
        		while (counter<improvement_iterations):
                		newpath=list(path)
                		city1=randint(0,cityamount-1)
                		city2=randint(0,cityamount-1)
                		if (city1!=city2):
                        		newpath[city1]=path[city2]
                        		newpath[city2]=path[city1]
                        		cost1=calculatecost(cityamount, costmatrix, path)
                        		cost2=calculatecost(cityamount, costmatrix, newpath)
                        		if (cost1>cost2):
                                		path=list(newpath)
						counter = 0
                		counter=counter+1
		else: 
			print "\npath has to be generated first: pick 2,3 or 4"
	
	if (pathgenerated == 1 and matrixgenerated == 1):
		cost=calculatecost(cityamount, costmatrix, path)
		print "New cost: " + str(cost)
	elif (matrixgenerated != 1):
		print "\nMatrix has to be generated first\n"

#	raw_input("\nPress enter to continue...\n")

