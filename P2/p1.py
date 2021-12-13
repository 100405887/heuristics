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

# def differentMAL(*args):
#     for i in args:
#         repetitions=0
#         for j in args:
#             if (i == j):
#                 repetitions+=1
#         if repetitions>1:
#             return False
#     return True

def different(*args):
    for i in range(len(args)):
        for j in range(len(args)):
            if i!=j:
                if args[i] == args[j]:
                    return False 
    return True

def setPorts(*args):
    for i in range(len(args)):
        for j in range(len(args)):
            if (contM[i][2]==1 and contM[j][2] == 2):
                for x in range(len(args)):
                    for y in range(len(args)):
                        if args[i][x][1]>args[i][y][1] and x==y:
                            return False 

    return True

def checkDepth1(*args):
    for i in range(len(args)):
        for j in range(len(args)):
            if i!=j:
                if args[i][0] == args[j][0]+1 or args[i][0] == len(mapM) - 1 or args[i][0]+1=='X':
                    return True
    return False

def checkDepth2(*args):
    ok=True    
    for i in args:
        ok=False
        posi=i
        for j in args:
            posj=j
            if ((posj[1]-posi[1])<2 or (mapM[posi[0]][posi[1]+1]!='S' and mapM[posi[0]][posi[1]+1]!='E')):
                ok=True
    return ok


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

     
    #problem.addConstraint(AllDifferentConstraint(), range(0,len(allconts)))
   
    

    problem.addConstraint(different,)
    problem.addConstraint(setPorts,)
    problem.addConstraint(checkDepth1,)

    solutions = problem.getSolutions()
    print (" #{0} solutions have been found.".format(len(solutions)))
    #print(solutions)
    # print(allpos)
    # print(electrified)
    # print(allconts)
