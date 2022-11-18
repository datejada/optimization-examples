#%% generic example in pyomo
from pyomo.environ import ConcreteModel, Set, Param, Var, Binary, Constraint, Objective, minimize, Suffix
from pyomo.opt import SolverFactory

import pandas as pd

import matplotlib.pyplot as plt

#%% read input data
input_data_folder = 'input-data'

df_seq_cost        = pd.read_csv('.\\'+input_data_folder+'\\sequence-cost.csv', index_col=[0])
df_flight_seq_data = pd.read_csv('.\\'+input_data_folder+'\\feasible-flight-sequences.csv', index_col=[0,1])

#%%

I = list(df_flight_seq_data.reset_index()['Flight'].unique())
J = list(df_flight_seq_data.reset_index()['Sequence'].unique())

Cj = dict(zip(df_seq_cost.index,df_seq_cost['Cost']))
Sij= dict(zip(df_flight_seq_data.index,df_flight_seq_data['Value']))

CrewReq = 3 # crew requierement

#%% definitions

# model
mCrew = ConcreteModel(name='Crew Assignment')

# sets
mCrew.i = Set(initialize=I, doc='flights')
mCrew.j = Set(initialize=J, doc='sequence')

# parameters
mCrew.pC = Param(mCrew.j,         initialize=Cj , doc='customers demand')
mCrew.pS = Param(mCrew.i,mCrew.j, initialize=Sij, doc='order of i in sequence j',default=0) #default=0 because not all the combinations are in Sij, so the ones not there are zero

mCrew.pR = Param(initialize=CrewReq,doc='crew requierement')

# variables
mCrew.vX = Var(mCrew.j, within=Binary, doc='1 if we select sequence j')

# constraints
def eAssignation(mCrew,i):
    return sum(mCrew.vX[j] for j in mCrew.j if mCrew.pS[i,j]>0) >= 1
mCrew.eAssignation = Constraint(mCrew.i,rule=eAssignation,doc='each flight i has to be selected at least once')

def eMinCrew(mCrew):
    return sum(mCrew.vX[j] for j in mCrew.j) == mCrew.pR
mCrew.eMinCrew = Constraint(rule=eMinCrew,doc='min flights')

# objective function
def eCost(mCrew):
    return sum (mCrew.pC[j]*mCrew.vX[j] for j in mCrew.j)
mCrew.ObjFun = Objective(rule=eCost, sense=minimize, doc='total profit')

#%% solver definition

# CBC
SolverName     = 'cbc'
SolverPath_exe = 'C:\\Users\\David\\Desktop\\U-TAD\\4to AÑO\\1er cuatrimestre\\Optimizacion de software\\cbc\\cbc' 
Solver = SolverFactory(SolverName,executable=SolverPath_exe)
#Solver.options['allowableGap'] = 0 

# XPRESS
#SolverName     = 'xpress'
#SolverPath_exe = 'C:\\xpressmp\\bin\\amplxpress'
#Solver = SolverFactory(SolverName,executable=SolverPath_exe)

# GUROBI (pip install gurobipy)
#SolverName     = 'gurobi'
#Solver = SolverFactory(SolverName)

#%% solving the model

# write the optimization problem
mCrew.write('crew.lp', io_options={'symbolic_solver_labels': True})

# solve
SolverResults = Solver.solve(mCrew, tee=True)

#%% print solution

mCrew.pprint()


#%% print only the variable

mCrew.vX.pprint()


# %%
