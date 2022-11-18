\* Source Pyomo model name=Burrito Challange *\

max 
ObjFun:
-250 vX(truck10)
-250 vX(truck11)
-250 vX(truck16)
-250 vX(truck18)
-250 vX(truck21)
-250 vX(truck22)
-250 vX(truck26)
-250 vX(truck28)
-250 vX(truck37)
-250 vX(truck38)
-250 vX(truck39)
-250 vX(truck40)
-250 vX(truck41)
-250 vX(truck44)
-250 vX(truck51)
-250 vX(truck53)
+45 vY(demand11_truck10)
+30 vY(demand11_truck11)
+100 vY(demand11_truck16)
+90 vY(demand11_truck18)
+30 vY(demand11_truck21)
+65 vY(demand11_truck22)
+5 vY(demand11_truck26)
+5 vY(demand11_truck28)
+65 vY(demand11_truck44)
+75 vY(demand11_truck53)
+15 vY(demand22_truck10)
+5 vY(demand22_truck11)
+30 vY(demand22_truck16)
+45 vY(demand22_truck18)
+10 vY(demand22_truck21)
+25 vY(demand22_truck22)
+10 vY(demand22_truck28)
+40 vY(demand22_truck44)
+10 vY(demand22_truck53)
+50 vY(demand31_truck26)
+25 vY(demand31_truck28)
+25 vY(demand31_truck37)
+50 vY(demand31_truck38)
+20 vY(demand31_truck39)
+30 vY(demand31_truck40)
+5 vY(demand31_truck41)
+20 vY(demand31_truck51)
+10 vY(demand31_truck53)
+95 vY(demand32_truck26)
+100 vY(demand32_truck28)
+145 vY(demand32_truck37)
+140 vY(demand32_truck38)
+50 vY(demand32_truck39)
+80 vY(demand32_truck40)
+85 vY(demand32_truck41)
+10 vY(demand32_truck44)
+40 vY(demand32_truck51)
+100 vY(demand33_truck26)
+195 vY(demand33_truck28)
+200 vY(demand33_truck37)
+105 vY(demand33_truck38)
+25 vY(demand33_truck40)
+120 vY(demand33_truck41)
+75 vY(demand33_truck44)
+5 vY(demand41_truck26)
+45 vY(demand41_truck28)
+75 vY(demand41_truck37)
+35 vY(demand41_truck38)
+50 vY(demand41_truck39)
+75 vY(demand41_truck40)
+100 vY(demand41_truck41)
+50 vY(demand41_truck51)
+5 vY(demand43_truck26)
+5 vY(demand43_truck37)
+15 vY(demand43_truck38)
+20 vY(demand43_truck39)
+25 vY(demand43_truck40)
+10 vY(demand43_truck41)
+25 vY(demand43_truck51)
+15 vY(demand44_truck26)
+35 vY(demand44_truck28)
+65 vY(demand44_truck37)
+45 vY(demand44_truck38)
+60 vY(demand44_truck39)
+85 vY(demand44_truck40)
+100 vY(demand44_truck41)
+60 vY(demand44_truck51)
+35 vY(demand46_truck26)
+10 vY(demand46_truck28)
+25 vY(demand46_truck37)
+50 vY(demand46_truck38)
+35 vY(demand46_truck39)
+50 vY(demand46_truck40)
+25 vY(demand46_truck41)
+35 vY(demand46_truck51)
+75 vY(demand4_truck10)
+95 vY(demand4_truck11)
+20 vY(demand4_truck16)
+35 vY(demand4_truck18)
+40 vY(demand4_truck21)
+70 vY(demand4_truck22)
+110 vY(demand51_truck10)
+80 vY(demand51_truck11)
+135 vY(demand51_truck16)
+150 vY(demand51_truck18)
+90 vY(demand51_truck21)
+135 vY(demand51_truck22)
+80 vY(demand51_truck44)
+50 vY(demand51_truck53)
+90 vY(demand53_truck10)
+75 vY(demand53_truck11)
+30 vY(demand53_truck16)
+35 vY(demand53_truck18)
+40 vY(demand53_truck21)
+75 vY(demand53_truck22)
+45 vY(demand53_truck53)
+30 vY(demand5_truck10)
+30 vY(demand5_truck11)
+15 vY(demand5_truck16)
+20 vY(demand5_truck18)
+20 vY(demand5_truck21)
+40 vY(demand5_truck22)
+15 vY(demand7_truck10)
+5 vY(demand7_truck11)
+5 vY(demand7_truck18)
+40 vY(demand7_truck21)
+25 vY(demand7_truck22)
+150 vY(demand8_truck10)
+150 vY(demand8_truck11)
+50 vY(demand8_truck16)
+65 vY(demand8_truck18)
+75 vY(demand8_truck21)
+125 vY(demand8_truck22)

