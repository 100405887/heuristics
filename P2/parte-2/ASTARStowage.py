import sys
# Containers coordinates are expressed as follows: 
# Containers coordinates when at any port: [-1, -1] | Containers coordinates when loaded on ship bay: [stack, depth]

class container: 
    def __init__(self, id, coordinates, type_):
        self.id = id
        self.coordinates = coordinates
        self.type_ = type_
        
    def __str__(self):
        ans = str(self.id) + ", " + str(self.coordinates) + ", " + str(self.type_)
        return ans

# ---------------------- A* ---------------------- #

class Node:
    def __init__(self, containers, parent=None):

        self.parent = parent
        self.containers = containers

        self.g = 0
        self.h = 0
    
    def __str__(self):
        printer = ""
        for cont in self.containers:
            printer += str(cont) + " ; "
        return printer 

    def __eq__(self, other):
        # return self.containers == other.containers # and self.parent == other.parent
        for contSelf in self.containers:
            for contOther in other.containers:
                if contSelf.id == contOther.id and (contSelf.coordinates[0]!=contOther.coordinates[0] or contSelf.coordinates[1]!=contOther.coordinates[1]):
                    return False
        return True

    def load(self, containerId, newPosition, mapa):
        # Copy containers list of node to operate with new node
        nextContainers = []
        for cont in self.containers:
            newCoordinates = []
            for coords in cont.coordinates:
                newCoordinates.append(coords)
            newCont = container(cont.id, newCoordinates, cont.type_)
            nextContainers.append(newCont)
        nextState = Node(nextContainers, self)
        
        for cont in nextContainers:
            if cont.id == containerId:
                cont.coordinates[0] = newPosition[0]
                cont.coordinates[1] = newPosition[1]
        
        nextState.setG(self.g, newPosition)
        nextState.setH(mapa)

        return nextState
    
    def getF(self):
        return self.g + self.h
    
    def setG(self, parentG, loadPosition):
        self.g = parentG + 10 + loadPosition[0]
    
    def getG(self):
        return self.g

    def setH(self, mapa):
        
        sumDepthN = 0
        sumDepthE = 0
        nN = 0
        nE = 1
        nS = 0
        nR = 0
        for cont in self.containers: 
            if cont.type_ == "S" and cont.coordinates[0]==-1:
                nS += 1
            if cont.type_ == "R" and cont.coordinates[0]==-1:
                nR += 1
        for i in range(len(mapa)):
            for j in range(len(mapa[i])):
                if mapa[i][j] == "N" and cellIsEmpty(self.containers, i,j): 
                    nN += 1
                    sumDepthN += i
                if mapa[i][j] == "E" and cellIsEmpty(self.containers, i,j):
                    nE += 1
                    sumDepthE += i
        averageDepthE = sumDepthE/nE
        averageDepth = (sumDepthE+sumDepthN)/(nE+nN)

        self.h = nS*(10+averageDepth) + nR*(10+averageDepthE)
        
    def getH(self):
        return self.h
    
    def getChildren(self, mapa):
        children = []
        #Precondiciones load 
        for cont in self.containers: # Comprobar todos los contenedores...
            for i in range(len(mapa)):
                for j in range(len(mapa[i])): # ...en todas las posiciones posibles
                    #print(cont.type_ + ";" + mapa[i][j] + ";" + str(cont.id) + '\n')
                    if cont.type_ == "S" and mapa[i][j] != "X" and cellIsEmpty(self.containers, i, j) and (not cellIsEmpty(self.containers, i+1, j) or i+1 >= len(mapa) or mapa[i+1][j]=="X"):
                        #print('Loading container ' + str(cont.id) + ' in ' + str(i) + ',' + str(j) + "\n")
                        children.append(self.load(cont.id, [i, j], mapa))
                    if cont.type_ == "R" and mapa[i][j] == "E" and cellIsEmpty(self.containers, i, j) and (not cellIsEmpty(self.containers, i+1, j) or i+1 >= len(mapa) or mapa[i+1][j]=="X"):
                        #print('Loading container ' + str(cont.id) + ' in ' + str(i) + ',' + str(j) + "\n")
                        children.append(self.load(cont.id, [i, j], mapa))
        #Precodiciones unload
        #Precondiciones sail
        return children 
    
    def isGoal(self):
        # Si todos los contenedores est??n colocados en algun punto del barco, es meta
        for cont in self.containers:
            if cont.coordinates[0] == -1:
                return False
        return True

