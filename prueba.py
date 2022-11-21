import multicarril as mp
import capacidad_NS as cap
import numpy as np

pen1 = np.arange(0,5.9,0.5)
pen2 = np.arange(6.3,8.9,0.5)
pen3 = np.arange(9.2,12,0.5)

pendiente =[]
for element in pen1:
    pendiente.append(element)
for element in pen2:
    pendiente.append(element)
for element in pen3:
    pendiente.append(element)
print(pendiente)