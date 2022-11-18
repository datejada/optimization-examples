\* Source Pyomo model name=Crew Assignment *\

min 
ObjFun:
+2 vX(Seq1)
+9 vX(Seq10)
+8 vX(Seq11)
+9 vX(Seq12)
+3 vX(Seq2)
+4 vX(Seq3)
+6 vX(Seq4)
+7 vX(Seq5)
+5 vX(Seq6)
+7 vX(Seq7)
+8 vX(Seq8)
+9 vX(Seq9)

s.t.

c_l_eAssignation(Chicago___Denver)_:
+1 vX(Seq4)
+1 vX(Seq5)
+1 vX(Seq9)
>= 1

c_l_eAssignation(Chicago___Seattle)_:
+1 vX(Seq10)
+1 vX(Seq11)
+1 vX(Seq12)
+1 vX(Seq7)
+1 vX(Seq8)
>= 1

c_l_eAssignation(Denver___Chicago)_:
+1 vX(Seq11)
+1 vX(Seq5)
+1 vX(Seq8)
>= 1

c_l_eAssignation(Denver___San_Francisco)_:
+1 vX(Seq2)
+1 vX(Seq4)
+1 vX(Seq5)
+1 vX(Seq9)
>= 1

c_l_eAssignation(Los_Angeles___Chicago)_:
+1 vX(Seq10)
+1 vX(Seq12)
+1 vX(Seq4)
+1 vX(Seq7)
+1 vX(Seq9)
>= 1

c_l_eAssignation(Los_Angeles___San_Francisco)_:
+1 vX(Seq1)
+1 vX(Seq10)
+1 vX(Seq11)
+1 vX(Seq6)
>= 1

c_l_eAssignation(San_Francisco___Denver)_:
+1 vX(Seq11)
+1 vX(Seq2)
+1 vX(Seq5)
+1 vX(Seq8)
>= 1

c_l_eAssignation(San_Francisco___Los_Angeles)_:
+1 vX(Seq1)
+1 vX(Seq10)
+1 vX(Seq4)
+1 vX(Seq7)
>= 1

c_l_eAssignation(San_Francisco___Seattle)_:
+1 vX(Seq12)
+1 vX(Seq3)
+1 vX(Seq6)
+1 vX(Seq9)
>= 1

c_l_eAssignation(Seattle___Los_Angeles)_:
+1 vX(Seq10)
+1 vX(Seq11)
+1 vX(Seq12)
+1 vX(Seq6)
+1 vX(Seq9)
>= 1

c_l_eAssignation(Seattle___San_Francisco)_:
+1 vX(Seq12)
+1 vX(Seq3)
+1 vX(Seq7)
+1 vX(Seq8)
>= 1

c_e_eMinCrew_:
+1 vX(Seq1)
+1 vX(Seq10)
+1 vX(Seq11)
+1 vX(Seq12)
+1 vX(Seq2)
+1 vX(Seq3)
+1 vX(Seq4)
+1 vX(Seq5)
+1 vX(Seq6)
+1 vX(Seq7)
+1 vX(Seq8)
+1 vX(Seq9)
= 3

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
   0 <= vX(Seq1) <= 1
   0 <= vX(Seq10) <= 1
   0 <= vX(Seq11) <= 1
   0 <= vX(Seq12) <= 1
   0 <= vX(Seq2) <= 1
   0 <= vX(Seq3) <= 1
   0 <= vX(Seq4) <= 1
   0 <= vX(Seq5) <= 1
   0 <= vX(Seq6) <= 1
   0 <= vX(Seq7) <= 1
   0 <= vX(Seq8) <= 1
   0 <= vX(Seq9) <= 1
binary
  vX(Seq1)
  vX(Seq10)
  vX(Seq11)
  vX(Seq12)
  vX(Seq2)
  vX(Seq3)
  vX(Seq4)
  vX(Seq5)
  vX(Seq6)
  vX(Seq7)
  vX(Seq8)
  vX(Seq9)
end
