# @100405988
# @100405887
#we import the constraint library
import constraint
from constraint import *

# Reading input files and storing data into lists
bay = open("map", 'r')
mapM = []
for row in bay:
    mapM.append(row.split())

conts = open("container", 'r')
contM = []
for row in conts:
    contM.append( row.split())


def bottom(cont, bay, bayrowindex, baycolindex):

    for i in bayrowindex:
        if bay[bayrowindex][baycolindex]!='X':
            return False
    return True

# def ports(*args):
#     for i in range(len(args)):
#         for j in range(len(args)):
#             if 
    
#     return True

if __name__ == '__main__':
    problem = constraint.Problem()
    #adding the variables with their domains
    # All positions
    allpos=[]
    # All positions with power supply
    electrified=[]
    # Every container
    allconts=[]
    for conts in contM:
        allconts.append(conts[0])
    for i in range(len(mapM)):
        for j in range(len(mapM[i])):
            if mapM[i][j] !='X':
                allpos.append([i,j])
    for i in range(len(mapM)):
        for j in range(len(mapM[i])):
            if mapM[i][j]=='E':
                electrified.append([i,j])
    for conts in contM:
        if conts[1]=='S':
            problem.addVariable(conts[0],allpos)
        if conts[1]=='R':
            problem.addVariable(conts[0],electrified)

    # problem.addConstraint(AllDifferentConstraint(), allconts)
    # problem.addConstraint(setPorts(), allconts)
    # problem.addConstraint(checkDepth(), allconts)

    # solutions = problem.getSolutions()
    # print (" #{0} solutions have been found.".format(len(solutions)))
    # print(solutions)
    print(allpos)
    print(electrified)
    print(allconts)
