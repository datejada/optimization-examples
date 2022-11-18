#%% import libraries

# getting only what we need from pyomo
from pyomo.environ import ConcreteModel, Set, Param, Var, Binary, NonNegativeReals, Reals, Constraint, Objective, minimize, Suffix, value
from pyomo.opt import SolverFactory

# other libraries
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

#%% input data

# sets
I = ['T1','T2','D1','D2','D3','P1','P2'] # all nodes
T = ['T1','T2'                         ] # source nodes
D = [          'D1','D2','D3'          ] # storage nodes
P = [                         'P1','P2'] # swimming pool nodes

# network connections
connections = {
    ('T1','D1'):1,
    ('D1','D2'):1,
    ('D1','P1'):1,
    ('D1','D3'):1,
    ('T2','D3'):1,
    ('D3','P2'):1,
    }

# scalar values
domestic_scarcity_cost       = 3  # EUR/m3
farming_scarcity_cost        = 1  # EUR/m3
two_pools_extra_closure_cost = 50 # EUR

# parameters
daily_domestic_consumption = ( # m3
    {'D1': 150,
     'D2': 100,
     'D3': 400,})

daily_farming_consumption = ( # m3
    {'D1': 100,
     'D2':  50,
     'D3':   0,})

daily_pools_consumption = ( # m3
    {'P1':  50,
     'P2':  25,})

close_pool_penalty = ( # EUR
    {'P1': 100,
     'P2':  50,})

daily_available_supply = ( # m3
    {'T1': 400,
     'T2': 400,})

# transportation cost
transport_cost = { # c€/m3
    ('T1','D1'):8,
    ('D1','D2'):2,
    ('D1','P1'):5,
    ('D1','D3'):4,
    ('T2','D3'):7,
    ('D3','P2'):5,
    }

#%% definitions

# model
mSP = ConcreteModel(name='Swimming Pools')

# sets
mSP.i  = Set(initialize=I    , doc='network nodes')
mSP.j  = Set(initialize=mSP.i, doc='network nodes') #alias of i
mSP.t  = Set(initialize=mSP.i, doc='source nodes' , filter=lambda mSP,i:i in T)
mSP.d  = Set(initialize=mSP.i, doc='storage nodes', filter=lambda mSP,i:i in D)
mSP.p  = Set(initialize=mSP.i, doc='pools nodes'  , filter=lambda mSP,i:i in P)

mSP.ij = Set(initialize=mSP.i*mSP.j, doc='set of connections', filter=lambda mSP,i,j:(i,j) in connections)

# parameters
mSP.pDSCost = Param(initialize=domestic_scarcity_cost       , doc='domestic scarcity cost in EUR/m3'      )
mSP.pFSCost = Param(initialize=farming_scarcity_cost        , doc='farming  scarcity cost in EUR/m3'      )
mSP.pPECost = Param(initialize=two_pools_extra_closure_cost , doc='extra closure cost of two pools in EUR')

mSP.pDDCons = Param(mSP.d, initialize=daily_domestic_consumption, doc='daily domestic consumption in m3', default=0)
mSP.pDFCons = Param(mSP.d, initialize=daily_farming_consumption , doc='daily farming  consumption in m3', default=0)
mSP.pDPCons = Param(mSP.p, initialize=daily_pools_consumption   , doc='daily pools    consumption in m3', default=0)
mSP.pDASupp = Param(mSP.t, initialize=daily_available_supply    , doc='daily available supply     in m3', default=0)
mSP.pPCCost = Param(mSP.p, initialize=close_pool_penalty        , doc='penalty cost of closing pool p in EUR')

mSP.pTRCost = Param(mSP.i,mSP.j, initialize=transport_cost      , doc='transport_cost          in c€/m3', default=0)
mSP.pConnec = Param(mSP.i,mSP.j, initialize=connections         , doc='connections among nodes'         , default=0)

# variables
mSP.vFlow         = Var(mSP.ij, within=Reals           , doc='daily flow from node i to j       in m3'                                          )
mSP.vDomScar      = Var(mSP.d , within=NonNegativeReals, doc='daily domestic scarcity in node d in m3', bounds=lambda mSP,d:(0.0,mSP.pDDCons[d]))
mSP.vFarScar      = Var(mSP.d , within=NonNegativeReals, doc='daily farming  scarcity in node d in m3', bounds=lambda mSP,d:(0.0,mSP.pDFCons[d]))
mSP.vPoolOpen     = Var(mSP.p , within=Binary          , doc='binary decision to close or not      pool p     (0-> close            , 1->       open)')
mSP.v2PoolsClosed = Var(        within=Binary          , doc='binary decision to know if both pool are closed (0-> at least one open, 1-> both close)')

