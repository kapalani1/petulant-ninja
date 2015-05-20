import copy

def create_rooted_spanning_tree(G, root):
    S = {}
    marked = {}
    graph = copy.deepcopy(G)
    S[root] = {}
    node = root
    for neighbor in graph[root]:
        if neighbor not in S:
            S[neighbor] = {}
        if neighbor in marked and node in marked:
            color = 'red'
        else:
            marked[neighbor] = True
            color = 'green'
            if neighbor not in S[node]:
                S[node][neighbor] = color
            if node not in S[neighbor]:
                S[neighbor][node] = color
    marked[node] = True    
    graph.pop(root)
    for node in graph:
        if node not in S:
            S[node] = {}
        for neighbor in graph[node]:
            if neighbor not in S:
                S[neighbor] = {}
            if neighbor in marked and node in marked:
                color = 'red'
            else:
                marked[neighbor] = True
                color = 'green'
            if neighbor not in S[node]:
                S[node][neighbor] = color
            if node not in S[neighbor]:
                S[neighbor][node] = color
        if node not in marked:
            marked[node] = True

    return S

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result
# feel free to edit the test to
# match the solution your program produces
def test_create_rooted_spanning_tree():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    S = create_rooted_spanning_tree(G,'a')
    assert S == {'a': {'c': 'green', 'b': 'green'}, 
                 'b': {'a': 'green', 'd': 'red'}, 
                 'c': {'a': 'green', 'd': 'green'}, 
                 'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
                 'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
                 'f': {'e': 'green', 'g': 'red'},
                 'g': {'e': 'green', 'f': 'red'} 
                 }

###########

def post_order(S, root):
    # return mapping between nodes of S and the post-order value
    # of that node
    po = {}
    pendingList = [];
    pendingList.append(root)
    counter = 0
    while len(pendingList)>0:
        node = pendingList[len(pendingList)-1]
        q = 0
        for neighbor in S[node]:
            if (S[node][neighbor] == 'green'):
                if neighbor in po or neighbor in pendingList:
                    q+=1
        if(q==S[node].values().count('green')):
            #all neighbors in pending list, so can assign value to node
            po[node] = counter+1
            counter+=1
            if node in pendingList:
                pendingList.remove(node)
        else:
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor not in pendingList:
                        pendingList.append(neighbor)
    return po

# This is just one possible solution
# There are other ways to create a 
# spanning tree, and the grader will
# accept any valid result.
# feel free to edit the test to
# match the solution your program produces
def test_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    assert po == {'a':7, 'b':1, 'c':6, 'd':5, 'e':4, 'f':2, 'g':3}

##############

def number_of_descendants(S, root):
    # return mapping between nodes of S and the number of descendants
    # of that node
    nd = {}
    pendingList = []
    pendingList.append(root)
    while(len(pendingList)>0):
        node = pendingList[len(pendingList)-1]
        q = 0
        for neighbor in S[node]:
            if (S[node][neighbor] == 'green'):
                if neighbor in nd or neighbor in pendingList:
                    q+=1
        if(q==S[node].values().count('green')):
            s = 1
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor in nd:
                        s+=nd[neighbor]
                    elif neighbor not in pendingList:
                        s+=1
            nd[node] =s
            pendingList.remove(node)
        else:
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor not in pendingList:
                        pendingList.append(neighbor)
    return nd

def test_number_of_descendants():
    S =  {'a': {'c': 'green', 'b': 'green'}, 
          'b': {'a': 'green', 'd': 'red'}, 
          'c': {'a': 'green', 'd': 'green'}, 
          'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
          'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
          'f': {'e': 'green', 'g': 'red'},
          'g': {'e': 'green', 'f': 'red'} 
          }
    nd = number_of_descendants(S, 'a')
    assert nd == {'a':7, 'b':1, 'c':5, 'd':4, 'e':3, 'f':1, 'g':1}

###############

def lowest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the lowest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    l = {}
    pendingList = []
    pendingList.append(root)
    while(len(pendingList)>0):
        node = pendingList[len(pendingList)-1]
        q = 0
        for neighbor in S[node]:
            if (S[node][neighbor] == 'green'):
                if neighbor in l or neighbor in pendingList:
                    q+=1
        if(q==S[node].values().count('green')):
            g = [po[node]]
            r = []
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor not in pendingList:
                        if neighbor in l:
                            g.append(l[neighbor])
                        else:
                            g.append(po[neighbor])
                else:
                    r.append(po[neighbor])
            if(len(r)==0 and len(g)==0):
                l[node]=po[node]
            elif(len(r)==0):
                l[node] = min(g)
            else:
                l[node] = min([min(g),min(r)])
            pendingList.remove(node)
        else:
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor not in pendingList:
                        pendingList.append(neighbor)
    return l

