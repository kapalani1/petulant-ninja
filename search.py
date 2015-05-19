# -----------
# User Instructions:
# 
# Modify the function search so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# Make sure that the initial cell in the grid 
# you return has the value 0.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def searchHelper(grid,init,goal,cost,visited,o,expansion,ctr,backpointer):
    expansion[o[0][1][0]][o[0][1][1]] = ctr;
    visited[o[0][1][0]][o[0][1][1]] = -1;
    if(visited[goal[0]][goal[1]]==-1):
        return backpointer
    for i in xrange(len(delta)):
        [newX,newY] = [o[0][1][0]+delta[i][0],o[0][1][1]+delta[i][1]];
        if(newX<0 or newX>=len(grid) or newY<0 or newY>=len(grid[0])):
            continue
        elif(visited[newX][newY]==0):
            grid[newX][newY] = grid[o[0][1][0]][o[0][1][1]]+1
            expansion[newX][newY] = grid[newX][newY]
            o.append((grid[newX][newY],[newX,newY]))
            backpointer[newX][newY] = (newX,newY)
            visited[newX][newY] = -1
    o.pop(0)
    if(len(o)==0):
        return 'fail'
    else:
        o.sort(key=lambda x:x[0])
        for i in xrange(len(o)):
            ctr+=1
            ret =searchHelper(grid,init,goal,cost+1,visited,o,expansion,ctr,backpointer) 
            if(ret!='fail'):
                return ret
        return 'fail'

def pretty(backpointer,init,goal,grid):
    for i in xrange(len(backpointer)):
        print backpointer[i]
    path = [[' ' for i in xrange(len(backpointer[0]))] for j in xrange(len(backpointer))]
    path[goal[0]][goal[1]] = '*'
    IamAt = goal
    while(True):
        for i in xrange(len(delta)):
            d = delta[i]
            newX = IamAt[0]-d[0];
            newY = IamAt[1]-d[1];
            if(newX<0 or newX>=len(backpointer) or newY<0 or newY>=len(backpointer[0])):
                continue
            if(abs((backpointer[newX][newY][0]-IamAt[0]) + (backpointer[newX][newY][1]-IamAt[1])) == 1):
                print IamAt
                print newX,newY
                if(grid[newX][newY]<grid[IamAt[0]][IamAt[1]]):
                    pos = [backpointer[newX][newY][0],backpointer[newX][newY][1]]
                    print "SET POS"
                    break
        cameFrom = pos
        if(IamAt==cameFrom):
            break
        for i in xrange(len(path)):
            print path[i]
        dirVector = [IamAt[0]-cameFrom[0],IamAt[1]-cameFrom[1]]
        dirIndex = delta.index(dirVector)
        path[cameFrom[0]][cameFrom[1]] = delta_name[dirIndex];
        IamAt = [cameFrom[0],cameFrom[1]];
    return path    

def search(grid,init,goal,cost):
    visited=[];
    expansion = [];
    backpointer = []
    for i in xrange(len(grid)):
        x=[];
        y = [];
        z = []
        for j in xrange(len(grid[0])):
            x.append(grid[i][j]);
            z.append((0,0))
            if(grid[i][j]==0):
                y.append(0);
            else:
                y.append(-1)
        visited.append(x);
        expansion.append(y)
        backpointer.append(z)
    return pretty(searchHelper(grid,init,goal,cost,visited,[(0,init)],expansion,0,backpointer),init,goal,grid)

s = search(grid,init,goal,cost)
for i in xrange(len(s)):
    print s[i]