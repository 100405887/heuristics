# @100405988
# @100405887
#we import the constraint library
import sys
import constraint
from constraint import *


def different(*args):
    for i in range(len(args)):
        for j in range(len(args)):
            if i!=j:
                if args[i] == args[j]:
                    return False 
    return True

def checkports(first, second):
    if first[1]<second[1] and first[0]==second[0]:
        return False
    return True
    
def checkDepth(*args):
    ok=True    
    for posi in args:
        if posi[1] != len(mapM[0]) - 1:
            if (mapM[posi[1]+1][posi[0]]=='N' or mapM[posi[1]+1][posi[0]]=='E'):
                ok=False
                for posj in args:
                    if posi[1]+1==posj[1] and posi[0]==posj[0]:
                        ok=True    
                if not ok: return False           
    return ok

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
                allpos.append([j,i])

    #available electrified positions in the matrix          
    for i in range(len(mapM)):
        for j in range(len(mapM[i])):
            if mapM[i][j]=='E':
                electrified.append([j,i])

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