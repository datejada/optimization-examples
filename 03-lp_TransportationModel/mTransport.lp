\* Source Pyomo model name=Transportation Problem *\

min 
eCost:
+0.14999999999999999 vX(Algeciras_Barcelona)
+0.050000000000000003 vX(Algeciras_Madrid)
+0.11 vX(Algeciras_Valencia)
+0.12 vX(Vigo_Barcelona)
+0.059999999999999998 vX(Vigo_Madrid)
+0.089999999999999997 vX(Vigo_Valencia)

s.t.

c_u_eCapacity(Algeciras)_:
+1 vX(Algeciras_Barcelona)
+1 vX(Algeciras_Madrid)
+1 vX(Algeciras_Valencia)
<= 700

c_u_eCapacity(Vigo)_:
+1 vX(Vigo_Barcelona)
+1 vX(Vigo_Madrid)
+1 vX(Vigo_Valencia)
<= 350

c_l_eDemand(Barcelona)_:
+1 vX(Algeciras_Barcelona)
+1 vX(Vigo_Barcelona)
>= 450

c_l_eDemand(Madrid)_:
+1 vX(Algeciras_Madrid)
+1 vX(Vigo_Madrid)
>= 600

c_l_eDemand(Valencia)_:
+1 vX(Algeciras_Valencia)
+1 vX(Vigo_Valencia)
>= 150

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
   0 <= vX(Algeciras_Barcelona) <= +inf
   0 <= vX(Algeciras_Madrid) <= +inf
   0 <= vX(Algeciras_Valencia) <= +inf
   0 <= vX(Vigo_Barcelona) <= +inf
   0 <= vX(Vigo_Madrid) <= +inf
   0 <= vX(Vigo_Valencia) <= +inf
end
