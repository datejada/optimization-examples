\* Source Pyomo model name=Linea de metro *\

min 
ObjFun:
+4 vX(L1)
+4 vX(L2)
+4 vX(L3)
+4 vX(L4)
+3 vX(L5)
+4 vX(L6)
+3 vX(L7)
+3 vX(L8)

s.t.

c_l_eAssignation(P1)_:
+1 vX(L1)
+1 vX(L2)
+1 vX(L6)
>= 1

c_l_eAssignation(P10)_:
+1 vX(L4)
+1 vX(L6)
+1 vX(L8)
>= 1

c_l_eAssignation(P2)_:
+1 vX(L1)
+1 vX(L3)
+1 vX(L5)
+1 vX(L8)
>= 1

c_l_eAssignation(P3)_:
+1 vX(L1)
+1 vX(L2)
+1 vX(L3)
+1 vX(L7)
>= 1

c_l_eAssignation(P4)_:
+1 vX(L1)
+1 vX(L3)
+1 vX(L6)
>= 1

c_l_eAssignation(P5)_:
+1 vX(L2)
+1 vX(L4)
+1 vX(L6)
>= 1

c_l_eAssignation(P6)_:
+1 vX(L3)
+1 vX(L8)
>= 1

c_l_eAssignation(P7)_:
+1 vX(L2)
+1 vX(L4)
+1 vX(L5)
>= 1

c_l_eAssignation(P8)_:
+1 vX(L5)
+1 vX(L7)
>= 1

c_l_eAssignation(P9)_:
+1 vX(L4)
+1 vX(L7)
>= 1

c_l_point2_:
+1 vX(L1)
+1 vX(L3)
+1 vX(L5)
+1 vX(L8)
>= 2

c_u_transbordo_:
-2 vX(L2)
-1 vX(L7)
<= -2

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
   0 <= vX(L1) <= 1
   0 <= vX(L2) <= 1
   0 <= vX(L3) <= 1
   0 <= vX(L4) <= 1
   0 <= vX(L5) <= 1
   0 <= vX(L6) <= 1
   0 <= vX(L7) <= 1
   0 <= vX(L8) <= 1
binary
  vX(L1)
  vX(L2)
  vX(L3)
  vX(L4)
  vX(L5)
  vX(L6)
  vX(L7)
  vX(L8)
end
