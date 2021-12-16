# @100405988
# @100405887
#we import the constraint library
import sys
import constraint
from constraint import *




# def bottom(cont, bay, bayrowindex, baycolindex):

#     for i in bayrowindex:
#         if bay[bayrowindex][baycolindex]!='X':
#             return False
#     return True

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



# def checkDepth1(*args):
#     ok=True
#     for i in range(len(args)):
#             for j in range(len(args)):
            
#                 if args[i][0] == args[j][0]+1 or args[i][0] == len(mapM) - 1 or mapM[args[i][0]+1][args[i][1]]=='X':
#                     ok= True
#                 else: ok=False 
#     return ok

def checkports(first, second):
    if first[0]<second[0] and first[1]==second[1]:
        return False
    return True
    
def checkDepth(*args):
    ok=True    
    for posi in args:
        if posi[0] != len(mapM) - 1:
            if (mapM[posi[0]+1][posi[1]]=='N' or mapM[posi[0]+1][posi[1]]=='E'):
                ok=False
                for posj in args:
                    if posi[0]+1==posj[0] and posi[1]==posj[1]:
                        ok=True    
                if not ok: return False           
    return ok

# def checkDepth23448(*args):
#     ok=True
#     for pos in args:
#         if  alltheway(pos, args) or pos[0] == len(mapM) - 1 or mapM[pos[0]+1][pos[1]]=='X':
#             ok= True
#         else: return False 
#     return ok

# def alltheway(checkpos, *args):

#     for auxpos in args:
#         #print(args[j][0][0])
#         if auxpos[0]==checkpos[0]+1 and auxpos[1]==checkpos[1]:
#             return True
        
#     return False

def main():
    #Reading arguments from .sh and assigning them to the  corresponding variables    
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

    #creating problem ini constraint library    
    problem = constraint.Problem()
    # All positions
    allpos=[]
    # All positions with power supply
    electrified=[]
    # Every container
    allconts=[]

    #filling previous arrays with corresponding data from recently created matrixes
    #container identificators to use as variables
    for conts in contM:
        allconts.append(conts[0])

    #all available positions in the matrix     
    for i in range(len(mapM)):
        for j in range(len(mapM[i])):
            if mapM[i][j] !='X':
                allpos.append([i,j])

    #available electrified positions in the matrix          
    for i in range(len(mapM)):
        for j in range(len(mapM[i])):
            if mapM[i][j]=='E':
                electrified.append([i,j])

    #adding the variables with their domains according to the type of container
    for conts in contM:
        if conts[1]=='S':
            problem.addVariable(conts[0],allpos)
        if conts[1]=='R':
            problem.addVariable(conts[0],electrified)

     
    #problem.addConstraint(AllDifferentConstraint(), range(0,len(allconts)))
   
   #creating the constraints in the library using our defined methods, without providing variables as they will apply to every
   #variable created for each execution, which will differ according to the data received in the containers file
    problem.addConstraint(different,)

    for a in contM:
        for b in contM:
            if a[2]=='2' and b[2]=='1':
                problem.addConstraint(checkports,[a[0],b[0]])

    problem.addConstraint(checkDepth,)

    #obtaining our solutions
    solutions = problem.getSolutions()

    #printing in terminal the amount of solutions found to have an idea of wether it worked without requiring opening the output file
    print (" #{0} solutions have been found.".format(len(solutions)))

    #creating the output file with the indicated name into the folder where the input data was stored and opening it with write permission
    output=path+map+"-"+containers+".output"
    outfile=open(output, "w+")

    #writing the amount of solutions found
    outfile.write("Number of solutions:"+str(len(solutions)))

    #writing each possible solution found into a line 
    for line in solutions:
        outfile.write("\n"+str(line))
    # print(allpos)
    # print(electrified)
    # print(allconts)

if __name__ == '__main__':
    main()