s.t.

c_u_eAssignation1(demand11)_:
+1 vY(demand11_truck10)
+1 vY(demand11_truck11)
+1 vY(demand11_truck16)
+1 vY(demand11_truck18)
+1 vY(demand11_truck21)
+1 vY(demand11_truck22)
+1 vY(demand11_truck26)
+1 vY(demand11_truck28)
+1 vY(demand11_truck44)
+1 vY(demand11_truck53)
<= 1

c_u_eAssignation1(demand22)_:
+1 vY(demand22_truck10)
+1 vY(demand22_truck11)
+1 vY(demand22_truck16)
+1 vY(demand22_truck18)
+1 vY(demand22_truck21)
+1 vY(demand22_truck22)
+1 vY(demand22_truck28)
+1 vY(demand22_truck44)
+1 vY(demand22_truck53)
<= 1

c_u_eAssignation1(demand31)_:
+1 vY(demand31_truck26)
+1 vY(demand31_truck28)
+1 vY(demand31_truck37)
+1 vY(demand31_truck38)
+1 vY(demand31_truck39)
+1 vY(demand31_truck40)
+1 vY(demand31_truck41)
+1 vY(demand31_truck51)
+1 vY(demand31_truck53)
<= 1

c_u_eAssignation1(demand32)_:
+1 vY(demand32_truck26)
+1 vY(demand32_truck28)
+1 vY(demand32_truck37)
+1 vY(demand32_truck38)
+1 vY(demand32_truck39)
+1 vY(demand32_truck40)
+1 vY(demand32_truck41)
+1 vY(demand32_truck44)
+1 vY(demand32_truck51)
<= 1

c_u_eAssignation1(demand33)_:
+1 vY(demand33_truck26)
+1 vY(demand33_truck28)
+1 vY(demand33_truck37)
+1 vY(demand33_truck38)
+1 vY(demand33_truck40)
+1 vY(demand33_truck41)
+1 vY(demand33_truck44)
<= 1

c_u_eAssignation1(demand4)_:
+1 vY(demand4_truck10)
+1 vY(demand4_truck11)
+1 vY(demand4_truck16)
+1 vY(demand4_truck18)
+1 vY(demand4_truck21)
+1 vY(demand4_truck22)
<= 1

c_u_eAssignation1(demand41)_:
+1 vY(demand41_truck26)
+1 vY(demand41_truck28)
+1 vY(demand41_truck37)
+1 vY(demand41_truck38)
+1 vY(demand41_truck39)
+1 vY(demand41_truck40)
+1 vY(demand41_truck41)
+1 vY(demand41_truck51)
<= 1

c_u_eAssignation1(demand43)_:
+1 vY(demand43_truck26)
+1 vY(demand43_truck37)
+1 vY(demand43_truck38)
+1 vY(demand43_truck39)
+1 vY(demand43_truck40)
+1 vY(demand43_truck41)
+1 vY(demand43_truck51)
<= 1

c_u_eAssignation1(demand44)_:
+1 vY(demand44_truck26)
+1 vY(demand44_truck28)
+1 vY(demand44_truck37)
+1 vY(demand44_truck38)
+1 vY(demand44_truck39)
+1 vY(demand44_truck40)
+1 vY(demand44_truck41)
+1 vY(demand44_truck51)
<= 1

c_u_eAssignation1(demand46)_:
+1 vY(demand46_truck26)
+1 vY(demand46_truck28)
+1 vY(demand46_truck37)
+1 vY(demand46_truck38)
+1 vY(demand46_truck39)
+1 vY(demand46_truck40)
+1 vY(demand46_truck41)
+1 vY(demand46_truck51)
<= 1

c_u_eAssignation1(demand5)_:
+1 vY(demand5_truck10)
+1 vY(demand5_truck11)
+1 vY(demand5_truck16)
+1 vY(demand5_truck18)
+1 vY(demand5_truck21)
+1 vY(demand5_truck22)
<= 1

c_u_eAssignation1(demand51)_:
+1 vY(demand51_truck10)
+1 vY(demand51_truck11)
+1 vY(demand51_truck16)
+1 vY(demand51_truck18)
+1 vY(demand51_truck21)
+1 vY(demand51_truck22)
+1 vY(demand51_truck44)
+1 vY(demand51_truck53)
<= 1

