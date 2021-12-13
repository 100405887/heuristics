# @100405988
# @100405887
#we import the constraint library
import constraint
from constraint import *

bay = open("map", 'r')
mapM = bay.read()
mapM = mapM.split(",")
# for row in bay:
#     mapM.append([int(x) for x in row.split()])

conts = open("container", 'r')
# contM = []
# for row in conts:
#     contM.append([int(x) for x in row.split()])

# def refrigerated(cont, space):
#     if cont=='R':
#         if space=='E':
#             return True
#         else: return False
#     return True

# def bottom(cont, bay, bayrowindex, baycolindex):

#     for i in bayrowindex:
#         if bay[bayrowindex][baycolindex]!='X':
#             return False
#     return True


if __name__ == '__main__':
    # problem = constraint.Problem()
    # #adding the variables with their domains
    # allpos={}
    # electrified={}
    # allconts={}
    # for conts in contM:
    #     allconts.append(conts)
    # for spots in mapM:
    #     allpos.append(spots)
    # for spotsE in mapM:
    #     if spotsE=='E':
    #         electrified.append(spotsE)
    # for conts in contM:
    #     if conts[1]=='S':
    #         problem.addVariable(conts[0],[allpos])
    #     if conts[1]=='R':
    #         problem.addVariable(conts[0],[electrified])

    # problem.addConstraint(AllDifferentConstraint(), allconts)

    # solutions = problem.getSolutions()
    # print (" #{0} solutions have been found.".format(len(solutions)))
    # print(solutions)
    print(mapM)