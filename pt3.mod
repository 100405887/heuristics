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
var CHARGES{f in FREELANCER, s in SCOOTER} binary; 

###### Objective function ######
#minimize GOAL: {s in SCOOTER, l in LOCATION} sum{f in FREELANCER, a in FREELANCER}(COST[f,l]*PLACEMENT[l,s]*CHARGES[s,a]);
#minimize GOAL:sum{f in FREELANCER, a in FREELANCER}((COST*PLACEMENT*CHARGES)[f,a]);
#minimize GOAL: sum{f in FREELANCER, s in SCOOTER} (COST[f,l]*PLACEMENT[l,s])*CHARGES[f,s];
#minimize GOAL: sum{f in FREELANCER, a in FREELANCER} COST[f,l]*(PLACEMENT[l,s]*CHARGES[s,a]);
minimize GOAL{l in LOCATION}: sum{f in FREELANCER, s in SCOOTER} (COST[f,l]*PLACEMENT[l,s])*CHARGES[f,s];
###### Constraints ###### 

# No freelancer can charge more than 3 scooters
s.t. FREEMAX {f in FREELANCER}: 
    sum{s in SCOOTER} CHARGES[f,s] <= 3;

# Each scooter must be recharged by a single freelancer    
s.t. ONEFREELANCER{s in SCOOTER}:
    sum{f in FREELANCER} CHARGES[f,s]=1;

# Banned locations per freelancer
s.t. BANNEDfF in FREELANCER, l in LOCATION}:
    sum{s in SCOOTER} (ALLOWED[f,l]*PLACEMENT[l,s])*CHARGES[f,s] = sum{s in SCOOTER} CHARGES[f,s];

# 50% max 
s.t. fiftymax{f in FREELANCER, a in FREELANCER}:
    sum{s in SCOOTER} CHARGES[f,s]<=1.5*sum{s in SCOOTER} CHARGES[a,s];
end;
