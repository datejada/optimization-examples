#%% generic example in pyomo
from pyomo.environ import ConcreteModel, Set, Param, Var, Binary, Constraint, Objective, minimize, Suffix, value
from pyomo.opt import SolverFactory
import string

#%% read input data

# inputs for sets
N = 10 # board size

rows = list(string.ascii_uppercase[0:N])
cols = [c+1 for c in range(N)]

# inputs for parameters
PeopleLocation = {
    ('A', 2): 1,
    ('A', 7): 1,
    ('B', 9): 1,
    ('D', 5): 1,
    ('E', 4): 1,
    ('E', 8): 1,
    ('G', 3): 1,
    ('H', 4): 1,
    ('J', 3): 1,
    ('J', 8): 1,
    }

PeopleToBuilding = {
    ('A', 2,'B',  5): 1,
    ('A', 7,'D',  9): 1,
    ('B', 9,'F',  6): 1,
    ('D', 5,'C',  2): 1,
    ('E', 4,'I',  7): 1,
    ('E', 8,'D',  2): 1,
    ('G', 3,'G',  7): 1,
    ('H', 4,'J',  1): 1,
    ('J', 3,'G', 10): 1,
    ('J', 8,'H',  9): 1,
    }

Distance = {(i,j,ii,jj):((rr-r)**2+(cc-c)**2)**(1/2)
                for r,i   in enumerate(rows)
                for c,j   in enumerate(cols)
                for rr,ii in enumerate(rows)
                for cc,jj in enumerate(cols)}

# max stages in the trip 
S = 2*len(PeopleLocation) #we want go back to the starting point 
# list of stages
stag = [s+1 for s in range(S)]

#%% definitions

# model
mSDC = ConcreteModel(name='Self-driving cars')

# sets
mSDC.i  = Set(initialize=rows  , doc='rows'              )
mSDC.ii = Set(initialize=mSDC.i, doc='alias for rows'    )
mSDC.iii= Set(initialize=mSDC.i, doc='alias for rows'    )
mSDC.j  = Set(initialize=cols  , doc='columns'           )
mSDC.jj = Set(initialize=mSDC.j, doc='alias for columns' )
mSDC.jjj= Set(initialize=mSDC.j, doc='alias for columns' )
mSDC.k  = Set(initialize=stag  , doc='stages in the trip')

# parameters
mSDC.pPeopleLoc  = Param(mSDC.i , mSDC.j ,                   initialize=PeopleLocation  , doc='people   location in the board',default=0) #default=0 because not all the combinations are in the parameter initialization
mSDC.pPeopToBuild= Param(mSDC.i , mSDC.j , mSDC.ii, mSDC.jj, initialize=PeopleToBuilding, doc='People to destination Building',default=0) #default=0 because not all the combinations are in the parameter initialization
mSDC.pDistance   = Param(mSDC.i , mSDC.j , mSDC.ii, mSDC.jj, initialize=Distance        , doc='People to destination Building',default=0) #default=0 because not all the combinations are in the parameter initialization


# variables
mSDC.vX = Var(mSDC.i, mSDC.j, mSDC.ii, mSDC.jj, mSDC.k, within=Binary, doc='wheter the path from i to j is included in the route at stage k')

# constraints
def ePeopToBuild_rule(mSDC,i,j):
    if(mSDC.pPeopleLoc[i,j]==1):
        return sum(mSDC.vX[i,j,ii,jj,k]
                    for ii in mSDC.ii
                    for jj in mSDC.jj
                    for k  in mSDC.k 
                    if mSDC.pPeopToBuild[i,j,ii,jj]==1)==1
    else:
        return Constraint.Skip
mSDC.ePeopToBuild = Constraint(mSDC.i,mSDC.j, rule=ePeopToBuild_rule, doc='Assigning a person an only building')

def eOrder_rule(mSDC,k):
    return sum(mSDC.vX[ii,jj,i,j,k]
                for i  in mSDC.i
                for j  in mSDC.j
                for ii in mSDC.ii
                for jj in mSDC.jj)==1
mSDC.eOrder = Constraint(mSDC.k, rule=eOrder_rule, doc='Assigning one order between the destinations')

def eSequence_rule(mSDC,ii,jj,k):
    if(k != S):
        return sum(mSDC.vX[i,j,ii,jj,k]
                    for i in mSDC.i
                    for j in mSDC.j)==sum(mSDC.vX[ii,jj,iii,jjj,k+1]
                                            for iii in mSDC.iii
                                            for jjj in mSDC.jjj)
    else:
        return sum(mSDC.vX[i,j,ii,jj,k]
                    for i in mSDC.i
                    for j in mSDC.j)==sum(mSDC.vX[ii,jj,iii,jjj,1]
                                            for iii in mSDC.iii
                                            for jjj in mSDC.jjj)
mSDC.eSequence = Constraint(mSDC.ii,mSDC.jj,mSDC.k, rule=eSequence_rule, doc='Sequence for the travel (only one route) -> avoiding sub-routes')

# objective function
def eObj_rule(mSDC):
    return sum(mSDC.pDistance[i,j,ii,jj]*mSDC.vX[i,j,ii,jj,k]
                for i  in mSDC.i
                for j  in mSDC.j
                for ii in mSDC.ii
                for jj in mSDC.jj
                for k  in mSDC.k)
mSDC.ObjFun = Objective(rule=eObj_rule, sense=minimize)


#%% solver definition

# CBC
#SolverName     = 'cbc'
#SolverPath_exe = 'C:\\cbc-win64\\cbc' 
#Solver = SolverFactory(SolverName,executable=SolverPath_exe)
#Solver.options['allowableGap'] = 0 

# XPRESS
#SolverName     = 'xpress'
#SolverPath_exe = 'C:\\xpressmp\\bin\\amplxpress'
#Solver = SolverFactory(SolverName,executable=SolverPath_exe)

# GUROBI (pip install gurobipy)
SolverName     = 'gurobi'
Solver = SolverFactory(SolverName)

#%% solving the model

# write the optimization problem
mSDC.write('self-driving-cars-closed-loop.lp', io_options={'symbolic_solver_labels': True})

# solve
SolverResults = Solver.solve(mSDC, tee=True)

#mSDC.pprint() # print solution
#mSDC.vX.pprint() # print all the variables

#%% print results

# total distance
print('Total distance: ' + str(value(mSDC.ObjFun)))

# the tour
tour = {(i,j,ii,jj):k 
            for k  in mSDC.k
            for i  in mSDC.i
            for j  in mSDC.j
            for ii in mSDC.ii
            for jj in mSDC.jj
            if mSDC.vX[i,j,ii,jj,k].value==1}
tour

# %%
