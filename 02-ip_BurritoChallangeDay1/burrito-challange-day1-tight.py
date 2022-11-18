#%% generic example in pyomo

from pyomo.environ import ConcreteModel, Set, Param, Var, Binary, Constraint, Objective, maximize, Suffix
from pyomo.opt import SolverFactory

import pandas as pd

import matplotlib.pyplot as plt

#%% read input data
input_data_folder = 'round1-day1'

df_demand_data       = pd.read_csv('.\\'+input_data_folder+'\\demand_node_data.csv' , index_col=0)
df_truck_data        = pd.read_csv('.\\'+input_data_folder+'\\truck_node_data.csv'  , index_col=0)
df_demand_truck_data = pd.read_csv('.\\'+input_data_folder+'\\demand_truck_data.csv', index_col=[0,1])
df_problem_data      = pd.read_csv('.\\'+input_data_folder+'\\problem_data.csv')

I = list(df_demand_data.index.map(str))
J = list(df_truck_data.index.map(str))

Di = dict(zip(df_demand_data.index,df_demand_data['demand']))
Aij= dict(zip(df_demand_truck_data.index,df_demand_truck_data['scaled_demand']))
print(Aij)
F =  df_problem_data.loc[0,'truck_cost']
R =  df_problem_data.loc[0,'burrito_price']
K =  df_problem_data.loc[0,'ingredient_cost']

#%% definitions

# model
mBurrito = ConcreteModel(name='Burrito Challange')

# sets
mBurrito.i = Set(initialize=I, doc='customers')
mBurrito.j = Set(initialize=J, doc='trucks')

# parameters
mBurrito.pD = Param(mBurrito.i, initialize=Di, doc='customers demand')
mBurrito.pA = Param(mBurrito.i,mBurrito.j, initialize=Aij, doc='demand multiplier for customer i and truck j')

mBurrito.pF = Param(initialize=F,doc='truck fixed cost')
mBurrito.pR = Param(initialize=R,doc='revenue per burrito sold')
mBurrito.pK = Param(initialize=K,doc='cost per burrito sold')

# variables
mBurrito.vX = Var(           mBurrito.j, within=Binary, doc='1 if we assing demand i to truck at j')
mBurrito.vY = Var(mBurrito.i,mBurrito.j, within=Binary, doc='1 if we locate a truck at j')

# constraints
def eAssignation1(mBurrito,i):
    return sum(mBurrito.vY[i,j] for j in mBurrito.j if mBurrito.pA[i,j]>0) <= 1
mBurrito.eAssignation1 = Constraint(mBurrito.i,rule=eAssignation1,doc='each customer may be assigned to at most one truck')

def eAssignation2(mBurrito,i,j):
    if(mBurrito.pA[i,j]>0):
        return mBurrito.vY[i,j] <= mBurrito.vX[j]
    else:
        return Constraint.Skip
mBurrito.eAssignation2 = Constraint(mBurrito.i,mBurrito.j,rule=eAssignation2,doc='a customer can only be served by a truck')

# objective function
def eProfit(mBurrito):
    return (+ sum((mBurrito.pR-mBurrito.pK)*mBurrito.pA[i,j]*mBurrito.vY[i,j] for i in mBurrito.i for j in mBurrito.j)
            - sum( mBurrito.pF*mBurrito.vX[j] for j in mBurrito.j))

mBurrito.ObjFun = Objective(rule=eProfit, sense=maximize, doc='total profit')

#%% solver definition

# CBC
SolverName     = 'cbc'
SolverPath_exe = 'C:\\cbc-win64\\cbc' 
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
mBurrito.write('burrito-tight.lp', io_options={'symbolic_solver_labels': True})

# solve
SolverResults = Solver.solve(mBurrito, tee=True)

#%% print solution

mBurrito.pprint()


#%% print only the variable

mBurrito.vX.pprint()
mBurrito.vY.pprint()


# %% plot

trucks = [mBurrito.vX[j].value for j in J]

fig = plt.figure(figsize=(7,7))

plt.scatter(x=df_truck_data ['x'],y=df_truck_data ['y'],c=trucks,marker='s',cmap='Pastel2_r')
plt.scatter(x=df_demand_data['x'],y=df_demand_data['y'],marker='o',s=10*df_demand_data['demand'],color='cornflowerblue')

edges = ((i,j) for i in mBurrito.i for j in mBurrito.j if mBurrito.vY[i,j].value==1.0)

for i,j in edges:
    plt.plot([df_truck_data.loc[j,'x'],df_demand_data.loc[i,'x']],[df_truck_data.loc[j,'y'],df_demand_data.loc[i,'y']],color='indianred',linestyle='dashed')

plt.axis('off')
plt.savefig('burrito-challange-day1-tight.png',dpi=500)
plt.show

# %%
