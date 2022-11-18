#%% simple example in pyomo
import numpy as np
import time # count clock time
from pyomo.environ import ConcreteModel, Set, Param, Var, NonNegativeReals, Binary, Integers, Constraint, Objective, minimize, Suffix, value
from pyomo.opt import SolverFactory

#%% parameters

# input values
NumOrders =  10 # total number of orders
NumRolls  = 130 # available number of paper rolls (assumption). If we use 150 CBC can't solve it :( but, Gurobi does :)
MaxCuts   =   4 # maximum number of cuts in one roll
RollLeng  =   3 # length per roll

# lists
orders = ['t'+str(i+1) for i in range(NumOrders)]
rolls  = ['r'+str(j+1) for j in range(NumRolls) ]

rolls_per_order  = [  20,  30,  15,  25,  40,  25,  50,  15,  10,   5]
lengt_per_order  = [0.50,0.75,1.00,1.25,1.50,1.75,2.00,2.25,2.50,2.75]

min_rolls = round(sum(np.array(rolls_per_order)*np.array(lengt_per_order))/3,2)
max_orders_per_roll = np.floor(np.array([RollLeng for i in range(NumOrders)])/lengt_per_order)

print("We need at least {} rolls (disregarding the waste). \
So, the total number of rolls (NumRolls) to consider must be \
greater than this number.".format(min_rolls))

#%% model

# model definition
m = ConcreteModel('Paper roll cut')

# sets
m.i = Set(initialize=orders,doc='type of order')
m.j = Set(initialize=rolls ,doc='set of rolls' )

# parameters
m.pRollsPerOrder = Param(m.i, initialize=dict(zip(orders,rolls_per_order)), doc='rolls per type of order')
m.pLengtPerOrder = Param(m.i, initialize=dict(zip(orders,lengt_per_order)), doc='length per type of order')
m.pMaxOrdersRoll = Param(m.i, initialize=dict(zip(orders,max_orders_per_roll)))

# variable definition
m.vX = Var(m.i,m.j, within=Integers        , bounds=lambda m,i,j: (0,m.pMaxOrdersRoll[i]),doc='rolls of type i in roll j')
m.vW = Var(    m.j, within=NonNegativeReals, bounds=(0,RollLeng)                         ,doc='waste in roll j')
m.vD = Var(    m.j, within=Binary          , bounds=(0,1)                                ,doc='aux binary var to determine if an order t1 is used (1) or not (0) in the roll j')
#m.vY = Var(    m.j, within=Binary          , bounds=(0,1)                                ,doc='binary var to determine if the roll j is used (1) or not (0)') # with no warmstart
m.vY = Var(    m.j, within=Binary          , bounds=(0,1)                                ,doc='binary var to determine if the roll j is used (1) or not (0)',initialize=dict(zip(rolls,np.ones(NumRolls)))) #with warmstart

#%% Objective Function and Constraints

# objective function (option 1 - Minimize waste)
def eMinWaste(m):
    return sum(m.vW[j] for j in m.j)
m.eMinWaste = Objective(rule=eMinWaste, sense=minimize, doc='minimize the total waste')

# objective function (option 2 - Minimize used rolls)
def eMinNumMR(m):
    return sum(m.vY[j] for j in m.j)
m.eMinNumMR = Objective(rule=eMinNumMR, sense=minimize, doc='minimize the total used rolls')

# constraints
def eNumPedi(m,i):
    return sum(m.vX[i,j] for j in m.j) == m.pRollsPerOrder[i]
m.eNumPedi = Constraint(m.i, rule=eNumPedi, doc='rolls demand per order type')

def eLimCort(m,j):
    return sum(m.vX[i,j] for i in m.i) <= (MaxCuts+1)*m.vY[j]
m.eLimCort = Constraint(m.j, rule=eLimCort, doc='maximum number of cuts in a roll')

def eLimLong(m,j):
    return sum(m.pLengtPerOrder[i]*m.vX[i,j] for i in m.i) + m.vW[j] == RollLeng*m.vY[j]
m.eLimLong = Constraint(m.j, rule=eLimLong, doc='lenght limit in a roll')

# option 1 to model the logic constraint using the aux binary variable
# these constraints consider epsilon=1, m=-1 (lower bound) y M=4 (upper bound)
def eLogicOpt1a(m,j):
    return m.vX['t1',j]               <= (MaxCuts+1)*m.vD[j]
m.eLogicOpt1a = Constraint(m.j, rule=eLogicOpt1a, doc='if order of type 1 is carried out, include an order of either type 5 or type 9 (option 1)')

def eLogicOpt1b(m,j):
    return m.vX['t5',j] +m.vX['t9',j] >=             m.vD[j]
m.eLogicOpt1b = Constraint(m.j, rule=eLogicOpt1b, doc='if order of type 1 is carried out, include an order of either type 5 or type 9 (option 1)')

# option 2 to model the logic constraint (we can obtain eLogicOpt2 from eLogicOpt1a and eLogicOpt1b)
def eLogicOpt2(m,j):
    return (MaxCuts+1)*(m.vX['t5',j] +m.vX['t9',j]) >= m.vX['t1',j]
m.eLogicOpt2 = Constraint(m.j, rule=eLogicOpt2, doc='if order of type 1 is carried out, include an order of either type 5 or type 9 (option 2)')


