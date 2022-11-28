import multicarril as mp
import sensibilidad_2_carriles as sen2
import numpy as np
import capacidad_NS as cap
import main as mn


datos = mn.Capacidad_Ns(3.65,1.30,7.5,1.30,55,82,50,10,40,763)
#res = cap.inter_compuesta_mon_esc(47.73,cap.tabla_9x,cap.montanoso,40,1.30)
sen2.sensiblidad_longitud(3.65,1.30,7.5,1.30,55,82,50,10,40,763,2000,"D")
 