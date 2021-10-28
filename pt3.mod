set LOCATION; 
set FREELANCER;

# Cost of A FREELANCER charging a scooter according to location
param COST{m in LOCATION, n in FREELANCER};

#Amount of scooters to be charged per location
param SCOOTPERLOC{L in LOCATION, F in FREELANCER};

# Decision variables named CHARGES 
var CHARGES{m in LOCATION, n in FREELANCER} integer, >= 0; 

###### Objective function ######
minimize GOAL: sum{m in LOCATION, n in FREELANCER} CHARGES[m,n]*COST[m,n];

###### Constraints ###### 
# The amount of charged scooters at a location must be equal to the amount of scooters that need charging
s.t. LOCS {m in LOCATION: SCOOTPERLOC[m]>0}: 
    sum{n in FREELANCER} CHARGES[m,n] = SCOOTPERLOC[m];
    
# No freelancer can charge more than 3 scooters
s.t. FREEMAX {n in FREELANCER}: 
    sum{m in LOCATION} CHARGES[m,n] <= 3;
    
