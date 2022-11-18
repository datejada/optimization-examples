#%% generic example in pyomo
from pyomo.environ import ConcreteModel, Set, Param, Var, Binary, Constraint, Objective, minimize, Suffix, value
from pyomo.opt import SolverFactory

import pandas as pd

#%% read input data

# read and transform input data
df_comb = (pd.read_csv('./inputs/combinations.csv',
                    index_col=[0])
        .fillna(0)
        .stack()
     )
df_comb.index.names = ['points','lines']

df_cost = (pd.read_csv('./inputs/costs.csv',
                    index_col=[0])
     )


# create lists and dicts
I = list(df_comb.index.get_level_values('points').unique().map(str))
J = list(df_comb.index.get_level_values('lines' ).unique().map(str))

Comb_ij= dict(zip(df_comb.index,df_comb))
Cost_j = dict(zip(df_cost.index,df_cost['Cost']))

#%% definitions

# model
mMP = ConcreteModel(name='Metro Planning')

# sets
mMP.i  = Set(initialize=I, doc='key points')
mMP.j  = Set(initialize=J, doc='lines'     )

# parameters
mMP.pCombination = Param(mMP.i, mMP.j, initialize=Comb_ij, doc='combination among points and lines',default=0)
mMP.pLineCost    = Param(       mMP.j, initialize=Cost_j , doc='line construction cost'                      )

# variables
mMP.vX = Var(mMP.j, within=Binary, doc='wheter the line j is built or not')

# constraints
def eConnections_rule(mMP,i):
    if(i!='P2'):
        return sum(mMP.vX[j]
                    for j in mMP.j
                    if mMP.pCombination[i,j]==1)>=1
    else:
        return sum(mMP.vX[j]
                    for j in mMP.j
                    if mMP.pCombination[i,j]==1)>=2

mMP.eConnections = Constraint(mMP.i, rule=eConnections_rule, doc='minimum number of connections')

def eLogic_rule(mMP):
    return mMP.vX['L5']+mMP.vX['L7']>=2*(1-mMP.vX['L2'])
mMP.eLogic = Constraint(rule=eLogic_rule, doc='logic between L2, L5, and L7')

# objective function
def eObj_rule(mMP):
    return sum(mMP.pLineCost[j]*mMP.vX[j]
                for j  in mMP.j)
mMP.ObjFun = Objective(rule=eObj_rule, sense=minimize)


#%% solver definition

# CBC
SolverName     = 'cbc'
SolverPath_exe = 'C:\\cbc-win64\\cbc' 
Solver = SolverFactory(SolverName,executable=SolverPath_exe)
Solver.options['allowableGap'] = 0 

# XPRESS
#SolverName     = 'xpress'
#SolverPath_exe = 'C:\\xpressmp\\bin\\amplxpress'
#Solver = SolverFactory(SolverName,executable=SolverPath_exe)

# GUROBI (pip install gurobipy)
#SolverName     = 'gurobi'
#Solver = SolverFactory(SolverName)

#%% solving the model

# write the optimization problem
mMP.write('metro-planning.lp', io_options={'symbolic_solver_labels': True})

# solve
SolverResults = Solver.solve(mMP, tee=True)

#mMP.pprint() # print solution
#mMP.vX.pprint() # print all the variables

#%% print results

# objective function
print('Total cost: ' + str(value(mMP.ObjFun)))

# the lines
lines = {(j):1 for j  in mMP.j if mMP.vX[j].value==1}
lines

# %%