c_u_eAssignation1(demand53)_:
+1 vY(demand53_truck10)
+1 vY(demand53_truck11)
+1 vY(demand53_truck16)
+1 vY(demand53_truck18)
+1 vY(demand53_truck21)
+1 vY(demand53_truck22)
+1 vY(demand53_truck53)
<= 1

c_u_eAssignation1(demand7)_:
+1 vY(demand7_truck10)
+1 vY(demand7_truck11)
+1 vY(demand7_truck18)
+1 vY(demand7_truck21)
+1 vY(demand7_truck22)
<= 1

c_u_eAssignation1(demand8)_:
+1 vY(demand8_truck10)
+1 vY(demand8_truck11)
+1 vY(demand8_truck16)
+1 vY(demand8_truck18)
+1 vY(demand8_truck21)
+1 vY(demand8_truck22)
<= 1

c_u_eAssignation2(demand11_truck10)_:
-1 vX(truck10)
+1 vY(demand11_truck10)
<= 0

c_u_eAssignation2(demand11_truck11)_:
-1 vX(truck11)
+1 vY(demand11_truck11)
<= 0

c_u_eAssignation2(demand11_truck16)_:
-1 vX(truck16)
+1 vY(demand11_truck16)
<= 0

c_u_eAssignation2(demand11_truck18)_:
-1 vX(truck18)
+1 vY(demand11_truck18)
<= 0

c_u_eAssignation2(demand11_truck21)_:
-1 vX(truck21)
+1 vY(demand11_truck21)
<= 0

c_u_eAssignation2(demand11_truck22)_:
-1 vX(truck22)
+1 vY(demand11_truck22)
<= 0

c_u_eAssignation2(demand11_truck26)_:
-1 vX(truck26)
+1 vY(demand11_truck26)
<= 0

c_u_eAssignation2(demand11_truck28)_:
-1 vX(truck28)
+1 vY(demand11_truck28)
<= 0

c_u_eAssignation2(demand11_truck44)_:
-1 vX(truck44)
+1 vY(demand11_truck44)
<= 0

c_u_eAssignation2(demand11_truck53)_:
-1 vX(truck53)
+1 vY(demand11_truck53)
<= 0

c_u_eAssignation2(demand22_truck10)_:
-1 vX(truck10)
+1 vY(demand22_truck10)
<= 0

c_u_eAssignation2(demand22_truck11)_:
-1 vX(truck11)
+1 vY(demand22_truck11)
<= 0

c_u_eAssignation2(demand22_truck16)_:
-1 vX(truck16)
+1 vY(demand22_truck16)
<= 0

c_u_eAssignation2(demand22_truck18)_:
-1 vX(truck18)
+1 vY(demand22_truck18)
<= 0

c_u_eAssignation2(demand22_truck21)_:
-1 vX(truck21)
+1 vY(demand22_truck21)
<= 0

c_u_eAssignation2(demand22_truck22)_:
-1 vX(truck22)
+1 vY(demand22_truck22)
<= 0

c_u_eAssignation2(demand22_truck28)_:
-1 vX(truck28)
+1 vY(demand22_truck28)
<= 0

c_u_eAssignation2(demand22_truck44)_:
-1 vX(truck44)
+1 vY(demand22_truck44)
<= 0

c_u_eAssignation2(demand22_truck53)_:
-1 vX(truck53)
+1 vY(demand22_truck53)
<= 0

c_u_eAssignation2(demand31_truck26)_:
-1 vX(truck26)
+1 vY(demand31_truck26)
<= 0

c_u_eAssignation2(demand31_truck28)_:
-1 vX(truck28)
+1 vY(demand31_truck28)
<= 0

c_u_eAssignation2(demand31_truck37)_:
-1 vX(truck37)
+1 vY(demand31_truck37)
<= 0

c_u_eAssignation2(demand31_truck38)_:
-1 vX(truck38)
+1 vY(demand31_truck38)
<= 0

c_u_eAssignation2(demand31_truck39)_:
-1 vX(truck39)
+1 vY(demand31_truck39)
<= 0

c_u_eAssignation2(demand31_truck40)_:
-1 vX(truck40)
+1 vY(demand31_truck40)
<= 0

c_u_eAssignation2(demand31_truck41)_:
-1 vX(truck41)
+1 vY(demand31_truck41)
<= 0

