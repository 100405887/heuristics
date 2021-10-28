###### Setting up variables ######
set LOCATION; 
set DISPONIBILITY;
# Cost of moving a scooter from LOCATION m to LOCATION n
param COST{m in LOCATION, n in LOCATION};
# AVAILABILITY stores number of scooters available or demanded per LOCATION
param AVAILABILITY{a in LOCATION, b in DISPONIBILITY};
# Decision variables named DISPLACEMENT 
# counting number of displacements from LOCATION m to LOCATION n
var DISPLACEMENT{m in LOCATION, n in LOCATION} integer, >= 0; 
###### Objective function ######
minimize GOAL: sum{m in LOCATION, n in LOCATION} DISPLACEMENT[m,n]*COST[m,n];
###### Constraints ###### 
######################################REVISAR CONSTRAINTS
# Every available location must share at least 90% of their scooters available
s.t. share90 {m in LOCATION: AVAILABILITY[0,m]>0}: 
    sum{n in LOCATION} DISPLACEMENT[m,n] >= 0.9*AVAILABILITY[0,m];
    
# Scooters leaving an available location must be at least equal to total demand 
s.t. arriving: 
    sum{m in LOCATION, n in LOCATION: AVAILABILITY[0,n]>0} DISPLACEMENT[n,m] >= sum{n in LOCATION: AVAILABILITY[1,n]>0}AVAILABILITY[1,m];
    
# Scooters arriving to a demanding location must be at least the sum of its demand plus 
# scooters  leaving that location
s.t. demands {m in LOCATION: AVAILABILITY[0,m]>0}: 
    sum{n in LOCATION} DISPLACEMENT[n,m] >= AVAILABILITY[1,m] + sum{n in LOCATION}DISPLACEMENT[m,n];
    
# Sum of scooters leaving a location with no demand must be less or equal to 
# scooters arriving plus available scooters 
s.t. leaving {m in LOCATION: AVAILABILITY[0,m]>0}: 
    sum{n in LOCATION} DISPLACEMENT[m,n] <= AVAILABILITY[0,m] + DISPLACEMENT[n,m];
end;
