# Search

# Locations for both ship and containers are expressed as follows: 
# Initial port: 0 | First port: 1 | Second port: 2
# Containers coordinates are expressed as follows: 
# Containers at any port: [-1, -1] | Containers loaded: [stack, depth]



def state(int shipLocation, List containers, self): 
    self.containers = containers
    self.shipLocation = shipLocation 

def container(int id, int containerLocation, List coordinates, int destination, Boolean state, self):
    self.id = idContainer
    self.containerLocation = containerLocation
    self.coordinates = coordinates
    self.destination = destination 
    self.state = state

def sail(state stateNow, int newShipLocation):
    stateNow.ship = newShipLocation
    for range in stateNow.containers:
        if stateNow.containers[range].coordinates[0] != -1:
            stateNow.containers[range].containerLocation = newShipLocation

def load(state stateNow, int containerId, List newPosition):
    for range in stateNow.containers:
        if stateNow.containers[range] == containerId:
            stateNow.containers[range].coordinates[0] = newPosition[0]
            stateNow.containers[range].coordiantes[1] = newPosition[1]
            #stateNow.containers[range].containerLocation = stateNow.shipLocation
            if stateNow.containers[range].containerLocation = stateNow.containers[range].destination:
                stateNow.containers[range].state = True

def unload(stateNow, int containerId):

def gFunction():

def hFunction():

def heuristicFunction():

def main():
    # example of container in origin port 
    container container1 = new container(0, [-1,-1], 1, false)
    # example of container loaded in (3,2)
    container container2 = new container(-1, [3,2], 2, false)
    #example of container in port 2 reaching its destination
    container container3 = new container(2, [-1,-1], 1, true)
    #Creating a list of containers for my problem
    myContainers = []
    myCointainers.append(container1)
    myCointainers.append(container2)
    myCointainers.append(container3)
    #Defining initial state with ship at initial port
    state myState = new state(myContainers, 0)

if __name__ == '__main__':
    main()