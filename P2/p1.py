# @100405988
# @100405887
#we import the constraint library
import sys
import constraint
from constraint import *




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
            if (contM[i][2]=="1"and contM[j][2] == "2"):
                if args[i][1]>args[j][1] and args[j][0]==args[i][0]:
                    return False 

    return True

# def checkDepth1(*args):
#     ok=True
#     for i in range(len(args)):
#             for j in range(len(args)):
            
#                 if args[i][0] == args[j][0]+1 or args[i][0] == len(mapM) - 1 or mapM[args[i][0]+1][args[i][1]]=='X':
#                     ok= True
#                 else: ok=False 
#     return ok


def checkDepth2(*args):
    ok=True    
    for posi in args:
        if (mapM[posi[0]+1][posi[1]]=='N' or mapM[posi[0]+1][posi[1]]=='E'):
            ok=False
            for posj in args:
                if posi[0]+1==posj[0] and posi[1]==posj[1]:
                    ok=True    
            if not ok: return False
            
    return ok

def checkDepth23448(*args):
    ok=True
    for pos in args:
        if  alltheway(pos, args) or pos[0] == len(mapM) - 1 or mapM[pos[0]+1][pos[1]]=='X':
            ok= True
        else: return False 
    return ok

def alltheway(checkpos, *args):

    for auxpos in args:
        #print(args[j][0][0])
        if auxpos[0]==checkpos[0]+1 and auxpos[1]==checkpos[1]:
            return True
        
    return False

def main():
        # Reading input files and storing data into lists
    bay = open(sys.argv[1], 'r')
    global mapM
    mapM = []
    for row in bay:
        mapM.append(row.split())

    conts = open(sys.argv[2], 'r')
    global contM
    contM = []
    for row in conts:
        contM.append( row.split())
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
    problem.addConstraint(checkDepth2,)

    solutions = problem.getSolutions()
    print (" #{0} solutions have been found.".format(len(solutions)))
    output=sys.argv[1]+"-"+sys.argv[2]+".output"
    outfile=open(output, "w+")
    outfile.write("Number of solutions:"+str(len(solutions)))
    for line in solutions:
        outfile.write("\n"+str(line))
    # print(allpos)
    # print(electrified)
    # print(allconts)

if __name__ == '__main__':
    main()