# constraints
def eStorageNodeBalance_rule(mSP,i):
    return ( + sum(mSP.vFlow[j,i] for j in mSP.j if mSP.pConnec[j,i]==1)     # connections for node i to node d
             - sum(mSP.vFlow[i,j] for j in mSP.j if mSP.pConnec[i,j]==1)     # connections for node d to node j
            == mSP.pDDCons[i]-mSP.vDomScar[i]   # actual domestic consumption
             + mSP.pDFCons[i]-mSP.vFarScar[i] ) # actual farming  consumption
mSP.eStorageNodeBalance = Constraint(mSP.d, rule=eStorageNodeBalance_rule, doc='storage node balance constraint')

def eMaxAvaiSupply_rule(mSP,i,j):
    if mSP.pConnec[i,j]==1:
        return (0, mSP.vFlow[i,j], mSP.pDASupp[i])
    else:
        return Constraint.Skip
mSP.eMaxAvaiSupply = Constraint(mSP.t,mSP.j,rule=eMaxAvaiSupply_rule,doc='bounds for supply nodes')

def ePoolOpen_rule(mSP,i):
    return sum(mSP.vFlow[j,i] for j in mSP.j if mSP.pConnec[j,i]==1) == mSP.pDPCons[i]*mSP.vPoolOpen[i]
mSP.ePoolOpen = Constraint(mSP.p, rule=ePoolOpen_rule, doc='swimming pools flow definition considering if it is open or not')

def eLogic1_2PoolsClosed_rule(mSP):
    return sum(mSP.vPoolOpen[p] for p in mSP.p) >=   (1-mSP.v2PoolsClosed)
mSP.eLogic1_2PoolsClosed = Constraint(rule=eLogic1_2PoolsClosed_rule, doc='first  logic to determine if both pools are closed or not')

def eLogic2_2PoolsClosed_rule(mSP):
    return sum(mSP.vPoolOpen[p] for p in mSP.p) <= 2*(1-mSP.v2PoolsClosed)
mSP.eLogic2_2PoolsClosed = Constraint(rule=eLogic2_2PoolsClosed_rule, doc='second logic to determine if both pools are closed or not')

# objective function
def eObj_rule(mSP):
    return (+ sum(mSP.pTRCost[i,j]*mSP.vFlow[i,j]/100 for i,j in mSP.i*mSP.j if mSP.pConnec[i,j]==1) # transport cost
            + mSP.pDSCost*sum(mSP.vDomScar[d] for d in mSP.d) # domestic scarcity penalization
            + mSP.pFSCost*sum(mSP.vFarScar[d] for d in mSP.d) # farming  scarcity penalization
            +             sum(mSP.pPCCost [p]*(1-mSP.vPoolOpen    [p]) for p in mSP.p) # penalty cost of closing pools
            +                 mSP.pPECost    *   mSP.v2PoolsClosed                     # extra penalty cost of closing both pools
            )
mSP.ObjFun = Objective(rule=eObj_rule, sense=minimize)


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
mSP.write('swimming-pools.lp', io_options={'symbolic_solver_labels': True})

# solve
SolverResults = Solver.solve(mSP, tee=True)

#%% print solution
mSP.pprint()

#%% print all variables results

# flow results
mSP.vFlow.pprint()         
mSP.vDomScar.pprint()      
mSP.vFarScar.pprint()      
mSP.vPoolOpen.pprint()     
mSP.v2PoolsClosed.pprint() 

#%% print results

# objective function
print('Total cost: ' + str(value(mSP.ObjFun)))

#%% network graph

# creating the graph object
G = nx.DiGraph()

# adding the topology
for i,j in mSP.ij:
    G.add_edge(i,j,weight=value(mSP.vFlow[i,j]))

edge_labels = nx.get_edge_attributes(G, "weight")
edges       = [e     for e,w in edge_labels.items()]
colors      = [w/100 for e,w in edge_labels.items()]
color_bar   = [w     for e,w in edge_labels.items()]
cmap        = plt.cm.RdYlBu_r
node_size   = 1500

# positions in the network
pos = {'T1':(4,8),
       'T2':(8,8),
       'D1':(4,4),
       'D2':(0,4),
       'D3':(8,4),
       'P1':(4,0),
       'P2':(8,0)}

# drawing the network

nodes = nx.draw_networkx_nodes(G,
                               pos,
                               node_size=node_size,
                               node_color='white',
                               edgecolors='black')

labels= nx.draw_networkx_labels(G,
                                pos,
                                labels={n:n for n in G.nodes()},
                                font_size=16)

edges = nx.draw_networkx_edges(G,
                               pos,
                               node_size=node_size,
                               edgelist=edges,
                               edge_color=colors,
                               arrowstyle="->",
                               arrowsize=10,
                               width=2.5,
                               edge_cmap=cmap)

# Set colorbar, margins, and saving the figure
pc = mpl.collections.PatchCollection(edges, cmap=cmap)
pc.set_array(color_bar)
ax = plt.gca()
ax.margins(0.10)
plt.axis("off")
plt.colorbar(pc, ax=ax)
plt.savefig('swimming-pools.png',dpi=500)
plt.show()


# %%
