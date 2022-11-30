import multicarril as mp
import sensibilidad_2_carriles as sen2
import numpy as np
import capacidad_NS as cap
import main as mn


datos = mn.Capacidad_Ns(3.65,1.30,7.5,1.30,55,82,50,10,40,763)
res = cap.inter_compuesta_mon_esc(47.73,cap.tabla_9x,cap.montanoso,40,1.30)
#sen2.sensiblidad_longitud(3.65,1.30,7.5,1.30,55,82,50,10,40,763,2000,"D")
 
datos_2 = cap.inter_compuesta3(cap.tabla_3x, cap.tabla_3,2,3.25)


datos_3 = cap.inter_compuesta_plan_ond(60.40,cap.tabla_9x, cap.ondulado, 40, 3.78)


datos3 = np.arange(0,1000,2)
resultados = []
for element in datos3:
    var = cap.interpolacionp(cap.tabla_7x,cap.tabla_7,element/2070)
    resultados.append(var)


