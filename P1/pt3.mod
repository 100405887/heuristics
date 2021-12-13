set LOCATION; 
set FREELANCER;
set SCOOTER;
# Maximum of scooters charges per Freelancer
param MAX_CHARGES;
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
minimize GOAL: sum{l in LOCATION} sum{f in FREELANCER, s in SCOOTER} (COST[f,l]*PLACEMENT[l,s])*CHARGES[f,s];
###### Constraints ###### 

# No freelancer can charge more than 3 scooters
s.t. MAX_PER_FREELANCER {f in FREELANCER}: 
    sum{s in SCOOTER} CHARGES[f,s] <= MAX_CHARGES;

# Each scooter must be recharged by a single freelancer    
s.t. ONEFREELANCER{s in SCOOTER}:
    sum{f in FREELANCER} CHARGES[f,s]=1;

# Banned locations per freelancer
s.t. BANNED{l in LOCATION, f in FREELANCER: ALLOWED[f,l]=0}:
    sum{s in SCOOTER} PLACEMENT[l,s]*CHARGES[f,s] = 0;

# Maximum of 50% more charges than rest of freelancers
s.t. COMPENSATE{f in FREELANCER, a in FREELANCER}:
    sum{s in SCOOTER} CHARGES[f,s]<=1.5*sum{s in SCOOTER} CHARGES[a,s];

end;