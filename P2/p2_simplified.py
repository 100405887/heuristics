# ---------------------- A* ---------------------- #
class Graph:













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

    def load(self, containerId, newPosition):
        for range in self.containers:
            if range.id == containerId:
                range.coordinates[0] = newPosition[0]
                range.coordinates[1] = newPosition[1]

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

