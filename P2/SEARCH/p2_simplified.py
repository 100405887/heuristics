'''
class state:
    def __init__(self, containers):
        self.containers = containers 

    def load(self, containerId, newPosition):
        for cont in self.containers:
            if cont.id == containerId:
                cont.coordinates[0] = newPosition[0]
                cont.coordinates[1] = newPosition[1]

    def load(self, containerId, newPosition):
        # Copy containers list state to operate with new state
        nextContainers = self.containers.copy()
        nextState = state(nextContainers)
        
        for cont in nextContainers:
            if cont.id == containerId:
                cont.coordinates[0] = newPosition[0]
                cont.coordinates[1] = newPosition[1]
                
        return nextState
'''
# ------------------------ Search simplified ------------------------ #

# Containers coordinates are expressed as follows: 
# Containers at any port: [-1, -1] | Containers loaded: [stack, depth]
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

    def __eq__(self, other):
        return self.containers == other.containers # and self.parent == other.parent
    
    def load(self, containerId, newPosition):
        for cont in self.containers:
            if cont.id == containerId:
                cont.coordinates[0] = newPosition[0]
                cont.coordinates[1] = newPosition[1]

    def load(self, containerId, newPosition):
        # Copy containers list of node to operate with new node
        nextContainers = self.containers.copy()
        nextState = Node(nextContainers, self.parent)
        
        for cont in nextContainers:
            if cont.id == containerId:
                cont.coordinates[0] = newPosition[0]
                cont.coordinates[1] = newPosition[1]
                
        return nextState
    
    def getF(self):
        return self.g + self.h
    
    def getChildren(self, node, map):
        children = []
        #Precondiciones load 
        for cont in node.containers: # Comprobar todos los contenedores...
            for i in range(len(map)):
                for j in range(len(map[i])): # ...en todas las posiciones posibles
                    if cont.type_ == "S" and map[i][j] != "X" and cellIsEmpty(map, i, j) and not cellIsEmpty(map, i+1, j):
                        children.append(node.load(cont.id, possiblePosition))
                    if cont.type_ == "R" and map[i][j] == "E" and cellIsEmpty(map, i, j) and not cellIsEmpty(map, i+1, j):
                        children.append(node.load(cont.id, possiblePosition))
        #Precodiciones unload
        #Precondiciones sail
        return children 

    def cellIsEmpty(map, i, j):
        for cont in self.containers:
            if cont.coordinates[0] == i and cont.coordinates[1] == j:
                return False
        return True 
    
    def isGoal(self):
        # Si todos los contenedores están colocados en algun punto del barco, es meta
        for cont in self.containers:
            if cont.coordinates[0] == -1:
                return False
        return True

def aStar(start):
   
    openList = [start]
    closeList = []
    exitAStar = False

    while len(openList) != 0 and exitAStar == False:
        n = openList.pop(0)
        if n.isGoal(): # isGoal() analiza si el nodo n contiene el estado final
            exitAStar = True
        else:
            insertOrdered(closeList, n) # inserta en orden segun f(n)
            s = n.getChildren() # getChildren() debe devolver lista sucesores
            prev = s[0]
            for nod in s:
                if nod in close: 
                    continue # Ignore it. (This if/else structure saves up unnecessary condition checks) 
                else:
                    if nod not in openList and nod not in closeList:
                        insertOrdered(openList, nod)
                    # ¡¡¡REVISAR esta condicion para añadir el caso en que hay empate en valor de f(n)!!!
                    if nod in openList and nod.getF() < prev.getF():
                        openList.remove(prev)
                        insertOrdered(openList, nod)
                prev = nod # Update previous element saved to compare
    if exitAStar:
        solution = getPath(start, end) # Returns list of nodes from start to goal 
    else:
        solution = False 

def insertOrdered(thisList, node):
    for i in range(len(thisList)):
        if thisList[i].getF() > node.getF():
            thisList.insert(i, node)

def getPath(a, b):
    path = []
    while b is not a:
        path.insert(0, b) # Inserting at beginning so that path is start-end ordered
        b = b.parent
    return path

''' INTENTO GETPATH RECURSIVO
def getPath(listaNodos, a, b):
    if a is b:
        return listaNodos
    else :
        listaNodos.append(getPath(b.parent, b))
'''
if __name__ == '__main__':

    bay = open("map_simp", 'r')
    #global mapM
    mapM = []
    for row in bay:
        mapM.append(row.split())

    conts = open("containers_simp", 'r')
    #global contM
    contM = []
    for row in conts:
        contM.append(row.split())

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
    myState = Node(myContainers)

    print(mapM)
    print(contM) 
    for cont in myContainers:
        print(cont)

    print('Loading container 1...') 
    myState.load(1,[2,2])

    for cont in myContainers:
        print(cont) 