c_u_eAssignation2(demand31_truck51)_:
-1 vX(truck51)
+1 vY(demand31_truck51)
<= 0

c_u_eAssignation2(demand31_truck53)_:
-1 vX(truck53)
+1 vY(demand31_truck53)
<= 0

c_u_eAssignation2(demand32_truck26)_:
-1 vX(truck26)
+1 vY(demand32_truck26)
<= 0

c_u_eAssignation2(demand32_truck28)_:
-1 vX(truck28)
+1 vY(demand32_truck28)
<= 0

c_u_eAssignation2(demand32_truck37)_:
-1 vX(truck37)
+1 vY(demand32_truck37)
<= 0

c_u_eAssignation2(demand32_truck38)_:
-1 vX(truck38)
+1 vY(demand32_truck38)
<= 0

c_u_eAssignation2(demand32_truck39)_:
-1 vX(truck39)
+1 vY(demand32_truck39)
<= 0

c_u_eAssignation2(demand32_truck40)_:
-1 vX(truck40)
+1 vY(demand32_truck40)
<= 0

c_u_eAssignation2(demand32_truck41)_:
-1 vX(truck41)
+1 vY(demand32_truck41)
<= 0

c_u_eAssignation2(demand32_truck44)_:
-1 vX(truck44)
+1 vY(demand32_truck44)
<= 0

c_u_eAssignation2(demand32_truck51)_:
-1 vX(truck51)
+1 vY(demand32_truck51)
<= 0

c_u_eAssignation2(demand33_truck26)_:
-1 vX(truck26)
+1 vY(demand33_truck26)
<= 0

c_u_eAssignation2(demand33_truck28)_:
-1 vX(truck28)
+1 vY(demand33_truck28)
<= 0

c_u_eAssignation2(demand33_truck37)_:
-1 vX(truck37)
+1 vY(demand33_truck37)
<= 0

c_u_eAssignation2(demand33_truck38)_:
-1 vX(truck38)
+1 vY(demand33_truck38)
<= 0

c_u_eAssignation2(demand33_truck40)_:
-1 vX(truck40)
+1 vY(demand33_truck40)
<= 0

c_u_eAssignation2(demand33_truck41)_:
-1 vX(truck41)
+1 vY(demand33_truck41)
<= 0

c_u_eAssignation2(demand33_truck44)_:
-1 vX(truck44)
+1 vY(demand33_truck44)
<= 0

c_u_eAssignation2(demand4_truck10)_:
-1 vX(truck10)
+1 vY(demand4_truck10)
<= 0

c_u_eAssignation2(demand4_truck11)_:
-1 vX(truck11)
+1 vY(demand4_truck11)
<= 0

c_u_eAssignation2(demand4_truck16)_:
-1 vX(truck16)
+1 vY(demand4_truck16)
<= 0

c_u_eAssignation2(demand4_truck18)_:
-1 vX(truck18)
+1 vY(demand4_truck18)
<= 0

c_u_eAssignation2(demand4_truck21)_:
-1 vX(truck21)
+1 vY(demand4_truck21)
<= 0

c_u_eAssignation2(demand4_truck22)_:
-1 vX(truck22)
+1 vY(demand4_truck22)
<= 0

c_u_eAssignation2(demand41_truck26)_:
-1 vX(truck26)
+1 vY(demand41_truck26)
<= 0

c_u_eAssignation2(demand41_truck28)_:
-1 vX(truck28)
+1 vY(demand41_truck28)
<= 0

c_u_eAssignation2(demand41_truck37)_:
-1 vX(truck37)
+1 vY(demand41_truck37)
<= 0

c_u_eAssignation2(demand41_truck38)_:
-1 vX(truck38)
+1 vY(demand41_truck38)
<= 0

c_u_eAssignation2(demand41_truck39)_:
-1 vX(truck39)
+1 vY(demand41_truck39)
<= 0

c_u_eAssignation2(demand41_truck40)_:
-1 vX(truck40)
+1 vY(demand41_truck40)
<= 0

c_u_eAssignation2(demand41_truck41)_:
-1 vX(truck41)
+1 vY(demand41_truck41)
<= 0

c_u_eAssignation2(demand41_truck51)_:
-1 vX(truck51)
+1 vY(demand41_truck51)
<= 0

c_u_eAssignation2(demand43_truck26)_:
-1 vX(truck26)
+1 vY(demand43_truck26)
<= 0

