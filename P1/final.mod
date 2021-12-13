set LOCATION; 
set FREELANCER;
set SCOOTER;
set DISPONIBILITY;

# Cost of moving a scooter from LOCATION m to LOCATION n
param MOVINGC{m in LOCATION, n in LOCATION};

# AVAILABILITY stores number of scooters available or demanded per LOCATION
param AVAILABILITY{b in LOCATION};

# Cost of A FREELANCER charging a scooter according to location
param CHARGINGC{f in FREELANCER, l in LOCATION};


param PLACEMENT{l in LOCATION, s in SCOOTER};

#Freelancers not allowed to recharged at certain locations
param ALLOWED{f in FREELANCER, l in LOCATION};

# Maximum of scooters charges per Freelancer
param MAX_CHARGES;

# Decision variables named DISPLACEMENT 
# counting number of displacements from LOCATION m to LOCATION n
var DISPLACEMENT{m in LOCATION, n in LOCATION} integer, >= 0; 

# Decision variables named CHARGES 
var CHARGES{f in FREELANCER, s in SCOOTER} binary; 

###### Objective function ######
minimize GOAL: sum{l in LOCATION}(sum{f in FREELANCER, s in SCOOTER}(CHARGINGC[f,l]*PLACEMENT[l,s])*CHARGES[f,s])+ sum{m in LOCATION, n in LOCATION}(DISPLACEMENT[m,n]*MOVINGC[m,n]);

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

# Every available location must share at least 90% of their scooters available
s.t. share90 {m in LOCATION: AVAILABILITY[m]>0}: 
    sum{n in LOCATION} DISPLACEMENT[m,n] >= 0.9*AVAILABILITY[m];
    
# Scooters leaving an available location must be at least equal to total demand 
s.t. arriving: 
    sum{m in LOCATION,n in LOCATION:AVAILABILITY[m]>0} DISPLACEMENT[m,n] >= -sum{n in LOCATION: AVAILABILITY[n]<0}AVAILABILITY[n];
    
# Scooters arriving to a demanding location must be at least the sum of its demand plus 
# scooters  leaving that location
s.t. demands {m in LOCATION: AVAILABILITY[m]<0}: 
    sum{n in LOCATION} (DISPLACEMENT[n,m]-DISPLACEMENT[m,n]) >= -AVAILABILITY[m];
    
# Sum of scooters leaving a location with no demand must be less or equal to 
# scooters arriving plus available scooters 
s.t. leaving {m in LOCATION: AVAILABILITY[m]>0}: 
    sum{n in LOCATION} DISPLACEMENT[m,n] <= AVAILABILITY[m] + sum{n in LOCATION}DISPLACEMENT[n,m];

end;