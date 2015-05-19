# Find Eulerian Tour given a graph with edges
# Recursive solution using backtracking

def findNeighbors(popList,currentNode):
    neighbors = []
    for i in xrange(len(popList)):
        if(popList[i][0]==currentNode):
            neighbors.append(popList[i][1])
        elif(popList[i][1]==currentNode):
            neighbors.append(popList[i][0])
    return neighbors

def findIndexOfEdge(popList,currentNode,neighbour):
    edge1 = (currentNode,neighbour)
    edge2 = (neighbour,currentNode)
    for i in xrange(len(popList)):
        if(popList[i]==edge1 or popList[i]==edge2):
            return i

def find_eulerian_tour_helper(tour,startNode,currentNode,popList):
    if(currentNode==startNode and len(popList)==0):
        tour.append(startNode)
        return tour
    else:
        tour.append(currentNode)
        neighbours = findNeighbors(popList,currentNode)
        for neighbour in neighbours:
            #for every neighbor try to find the eulerian path
            index = findIndexOfEdge(popList,currentNode,neighbour)
            popList.pop(index)
            currentNode = neighbour
            sol = find_eulerian_tour_helper(tour,startNode,currentNode,popList)
            if (sol is not None):
                #found solution 
                return sol
            else:
                #couldn't find solution :(
                #remove the last edge you added and try again
                n = tour.pop()
                popList.append((n,tour[len(tour)-1]))
                currentNode = tour[len(tour)-1]
        return None

def find_eulerian_tour(graph):
    popList = []
    for i in xrange(len(graph)):
        popList.append(graph[i])
    startNode = graph[0][0];
    currentNode = graph[0][1];
    tour = [startNode]
    popList.pop(0)
    return find_eulerian_tour_helper(tour,startNode,currentNode,popList)


def testEulerianTour():
    print find_eulerian_tour([(1,2),(2,3),(3,1)])
    print find_eulerian_tour([(0,1),(0,3),(1,3),(1,4),(1,2),(3,2),(3,4)])
    print find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13),
    (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
    (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
    (7, 14),  (10, 13)])
    print find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19),
    (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
    (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
    (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)])

testEulerianTour()