c_u_eAssignation2(demand43_truck37)_:
-1 vX(truck37)
+1 vY(demand43_truck37)
<= 0

c_u_eAssignation2(demand43_truck38)_:
-1 vX(truck38)
+1 vY(demand43_truck38)
<= 0

c_u_eAssignation2(demand43_truck39)_:
-1 vX(truck39)
+1 vY(demand43_truck39)
<= 0

c_u_eAssignation2(demand43_truck40)_:
-1 vX(truck40)
+1 vY(demand43_truck40)
<= 0

c_u_eAssignation2(demand43_truck41)_:
-1 vX(truck41)
+1 vY(demand43_truck41)
<= 0

c_u_eAssignation2(demand43_truck51)_:
-1 vX(truck51)
+1 vY(demand43_truck51)
<= 0

c_u_eAssignation2(demand44_truck26)_:
-1 vX(truck26)
+1 vY(demand44_truck26)
<= 0

c_u_eAssignation2(demand44_truck28)_:
-1 vX(truck28)
+1 vY(demand44_truck28)
<= 0

c_u_eAssignation2(demand44_truck37)_:
-1 vX(truck37)
+1 vY(demand44_truck37)
<= 0

c_u_eAssignation2(demand44_truck38)_:
-1 vX(truck38)
+1 vY(demand44_truck38)
<= 0

c_u_eAssignation2(demand44_truck39)_:
-1 vX(truck39)
+1 vY(demand44_truck39)
<= 0

c_u_eAssignation2(demand44_truck40)_:
-1 vX(truck40)
+1 vY(demand44_truck40)
<= 0

c_u_eAssignation2(demand44_truck41)_:
-1 vX(truck41)
+1 vY(demand44_truck41)
<= 0

c_u_eAssignation2(demand44_truck51)_:
-1 vX(truck51)
+1 vY(demand44_truck51)
<= 0

c_u_eAssignation2(demand46_truck26)_:
-1 vX(truck26)
+1 vY(demand46_truck26)
<= 0

c_u_eAssignation2(demand46_truck28)_:
-1 vX(truck28)
+1 vY(demand46_truck28)
<= 0

c_u_eAssignation2(demand46_truck37)_:
-1 vX(truck37)
+1 vY(demand46_truck37)
<= 0

c_u_eAssignation2(demand46_truck38)_:
-1 vX(truck38)
+1 vY(demand46_truck38)
<= 0

c_u_eAssignation2(demand46_truck39)_:
-1 vX(truck39)
+1 vY(demand46_truck39)
<= 0

c_u_eAssignation2(demand46_truck40)_:
-1 vX(truck40)
+1 vY(demand46_truck40)
<= 0

c_u_eAssignation2(demand46_truck41)_:
-1 vX(truck41)
+1 vY(demand46_truck41)
<= 0

c_u_eAssignation2(demand46_truck51)_:
-1 vX(truck51)
+1 vY(demand46_truck51)
<= 0

c_u_eAssignation2(demand5_truck10)_:
-1 vX(truck10)
+1 vY(demand5_truck10)
<= 0

c_u_eAssignation2(demand5_truck11)_:
-1 vX(truck11)
+1 vY(demand5_truck11)
<= 0

c_u_eAssignation2(demand5_truck16)_:
-1 vX(truck16)
+1 vY(demand5_truck16)
<= 0

c_u_eAssignation2(demand5_truck18)_:
-1 vX(truck18)
+1 vY(demand5_truck18)
<= 0

c_u_eAssignation2(demand5_truck21)_:
-1 vX(truck21)
+1 vY(demand5_truck21)
<= 0

c_u_eAssignation2(demand5_truck22)_:
-1 vX(truck22)
+1 vY(demand5_truck22)
<= 0

c_u_eAssignation2(demand51_truck10)_:
-1 vX(truck10)
+1 vY(demand51_truck10)
<= 0

c_u_eAssignation2(demand51_truck11)_:
-1 vX(truck11)
+1 vY(demand51_truck11)
<= 0

c_u_eAssignation2(demand51_truck16)_:
-1 vX(truck16)
+1 vY(demand51_truck16)
<= 0

c_u_eAssignation2(demand51_truck18)_:
-1 vX(truck18)
+1 vY(demand51_truck18)
<= 0

c_u_eAssignation2(demand51_truck21)_:
-1 vX(truck21)
+1 vY(demand51_truck21)
<= 0

c_u_eAssignation2(demand51_truck22)_:
-1 vX(truck22)
+1 vY(demand51_truck22)
<= 0