#%% Solution Case 1 - Objective function min waste and no logic included

# we activate objective function 1 and deactivate objective function 2
m.eMinWaste.activate()
m.eMinNumMR.deactivate()

# we deactivate logic constraints
m.eLogicOpt1a.deactivate()
m.eLogicOpt1b.deactivate()
m.eLogicOpt2.deactivate()

# we fix the aux binary variable to zero
m.vD.fix(0)

# lp file
m.write('PaperRollCut-minimize-waste-no-logic.lp', io_options={'symbolic_solver_labels': True})

# count solve time
StartTime = time.time()

SolverName     = 'cbc' 
SolverPath_exe = 'C:\\cbc-win64\\cbc'
Solver = SolverFactory(SolverName,executable=SolverPath_exe)
#https://www.gams.com/latest/docs/S_CBC.html#CBC_OPTIONS_LIST
Solver.options['allowableGap'   ] = 0.05
#Solver.options['nodeStrategy'   ] ='hybrid'
#Solver.options['strategy'       ] = 2 #aggressive
#Solver.options['randomCbcSeed'  ] = 19821020
#Solver.options['Rins'           ] = 'often'
#Solver.options['greedyHeuristic'] = 'both'

#SolverName     = 'gurobi'
#Solver = SolverFactory(SolverName)
#Solver.options['MIPGap'] = 0.05

# solving the model
# solve
SolverResultsCase1 = Solver.solve(m, tee=True, warmstart=True)
#SolverResultsCase1 = Solver.solve(m, tee=True)

SolvingTime = time.time() - StartTime
print('Total solving time... ', round(SolvingTime), 's')

#%% print solution
SolverResultsCase1.write()
m.pprint()

# print individual values
print("Objective function - option minimize waste: {}".format(value(m.eMinWaste)))
print("total waste - option minimize waste: {}".format(sum([m.vW[j].value for j in m.j])))
print("total rolls - option minimize waste: {}".format(sum([m.vY[j].value for j in m.j])))

#%% Solution Case 2 - Objective function min rolls and no logic included

# we activate objective function 1 and deactivate objective function 2
m.eMinWaste.deactivate()
m.eMinNumMR.activate()

# lp file
m.write('PaperRollCut-minimize-rolls-no-logic.lp', io_options={'symbolic_solver_labels': True})

StartTime = time.time()

SolverResultsCase2 = Solver.solve(m, tee=True, warmstart=True)
#SolverResultsCase2 = Solver.solve(m, tee=True)

SolvingTime = time.time() - StartTime
print('Total solving time... ', round(SolvingTime), 's')

#%% print solution
SolverResultsCase2.write()
m.pprint()

# print individual values
print("Objective function - option minimize rolls: {}".format(value(m.eMinNumMR)))
print("total waste - option minimize rolls: {}".format(sum([m.vW[j].value for j in m.j])))
print("total rolls - option minimize rolls: {}".format(sum([m.vY[j].value for j in m.j])))

#%% Solution Case 3 - Objective function min rolls and logic included (option 1)

# we activate logic constraints (option 1)
m.eLogicOpt1a.activate()
m.eLogicOpt1b.activate()

# we unfix the aux binary variable
m.vD.unfix()

# lp file
m.write('PaperRollCut-minimize-rolls-logic-option1.lp', io_options={'symbolic_solver_labels': True})

StartTime = time.time()

SolverResultsCase3 = Solver.solve(m, tee=True, warmstart=True)
#SolverResultsCase3 = Solver.solve(m, tee=True)

SolvingTime = time.time() - StartTime
print('Total solving time... ', round(SolvingTime), 's')

#%% print solution
SolverResultsCase3.write()
m.pprint()

# print individual values
print("Objective function - option minimize rolls with logic (option 1): {}".format(value(m.eMinNumMR)))
print("total waste - option minimize rolls with logic (option 1): {}".format(sum([m.vW[j].value for j in m.j])))
print("total rolls - option minimize rolls with logic (option 1): {}".format(sum([m.vY[j].value for j in m.j])))

#%% Solution Case 4 - Objective function min rolls and logic included (option 2)

# we deactivate logic constraints option 1 and activate the option 2
m.eLogicOpt1a.deactivate()
m.eLogicOpt1b.deactivate()
m.eLogicOpt2.activate()

# we fix the aux binary variable to zero since the logic 2 doesn't need it
m.vD.fix(0)

# lp file
m.write('PaperRollCut-minimize-rolls-logic-option2.lp', io_options={'symbolic_solver_labels': True})

StartTime = time.time()

SolverResultsCase4 = Solver.solve(m, tee=True, warmstart=True) #warmstart for CBC being able to solve it (equivalen to mipstart option)
#SolverResultsCase4 = Solver.solve(m, tee=True)

SolvingTime = time.time() - StartTime
print('Total solving time... ', round(SolvingTime), 's')

#%% print solution
SolverResultsCase4.write()
m.pprint()

# print individual values
print("Objective function - option minimize rolls with logic (option 2): {}".format(value(m.eMinNumMR)))
print("total waste - option minimize rolls with logic (option 2): {}".format(sum([m.vW[j].value for j in m.j])))
print("total rolls - option minimize rolls with logic (option 2): {}".format(sum([m.vY[j].value for j in m.j])))
