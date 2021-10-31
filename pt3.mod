set LOCATION; 
set FREELANCER;
set SCOOTER;

# Cost of A FREELANCER charging a scooter according to location
param COST{f in FREELANCER, l in LOCATION};

#Amount of scooters to be charged per location
#param SCOOTPERLOC{l in LOCATION, f in FREELANCER};

param PLACEMENT{l in LOCATION, s in SCOOTER};

#Freelancers not allowed to recharged at certain locations
param ALLOWED{f in FREELANCER, l in LOCATION};

# Decision variables named CHARGES 
var CHARGES{s in SCOOTER, f in FREELANCER} integer, >= 0; 

###### Objective function ######
minimize GOAL: sum{l in LOCATION, f in FREELANCER, s in SCOOTER} COST[f,l]*PLACEMENT[l,s]*CHARGES[s,f];

###### Constraints ###### 

# No freelancer can charge more than 3 scooters
s.t. FREEMAX {f in FREELANCER}: 
    sum{s in SCOOTER} CHARGES[s,f] <= 3;

# Each scooter must be recharged by a single freelancer    
s.t. ONEFREELANCER{s in SCOOTER}:
    sum{f in FREELANCER} CHARGES[s,f]=1;

# Banned locations per freelancer
s.t. BANNED{f in FREELANCER,s in SCOOTER, l in LOCATION}:
    CHARGES[s,f] = ALLOWED[f,l]*PLACEMENT[l,s]*CHARGES[s,f];

# 50% max 
s.t. fiftymax{f in FREELANCER, a in FREELANCER}:
    sum{s in SCOOTER} CHARGES[s,f]<=1.5*sum{s in SCOOTER} CHARGES[s,a];
end;