c_u_eAssignation2(demand51_truck44)_:
-1 vX(truck44)
+1 vY(demand51_truck44)
<= 0

c_u_eAssignation2(demand51_truck53)_:
-1 vX(truck53)
+1 vY(demand51_truck53)
<= 0

c_u_eAssignation2(demand53_truck10)_:
-1 vX(truck10)
+1 vY(demand53_truck10)
<= 0

c_u_eAssignation2(demand53_truck11)_:
-1 vX(truck11)
+1 vY(demand53_truck11)
<= 0

c_u_eAssignation2(demand53_truck16)_:
-1 vX(truck16)
+1 vY(demand53_truck16)
<= 0

c_u_eAssignation2(demand53_truck18)_:
-1 vX(truck18)
+1 vY(demand53_truck18)
<= 0

c_u_eAssignation2(demand53_truck21)_:
-1 vX(truck21)
+1 vY(demand53_truck21)
<= 0

c_u_eAssignation2(demand53_truck22)_:
-1 vX(truck22)
+1 vY(demand53_truck22)
<= 0

c_u_eAssignation2(demand53_truck53)_:
-1 vX(truck53)
+1 vY(demand53_truck53)
<= 0

c_u_eAssignation2(demand7_truck10)_:
-1 vX(truck10)
+1 vY(demand7_truck10)
<= 0

c_u_eAssignation2(demand7_truck11)_:
-1 vX(truck11)
+1 vY(demand7_truck11)
<= 0

c_u_eAssignation2(demand7_truck18)_:
-1 vX(truck18)
+1 vY(demand7_truck18)
<= 0

c_u_eAssignation2(demand7_truck21)_:
-1 vX(truck21)
+1 vY(demand7_truck21)
<= 0

c_u_eAssignation2(demand7_truck22)_:
-1 vX(truck22)
+1 vY(demand7_truck22)
<= 0

c_u_eAssignation2(demand8_truck10)_:
-1 vX(truck10)
+1 vY(demand8_truck10)
<= 0

c_u_eAssignation2(demand8_truck11)_:
-1 vX(truck11)
+1 vY(demand8_truck11)
<= 0

c_u_eAssignation2(demand8_truck16)_:
-1 vX(truck16)
+1 vY(demand8_truck16)
<= 0

c_u_eAssignation2(demand8_truck18)_:
-1 vX(truck18)
+1 vY(demand8_truck18)
<= 0

c_u_eAssignation2(demand8_truck21)_:
-1 vX(truck21)
+1 vY(demand8_truck21)
<= 0

