#%% simple example in pyomo
from pyomo.environ import *

#%% case 1

# model definition
m = ConcreteModel()

# variable definition
m.x1 = Var(within=NonNegativeReals)
m.x2 = Var(within=NonNegativeReals)

# objective function
m.obj = Objective(expr= m.x1 - 2*m.x2)

# constraints
m.con1 = Constraint(expr=-1*m.x1 + 1*m.x2 <= 2)
m.con2 = Constraint(expr=-1*m.x1 + 2*m.x2 <= 6)

# duals, slack, and reduced cost
m.dual  = Suffix(direction=Suffix.IMPORT)
m.rc    = Suffix(direction=Suffix.IMPORT)
m.slack = Suffix(direction=Suffix.IMPORT)

# solver definition

SolverName     = 'cbc' 
SolverPath_exe = 'C:\\cbc-win64\\cbc'
Solver = SolverFactory(SolverName,executable=SolverPath_exe)

#SolverName     = 'gurobi'
#Solver = SolverFactory(SolverName)

# solving the model

# solve
SolverResultsCase1 = Solver.solve(m, tee=True)

# print solution

SolverResultsCase1.write()
m.pprint()

# print individual values
m.x1.display()
m.x2.display()
m.obj.display()
m.dual.display()  
m.rc.display()    
m.slack.display()


# %% case 2

m.obj = Objective(expr= m.x1 - 3*m.x2)

SolverResultsCase2 = Solver.solve(m, tee=True)

# print solution

SolverResultsCase2.write()
m.pprint()

# print individual values
m.x1.display()
m.x2.display()
m.obj.display()
m.dual.display()  
m.rc.display()    
m.slack.display()

# %% case 3

m.obj = Objective(expr= -m.x1 - m.x2)

SolverResultsCase3 = Solver.solve(m, tee=True)

# print solution

SolverResultsCase3.write()
m.pprint()

# print individual values
m.x1.display()
m.x2.display()
m.obj.display()
m.dual.display()  
m.rc.display()    
m.slack.display()
# %%
