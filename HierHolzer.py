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

def findNextStartNode(popList,tour):
    for node in tour:
        n = findNeighbors(popList,node)
        if len(n)>0:
            return (node,n)

def joinTours(tour1, tour2):
    if(tour1==[]):
        return tour2
    else:
        i = tour1.index(tour2[0])
        return tour1[:i]+tour2+tour1[i+1:]

def find_eulerian_tour(graph):
    popList = graph
    startNode = graph[0][0];
    currentNode = graph[0][1];
    tour = [startNode]
    popList.pop(0)
    eulerian = []
    while(len(popList)>0):
        while(currentNode!=startNode):
            tour.append(currentNode)
            neighbors = findNeighbors(popList,currentNode)
            if(len(neighbors)==0):
                print "No neighbors"
                return None
            popList.pop(findIndexOfEdge(popList,currentNode,neighbors[0]))
            currentNode = neighbors[0]
        tour.append(startNode)
        eulerian = joinTours(eulerian,tour)
        if(len(popList)==0):
            break
        (startNode,n) = findNextStartNode(popList,eulerian)
        currentNode = n[0];
        popList.pop(findIndexOfEdge(popList,startNode,currentNode))
        tour = []
        tour.append(startNode)
    return eulerian

def testEulerianTour():
    find_eulerian_tour([(1,2),(2,3),(3,1)])
    find_eulerian_tour([(0,1),(0,3),(1,3),(1,4),(1,2),(3,2),(3,4)])
    find_eulerian_tour([(1, 13), (1, 6), (6, 11), (3, 13),
    (8, 13), (0, 6), (8, 9),(5, 9), (2, 6), (6, 10), (7, 9),
    (1, 12), (4, 12), (5, 14), (0, 1),  (2, 3), (4, 11), (6, 9),
    (7, 14),  (10, 13)])
    find_eulerian_tour([(8, 16), (8, 18), (16, 17), (18, 19),
    (3, 17), (13, 17), (5, 13),(3, 4), (0, 18), (3, 14), (11, 14),
    (1, 8), (1, 9), (4, 12), (2, 19),(1, 10), (7, 9), (13, 15),
    (6, 12), (0, 1), (2, 11), (3, 18), (5, 6), (7, 15), (8, 13), (10, 17)])
    find_eulerian_tour([(1,2),(2,3),(3,4),(1,4),(4,7),(3,5),(4,5),(3,7),
        (5,6),(6,7),(7,8),(5,8),(5,9),(7,11),(5,11),(7,9)])
    find_eulerian_tour([(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 2)])
    find_eulerian_tour([(0, 1), (1, 2), (2, 5), (2, 3), (3, 0),
    (1,4),(1,5),(2,4)]) 

testEulerianTour()

use_harder_tests=True