c_u_eAssignation2(demand8_truck22)_:
-1 vX(truck22)
+1 vY(demand8_truck22)
<= 0

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
   0 <= vX(truck10) <= 1
   0 <= vX(truck11) <= 1
   0 <= vX(truck16) <= 1
   0 <= vX(truck18) <= 1
   0 <= vX(truck21) <= 1
   0 <= vX(truck22) <= 1
   0 <= vX(truck26) <= 1
   0 <= vX(truck28) <= 1
   0 <= vX(truck37) <= 1
   0 <= vX(truck38) <= 1
   0 <= vX(truck39) <= 1
   0 <= vX(truck40) <= 1
   0 <= vX(truck41) <= 1
   0 <= vX(truck44) <= 1
   0 <= vX(truck51) <= 1
   0 <= vX(truck53) <= 1
   0 <= vY(demand11_truck10) <= 1
   0 <= vY(demand11_truck11) <= 1
   0 <= vY(demand11_truck16) <= 1
   0 <= vY(demand11_truck18) <= 1
   0 <= vY(demand11_truck21) <= 1
   0 <= vY(demand11_truck22) <= 1
   0 <= vY(demand11_truck26) <= 1
   0 <= vY(demand11_truck28) <= 1
   0 <= vY(demand11_truck44) <= 1
   0 <= vY(demand11_truck53) <= 1
   0 <= vY(demand22_truck10) <= 1
   0 <= vY(demand22_truck11) <= 1
   0 <= vY(demand22_truck16) <= 1
   0 <= vY(demand22_truck18) <= 1
   0 <= vY(demand22_truck21) <= 1
   0 <= vY(demand22_truck22) <= 1
   0 <= vY(demand22_truck28) <= 1
   0 <= vY(demand22_truck44) <= 1
   0 <= vY(demand22_truck53) <= 1
   0 <= vY(demand31_truck26) <= 1
   0 <= vY(demand31_truck28) <= 1
   0 <= vY(demand31_truck37) <= 1
   0 <= vY(demand31_truck38) <= 1
   0 <= vY(demand31_truck39) <= 1
   0 <= vY(demand31_truck40) <= 1
   0 <= vY(demand31_truck41) <= 1
   0 <= vY(demand31_truck51) <= 1
   0 <= vY(demand31_truck53) <= 1
   0 <= vY(demand32_truck26) <= 1
   0 <= vY(demand32_truck28) <= 1
   0 <= vY(demand32_truck37) <= 1
   0 <= vY(demand32_truck38) <= 1
   0 <= vY(demand32_truck39) <= 1
   0 <= vY(demand32_truck40) <= 1
   0 <= vY(demand32_truck41) <= 1
   0 <= vY(demand32_truck44) <= 1
   0 <= vY(demand32_truck51) <= 1
   0 <= vY(demand33_truck26) <= 1
   0 <= vY(demand33_truck28) <= 1
   0 <= vY(demand33_truck37) <= 1
   0 <= vY(demand33_truck38) <= 1
   0 <= vY(demand33_truck40) <= 1
   0 <= vY(demand33_truck41) <= 1
   0 <= vY(demand33_truck44) <= 1
   0 <= vY(demand4_truck10) <= 1
   0 <= vY(demand4_truck11) <= 1
   0 <= vY(demand4_truck16) <= 1
   0 <= vY(demand4_truck18) <= 1
   0 <= vY(demand4_truck21) <= 1
   0 <= vY(demand4_truck22) <= 1
   0 <= vY(demand41_truck26) <= 1
   0 <= vY(demand41_truck28) <= 1
   0 <= vY(demand41_truck37) <= 1
   0 <= vY(demand41_truck38) <= 1
   0 <= vY(demand41_truck39) <= 1
   0 <= vY(demand41_truck40) <= 1
   0 <= vY(demand41_truck41) <= 1
   0 <= vY(demand41_truck51) <= 1
   0 <= vY(demand43_truck26) <= 1
   0 <= vY(demand43_truck37) <= 1
   0 <= vY(demand43_truck38) <= 1
   0 <= vY(demand43_truck39) <= 1
   0 <= vY(demand43_truck40) <= 1
   0 <= vY(demand43_truck41) <= 1
   0 <= vY(demand43_truck51) <= 1
   0 <= vY(demand44_truck26) <= 1
   0 <= vY(demand44_truck28) <= 1
   0 <= vY(demand44_truck37) <= 1
   0 <= vY(demand44_truck38) <= 1
   0 <= vY(demand44_truck39) <= 1
   0 <= vY(demand44_truck40) <= 1
   0 <= vY(demand44_truck41) <= 1
   0 <= vY(demand44_truck51) <= 1
   0 <= vY(demand46_truck26) <= 1
   0 <= vY(demand46_truck28) <= 1
   0 <= vY(demand46_truck37) <= 1
   0 <= vY(demand46_truck38) <= 1
   0 <= vY(demand46_truck39) <= 1
   0 <= vY(demand46_truck40) <= 1
   0 <= vY(demand46_truck41) <= 1
   0 <= vY(demand46_truck51) <= 1
   0 <= vY(demand5_truck10) <= 1
   0 <= vY(demand5_truck11) <= 1
   0 <= vY(demand5_truck16) <= 1
   0 <= vY(demand5_truck18) <= 1
   0 <= vY(demand5_truck21) <= 1
   0 <= vY(demand5_truck22) <= 1
   0 <= vY(demand51_truck10) <= 1
   0 <= vY(demand51_truck11) <= 1
   0 <= vY(demand51_truck16) <= 1
   0 <= vY(demand51_truck18) <= 1
   0 <= vY(demand51_truck21) <= 1
   0 <= vY(demand51_truck22) <= 1
   0 <= vY(demand51_truck44) <= 1
   0 <= vY(demand51_truck53) <= 1
   0 <= vY(demand53_truck10) <= 1
   0 <= vY(demand53_truck11) <= 1
   0 <= vY(demand53_truck16) <= 1
   0 <= vY(demand53_truck18) <= 1
   0 <= vY(demand53_truck21) <= 1
   0 <= vY(demand53_truck22) <= 1
   0 <= vY(demand53_truck53) <= 1
   0 <= vY(demand7_truck10) <= 1
   0 <= vY(demand7_truck11) <= 1
   0 <= vY(demand7_truck18) <= 1
   0 <= vY(demand7_truck21) <= 1
   0 <= vY(demand7_truck22) <= 1
   0 <= vY(demand8_truck10) <= 1
   0 <= vY(demand8_truck11) <= 1
   0 <= vY(demand8_truck16) <= 1
   0 <= vY(demand8_truck18) <= 1
   0 <= vY(demand8_truck21) <= 1
   0 <= vY(demand8_truck22) <= 1
