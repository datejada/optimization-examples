#%% generic example in pyomo
from pyomo.environ import ConcreteModel, Set, Param, Var, Binary, Constraint, Objective, maximize, Suffix
from pyomo.opt import SolverFactory

import matplotlib.pyplot as plt

#%% read input data

N = 8 # board size

I = [i+1 for i in range(N)]

#%% definitions

# model
mNQ = ConcreteModel(name='N Queens')

# sets
mNQ.i = Set(initialize=I, doc='rows')
mNQ.j = Set(initialize=mNQ.i, doc='columns')

# variables
mNQ.vX = Var(mNQ.i, mNQ.j, within=Binary, doc='1 if we select a quenn in position i,j')

# constraints
def eRow_rule(mNQ,i):
    return sum(mNQ.vX[i,j] for j in mNQ.j)<=1
mNQ.eRow = Constraint(mNQ.i, rule=eRow_rule, doc='one queen per row')

def eCol_rule(mNQ,j):
    return sum(mNQ.vX[i,j] for i in mNQ.i)<=1
mNQ.eCol = Constraint(mNQ.j, rule=eCol_rule, doc='one queen per column')

def eDiag_rule1(mNQ,i,j):
    totalQueen=0
    for r in mNQ.i:
        for c in mNQ.j:
            if j-c==i-r:
                totalQueen+=mNQ.vX[c,r] 
    return totalQueen<=1
mNQ.eDiag1 = Constraint(mNQ.i,mNQ.j, rule=eDiag_rule1, doc='one queen per diagonal')

def eDiag_rule2(mNQ,i,j):
    totalQueen=0
    for r in mNQ.i:
        for c in mNQ.j:
            if j-c==-(i-r):
                totalQueen+=mNQ.vX[c,r] 
    return totalQueen<=1
mNQ.eDiag2 = Constraint(mNQ.i,mNQ.j, rule=eDiag_rule2, doc='one queen per anti-diagonal')

# objective function
def eObj_rule(mNQ):
    return sum(mNQ.vX[i,j] for i in mNQ.i for j in mNQ.j)    
mNQ.ObjFun = Objective(rule=eObj_rule, sense=maximize)

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
mNQ.write('n-queens.lp', io_options={'symbolic_solver_labels': True})

# solve
SolverResults = Solver.solve(mNQ, tee=True)

#%% print solution

mNQ.pprint()


#%% print only the variable

mNQ.vX.pprint()


#%% plot
for i in mNQ.i:
    for j in mNQ.j:
        X=mNQ.vX[i,j].value
        if X==1:
            plt.scatter(i,j,s=80,color='salmon')
        else:
            plt.scatter(i,j,s=10,color='grey')
plt.axis('off')
plt.savefig('n-queens.png', format='png', dpi=1200)
plt.show()

# %%