def test_lowest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    l = lowest_post_order(S, 'a', po)
    assert l == {'a':1, 'b':1, 'c':1, 'd':1, 'e':2, 'f':2, 'g':2}


################

def highest_post_order(S, root, po):
    # return a mapping of the nodes in S
    # to the highest post order value
    # below that node
    # (and you're allowed to follow 1 red edge)
    h = {}
    pendingList = []
    pendingList.append(root)
    while(len(pendingList)>0):
        node = pendingList[len(pendingList)-1]
        q = 0
        for neighbor in S[node]:
            if (S[node][neighbor] == 'green'):
                if neighbor in h or neighbor in pendingList:
                    q+=1
        if(q==S[node].values().count('green')):
            g = [po[node]]
            r = []
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor not in pendingList:
                        if neighbor in h:
                            g.append(h[neighbor])
                        else:
                            g.append(po[neighbor])
                else:
                    r.append(po[neighbor])
            if(len(r)==0 and len(g)==0):
                h[node]=po[node]
            elif(len(r)==0):
                h[node] = max(g)
            else:
                h[node] = max([max(g),max(r)])
            pendingList.remove(node)
        else:
            for neighbor in S[node]:
                if S[node][neighbor] == 'green':
                    if neighbor not in pendingList:
                        pendingList.append(neighbor)
    return h

def test_highest_post_order():
    S = {'a': {'c': 'green', 'b': 'green'}, 
         'b': {'a': 'green', 'd': 'red'}, 
         'c': {'a': 'green', 'd': 'green'}, 
         'd': {'c': 'green', 'b': 'red', 'e': 'green'}, 
         'e': {'d': 'green', 'g': 'green', 'f': 'green'}, 
         'f': {'e': 'green', 'g': 'red'},
         'g': {'e': 'green', 'f': 'red'} 
         }
    po = post_order(S, 'a')
    h = highest_post_order(S, 'a', po)
    assert h == {'a':7, 'b':5, 'c':6, 'd':5, 'e':4, 'f':3, 'g':3}
    
#################

def buildDependencyList(S,root):
    dependencyList = {}
    pendingList = []
    pendingList.append(root)
    while(len(pendingList)>0):
        node = pendingList.pop()
        if node not in dependencyList:
            dependencyList[node] = {}
        for neighbor in S[node]:
            if (S[node][neighbor] == 'green'):
                if neighbor not in pendingList and neighbor not in dependencyList:
                    dependencyList[node][neighbor] = 1
                    pendingList.append(neighbor)
    return dependencyList


def bridge_edges(G, root):
    # use the four functions above
    # and then determine which edges in G are bridge edges
    # return them as a list of tuples ie: [(n1, n2), (n4, n5)]
    S = create_rooted_spanning_tree(G,root)
    po = post_order(S,root)
    nd = number_of_descendants(S,root)
    l = lowest_post_order(S,root,po)
    h = highest_post_order(S,root,po)
    bridges = []
    dependencyList = buildDependencyList(S,root)
    nodesList = dependencyList.keys()
    nodesList.reverse()
    for node in nodesList:
        descendants = dependencyList[node].keys()
        for descendant in descendants:
            if(h[descendant]<=po[descendant] and l[descendant]>abs(nd[descendant]-po[descendant])):
                bridges.append((node,descendant))
    return bridges


def test_bridge_edges():
    G = {'a': {'c': 1, 'b': 1}, 
         'b': {'a': 1, 'd': 1}, 
         'c': {'a': 1, 'd': 1}, 
         'd': {'c': 1, 'b': 1, 'e': 1}, 
         'e': {'d': 1, 'g': 1, 'f': 1}, 
         'f': {'e': 1, 'g': 1},
         'g': {'e': 1, 'f': 1} 
         }
    bridges = bridge_edges(G, 'a')
    assert bridges == [('d', 'e')]

def tester():
    test_create_rooted_spanning_tree()
    test_post_order()
    test_number_of_descendants()
    test_lowest_post_order()
    test_highest_post_order()
    test_bridge_edges()
    print "Passed all tests"

tester()