binary
  vX(truck10)
  vX(truck11)
  vX(truck16)
  vX(truck18)
  vX(truck21)
  vX(truck22)
  vX(truck26)
  vX(truck28)
  vX(truck37)
  vX(truck38)
  vX(truck39)
  vX(truck40)
  vX(truck41)
  vX(truck44)
  vX(truck51)
  vX(truck53)
  vY(demand11_truck10)
  vY(demand11_truck11)
  vY(demand11_truck16)
  vY(demand11_truck18)
  vY(demand11_truck21)
  vY(demand11_truck22)
  vY(demand11_truck26)
  vY(demand11_truck28)
  vY(demand11_truck44)
  vY(demand11_truck53)
  vY(demand22_truck10)
  vY(demand22_truck11)
  vY(demand22_truck16)
  vY(demand22_truck18)
  vY(demand22_truck21)
  vY(demand22_truck22)
  vY(demand22_truck28)
  vY(demand22_truck44)
  vY(demand22_truck53)
  vY(demand31_truck26)
  vY(demand31_truck28)
  vY(demand31_truck37)
  vY(demand31_truck38)
  vY(demand31_truck39)
  vY(demand31_truck40)
  vY(demand31_truck41)
  vY(demand31_truck51)
  vY(demand31_truck53)
  vY(demand32_truck26)
  vY(demand32_truck28)
  vY(demand32_truck37)
  vY(demand32_truck38)
  vY(demand32_truck39)
  vY(demand32_truck40)
  vY(demand32_truck41)
  vY(demand32_truck44)
  vY(demand32_truck51)
  vY(demand33_truck26)
  vY(demand33_truck28)
  vY(demand33_truck37)
  vY(demand33_truck38)
  vY(demand33_truck40)
  vY(demand33_truck41)
  vY(demand33_truck44)
  vY(demand4_truck10)
  vY(demand4_truck11)
  vY(demand4_truck16)
  vY(demand4_truck18)
  vY(demand4_truck21)
  vY(demand4_truck22)
  vY(demand41_truck26)
  vY(demand41_truck28)
  vY(demand41_truck37)
  vY(demand41_truck38)
  vY(demand41_truck39)
  vY(demand41_truck40)
  vY(demand41_truck41)
  vY(demand41_truck51)
  vY(demand43_truck26)
  vY(demand43_truck37)
  vY(demand43_truck38)
  vY(demand43_truck39)
  vY(demand43_truck40)
  vY(demand43_truck41)
  vY(demand43_truck51)
  vY(demand44_truck26)
  vY(demand44_truck28)
  vY(demand44_truck37)
  vY(demand44_truck38)
  vY(demand44_truck39)
  vY(demand44_truck40)
  vY(demand44_truck41)
  vY(demand44_truck51)
  vY(demand46_truck26)
  vY(demand46_truck28)
  vY(demand46_truck37)
  vY(demand46_truck38)
  vY(demand46_truck39)
  vY(demand46_truck40)
  vY(demand46_truck41)
  vY(demand46_truck51)
  vY(demand5_truck10)
  vY(demand5_truck11)
  vY(demand5_truck16)
  vY(demand5_truck18)
  vY(demand5_truck21)
  vY(demand5_truck22)
  vY(demand51_truck10)
  vY(demand51_truck11)
  vY(demand51_truck16)
  vY(demand51_truck18)
  vY(demand51_truck21)
  vY(demand51_truck22)
  vY(demand51_truck44)
  vY(demand51_truck53)
  vY(demand53_truck10)
  vY(demand53_truck11)
  vY(demand53_truck16)
  vY(demand53_truck18)
  vY(demand53_truck21)
  vY(demand53_truck22)
  vY(demand53_truck53)
  vY(demand7_truck10)
  vY(demand7_truck11)
  vY(demand7_truck18)
  vY(demand7_truck21)
  vY(demand7_truck22)
  vY(demand8_truck10)
  vY(demand8_truck11)
  vY(demand8_truck16)
  vY(demand8_truck18)
  vY(demand8_truck21)
  vY(demand8_truck22)
end