def aStar(start, mapa):
   
    openList = [start]
    closeList = []
    exitAStar = False

    start.setH(mapa) # Calcula h(n) del nodo inicial
    n = None
    while len(openList) != 0 and exitAStar == False:
        n = openList.pop(0)
        if n.isGoal(): # isGoal() analiza si el nodo n contiene el estado final
            exitAStar = True
        else:
            closeList = insertOrdered(closeList, n) # inserta en orden segun f(n)
            s = n.getChildren(mapa) # getChildren() debe devolver lista sucesores
            prev = s[0]
            for nod in s:
                if nod in closeList: 
                    print('Node already in close list')
                    continue # Ignore it. (This if/else structure saves up unnecessary condition checks) 
                else:
                    if nod not in openList and nod not in closeList:
                        #print('Inserting node in openList')
                        openList = insertOrdered(openList, nod)
                        #print(openList)
                    if nod in openList and nod.getF() < prev.getF():
                        #print('Inserting better node in openList')
                        openList.remove(prev)
                        openList = insertOrdered(openList, nod)
                    # In case of draw in f(n) value, we take smallest h(n). If h(n) is equal too, nothing happens 
                    if nod in openList and nod.getF() == prev.getF() and nod.h < prev.h:
                        openList.remove(prev)
                        openList = insertOrdered(openList, nod)
                prev = nod # Update previous element saved to compare
    if exitAStar:
        solution = getSolutionsPath(n) # Returns list of nodes from start to goal 
    else:
        solution = False 

    return solution

def insertOrdered(thisList, node):
    if len(thisList) == 0:
        thisList.append(node)
    for i in range(len(thisList)):
        #print((thisList[i].getF()))
        if thisList[i].getF() > node.getF() or (thisList[i].getF() == node.getF() and thisList[i].h >= node.h):
            #for elem in thisList:
                #print(str(elem) + "; ")
            #print('inserting for real')
            thisList.insert(i, node)
            # for elem in thisList:
            #     print(str(elem) + "; ")
        
    return thisList

def getSolutionsPath(nod):
    path = []
    while nod.parent is not None:
        path.insert(0, nod) # Inserting at beginning so that path is start-end ordered
        nod = nod.parent
    return path

def cellIsEmpty(containers, i, j):
    for cont in containers:
        if cont.coordinates[0] == i and cont.coordinates[1] == j:
            return False
    return True 

''' INTENTO GETPATH RECURSIVO
def getPath(listaNodos, a, b):
    if a is b:
        return listaNodos
    else :
        listaNodos.append(getPath(b.parent, b))
'''

def main():

    path=sys.argv[1]+"/"
    map=sys.argv[2]
    containers=sys.argv[3]

    # Reading input files and storing data into matrix (arrays of arrays to define map and list of containers w/ different attributes)
    bay = open(path+map, 'r')
    global mapM
    mapM = []
    for row in bay:
        mapM.append(row.split())

    conts = open(path+containers, 'r')
    global contM
    contM = []
    for row in conts:
        contM.append( row.split())

    myContainers = []
    for cont in contM:
        id = int(cont[0]) 
        type_ = cont[1]
        newContainer = container(id, [-1,-1], type_)
        myContainers.append(newContainer)

    # Three initial containers
    # container1 = container(0, [-1,-1], "S")
    # container2 = container(1, [-1,-1], "R")
    # container3 = container(2, [-1,-1], "S")
    #Creating a list of containers for my problem
    
    # myContainers.append(container1)
    # myContainers.append(container2)
    # myContainers.append(container3)

    #Defining initial state
    start = Node(myContainers)
    solution = aStar(start, mapM)
    if solution == False: 
        print ('No solution found')
    else: 
        print (solution)

    # print(mapM)
    # print(contM) 
    # for cont in start.containers:
    #     print(cont)

    # print('Loading container 1...') 
    # start.load(1,[2,2], mapM)

    # for cont in start.containers:
    #     print(cont) 

    # print(start)
    # print('Getting sucessors...')
    # sucesores = start.getChildren(mapM)
    # i = 1
    # for node in sucesores:
    #     print(str(i) +".- "+ str(node) + "\n")
    #     i += 1
    
if __name__ == '__main__':
    main()