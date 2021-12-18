
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

class state:
    def __init__(self, containers):
        self.containers = containers 
        self.g = 0
        self.h = 0

    def load(self, containerId, newPosition):
        for range in self.containers:
            if range.id == containerId:
                range.coordinates[0] = newPosition[0]
                range.coordinates[1] = newPosition[1]


# ---------------------- A* ---------------------- #

class Node:
    def __init__(self, parent=None, estado):

        self.parent = parent
        self.estado = estado

        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def getF(self):
        return self.g + self.h
    
    def getChildren(self, node):
        #Precodiciones
        children = []
        for range in node.estado.containers:
            for possiblePosition in listaPosiciones:
                if huecoDisponibleDelTipo and noHuecoVacioDebajo:
                    children.append(node.estado.load(range.id, possiblePosition))
        return children 
    
    def isGoal(self):
        # Si todos los contenedores están colocados en algun punto del barco, es meta
        for range in self.estado.containers:
            if range.coordinates[0] == -1:
                return False
        return True

def aStar(start):
   
    openList = [start]
    closeList = []
    exitAStar = False

    while len(openList) != 0 or exitAStar == False:
        n = openList.pop(0)
        if n.isGoal(): # isGoal() analiza si el nodo n contiene el estado final
            exitAStar = True
        else:
            insertOrdered(closeList, n) # inserta en orden segun f(n)
            s = n.getChildren() # getChildren() debe devolver lista sucesores
            prev = s[0]
            for range in s:
                if range in close: 
                    continue # Ignore it. (This if/else structure saves up unnecessary condition checks) 
                else:
                    if range not in openList and range not in closeList:
                        insertOrdered(openList, range)
                    if range in openList and range.getF() < prev.getF():
                        openList.remove(prev)
                        insertOrdered(openList, range)
                prev = range # Update previous element saved to compare
    if exitAStar:
        solution = getPath() # Define getPath() to return path form N to I through pointers
    else:
        solution = False 

def insertOrdered(thisList, node):
    for i in range(len(thisList)):
        if thisList[i].getF() > node.getF():
            thisList.insert(i, node)

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
    for range in contM:
        id = int(range[0]) 
        type_ = range[1]
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
    myState = state(myContainers)

    print(mapM)
    print(contM) 
    for range in myContainers:
        print(range)

    print('Loading container 1...') 
    myState.load(1,[2,2])

    for range in myContainers:
        print(range) 

