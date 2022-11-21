import main as mn
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# ns = []
# vol = np.arange(0,1000)

# for element in vol:
#     data = mn.Capacidad_Ns(3.2,1.3,7.4,2.6,55,80,50,10,40,element)
#     ns.append(data[17])
# #Gráfica Nivel de servicio vs Volumen de tránsito
# plt.style.use("seaborn-dark-palette")
# plt.plot(vol, ns ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Volumen de tránsito (veh/h/sentido)')
# plt.ylabel('Nivel de servicio')
# plt.savefig("static/assets/img/sensibilidad/multi_ns.png")
# plt.close()

# #Gráfica Pendiente vs Nivel de servicio
# ns_pen = []
# cap_pen = []
# pendiente= np.arange(0,12,0.2)
# for element in pendiente:
#      data = mn.Capacidad_Ns(3.2,1.3,element,2.9,55,80,50,10,40,250)
#      ns_pen.append(data[17])
#      cap_pen.append(data[5])


# plt.style.use("seaborn-dark-palette")
# plt.plot(pendiente, ns_pen ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Pendiente (%)')
# plt.ylabel('Nivel de servicio')
# plt.savefig("static/assets/img/sensibilidad/pen_ns.png")
# plt.close()


# #Gráfica Pendiente vs capacidad
# plt.style.use("seaborn-dark-palette")
# plt.plot(pendiente, cap_pen ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Pendiente (%)')
# plt.ylabel('Capacidad (Veh/h/sentido)')
# plt.savefig("static/assets/img/sensibilidad/cap_ns.png")
# plt.close()

#Gráfica longitud del tramo vs NS
# longitud = np.arange(0,4.5,0.1)
# ns_lon = []
# cap_lon = []
# for element in longitud:
#     data = mn.Capacidad_Ns(3.2,1.3,7,element,55,80,50,10,40,250)
#     ns_lon.append(data[17])
#     cap_lon.append(data[5])

# plt.style.use("seaborn-dark-palette")
# plt.plot(longitud, cap_lon ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Longitud (km)')
# plt.ylabel('Capacidad (Veh/h/sentido)')
# plt.savefig("static/assets/img/sensibilidad/cap_lon.png")
# plt.close()

# plt.style.use("seaborn-dark-palette")
# plt.plot(longitud, ns_lon ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Longitud (km)')
# plt.ylabel('Nivel de servicio')
# plt.savefig("static/assets/img/sensibilidad/ns_lon.png")
# plt.close()


#Efecto del ancho de berma
# berma = np.arange(0,1.8,0.1)
# ns_berma = []
# cap_berma = []
# for element in berma:
#     data = mn.Capacidad_Ns(3.2,element,7,2.9,55,80,50,10,40,250)
#     ns_berma.append(data[17])
#     cap_berma.append(data[5])

# plt.style.use("seaborn-dark-palette")
# plt.plot(berma, ns_berma ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Berma')
# plt.ylabel('Nivel de servicio')
# plt.savefig("static/assets/img/sensibilidad/ns_berma.png")
# plt.close()

# plt.style.use("seaborn-dark-palette")
# plt.plot(berma, cap_berma ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Berma')
# plt.ylabel('Capacidad')
# plt.savefig("static/assets/img/sensibilidad/cap_berma.png")
# plt.close()

# #Efecto del ancho de carril
# carril = np.arange(2.7,3.7,0.1)
# ns_carril = []
# cap_carril = []
# for element in carril:
#     data = mn.Capacidad_Ns(element,1.2,7,2.9,55,80,50,10,40,250)
#     ns_carril.append(data[17])
#     cap_carril.append(data[5])

# plt.style.use("seaborn-dark-palette")
# plt.plot(carril, cap_carril ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Carril')
# plt.ylabel('Capacidad')
# plt.savefig("static/assets/img/sensibilidad/cap_carril.png")
# plt.close()

# plt.style.use("seaborn-dark-palette")
# plt.plot(carril, ns_carril ,color="red", label='Nivel de servicio')
# plt.legend(loc="lower right")
# plt.grid(True)
# plt.xlabel('Carril')
# plt.ylabel('Nivel de servicio')
# plt.savefig("static/assets/img/sensibilidad/ns_carril.png")
# plt.close()

#Efecto porcentaje camiones

camiones = np.arange(0,50,2)
ns_camion = []
cap_camion = []
for element in camiones:
    data = mn.Capacidad_Ns(3,1.2,7,2.9,55,80,50,10,element,250)
    ns_camion.append(data[17])
    cap_camion.append(data[5])

plt.style.use("seaborn-dark-palette")
plt.plot(camiones, ns_camion ,color="red", label='Nivel de servicio')
plt.legend(loc="lower right")
plt.grid(True)
plt.xlabel('Porcentaje camiones')
plt.ylabel('Nivel de servicio')
plt.savefig("static/assets/img/sensibilidad/ns_camiones.png")
plt.close()

plt.style.use("seaborn-dark-palette")
plt.plot(camiones, cap_camion ,color="red", label='Nivel de servicio')
plt.legend(loc="lower right")
plt.grid(True)
plt.xlabel('Camiones')
plt.ylabel('Capacidad')
plt.savefig("static/assets/img/sensibilidad/cap_camion.png")
plt.close()