#%% librerías
from pyomo.environ import *

#%% modelo

# definicion
M = ConcreteModel()

# variable
M.xa = Var(within=NonNegativeReals) # xa >=0
M.xb = Var(within=NonNegativeReals) # xb >=0

# funcion objetivo
M.of = Objective(expr=400*M.xa+700*M.xb) #minimizar el coste

# restricciones
M.vita = Constraint(expr=3*M.xa+8*M.xb>=240) #requerimiento de vitaminas
M.mine = Constraint(expr=6*M.xa+3*M.xb>=120) #requerimiento de minerales
M.prot = Constraint(expr=4*M.xa+5*M.xb>=200) #requerimiento de proteinas


#%% definir el solver a usar

Solver = SolverFactory('cbc',executable='C:\\cbc-win64\\cbc')


# %% resolver el modelo

ModelResults = Solver.solve(M,tee=True)


# %% ver los resultados

ModelResults.write() #información del solver
M.pprint() # solución del modelo

# %% 


M.xa.display()
M.xb.display()
