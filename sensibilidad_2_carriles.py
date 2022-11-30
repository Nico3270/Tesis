import main as mn
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#Función para gráficar las variaciones en capacidad y nivel de servicio, por cambios en volumen
def sensibilidad_volumen(a_carril, a_berma, p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen,nivel,capa):
    ns = []
    vol = np.arange(0,capa+100,5)
    for element in vol:
        data = mn.Capacidad_Ns(a_carril, a_berma, p_promedio, l_tramo, d_sentido, p_no_rebase, p_autos, p_buses, p_camiones, element)
        ns.append(data[17])
    #Gráfica Nivel de servicio vs Volumen de tránsito
    plt.style.use("seaborn-dark-palette")
    plt.plot(vol, ns ,color="red", label='Nivel de servicio')
    plt.scatter(volumen,nivel, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Volumen de tránsito (veh/h/sentido)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_2carriles_volumen.png")
    plt.close()

#Función para gráficar las variaciones en capacidad y nivel de servicio, por cambios en pendiente
def sensibilidad_pendiente(a_carril, a_berma, p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen,cap,ns):
    #Gráfica Pendiente vs Nivel de servicio
    ns_pen = []
    cap_pen = []
    pendiente= np.arange(0,12,0.5)
    for element in pendiente:
        data = mn.Capacidad_Ns(a_carril,a_berma,element,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen)
        ns_pen.append(data[17])
        cap_pen.append(data[5])
    #Gráfica Pendiente vs N de S
    plt.style.use("seaborn-dark-palette")
    plt.plot(pendiente, ns_pen ,color="red", label='Nivel de servicio')
    plt.scatter(p_promedio,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_2carriles_pendiente.png")
    plt.close()

    #Gráfica Pendiente vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(pendiente, cap_pen ,color="red", label='Nivel de servicio')
    plt.scatter(p_promedio,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Capacidad (Veh/h/sentido)')
    plt.savefig("static/assets/img/sensibilidad/cap_2carriles_pendiente.png")
    plt.close()

#Función para gráficar las variaciones en capacidad y nivel de servicio, por cambios en longitud del tramo:

def sensiblidad_longitud(a_carril, a_berma, p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen,cap, ns):
    #Datos de entrada
    longitud = np.arange(0.51,4.5,0.1)
    ns_lon = []
    cap_lon = []
    for element in longitud:
        data = mn.Capacidad_Ns(a_carril,a_berma,p_promedio,element,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen)
        ns_lon.append(data[17])
        cap_lon.append(data[5])
    #Gráfica longitud del tramo vs Capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(longitud, cap_lon ,color="red", label='Nivel de servicio')
    plt.scatter(l_tramo,cap, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Longitud (km)')
    plt.ylabel('Capacidad (Veh/h/sentido)')
    plt.savefig("static/assets/img/sensibilidad/cap_2carriles_longitud.png")
    plt.close()
    #Gráfica longitud del tramo vs Ns
    plt.style.use("seaborn-dark-palette")
    plt.plot(longitud, ns_lon ,color="red", label='Nivel de servicio')
    plt.scatter(l_tramo,ns, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Longitud (km)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_2carriles_longitud.png")
    plt.close()

#Función para gráficar las variaciones en capacidad y nivel de servicio, por cambios en el ancho de la berma:
def sensibilidad_berma(a_carril, a_berma, p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen, ns, cap):
    berma = np.arange(0,3,0.2)
    ns_berma = []
    cap_berma = []
    for element in berma:
        data = mn.Capacidad_Ns(a_carril,element,p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen)
        ns_berma.append(data[17])
        cap_berma.append(data[5])
    #Gráfica Ancho de berma vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(berma, ns_berma ,color="red", label='Nivel de servicio')
    plt.scatter(a_berma,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Ancho de berma (m)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_2carriles_berma.png")
    plt.close()
    #Gráfica Ancho de berma vs Capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(berma, cap_berma ,color="red", label='Nivel de servicio')
    plt.scatter(a_berma,cap, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Ancho de Berma')
    plt.ylabel('Capacidad (Veh/h)')
    plt.savefig("static/assets/img/sensibilidad/cap_2carriles_berma.png")
    plt.close()


#Función para gráficar las variaciones en capacidad y nivel de servicio, por cambios en el ancho del carril:
def sensibilidad_carril(a_carril, a_berma, p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen, cap, ns):
    carril = np.arange(2.7,3.8,0.1)
    ns_carril = []
    cap_carril = []
    for element in carril:
        data = mn.Capacidad_Ns(element,a_berma, p_promedio, l_tramo, d_sentido, p_no_rebase, p_autos, p_buses,p_camiones, volumen)
        ns_carril.append(data[17])
        cap_carril.append(data[5])
    
    #Gráfica Ancho del carril vs Capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(carril, cap_carril ,color="red", label='Nivel de servicio')
    plt.scatter(a_carril,cap, label="Resultado obtenido")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de carril (metros)')
    plt.ylabel('Capacidad (Veh/h)')
    plt.savefig("static/assets/img/sensibilidad/cap_2carriles_carril.png")
    plt.close()
    #Gráfica Ancho del carril vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(carril, ns_carril ,color="red", label='Nivel de servicio')
    plt.scatter(a_carril,ns, label="Resultado obtenido")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de carril (metros)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_2carriles_carril.png")
    plt.close()

#Función para gráficar las variaciones en capacidad y nivel de servicio, por cambios en el porcentaje de camiones:
def sensibilidad_camiones(a_carril, a_berma, p_promedio,l_tramo,d_sentido,p_no_rebase,p_autos,p_buses,p_camiones,volumen,ns,cap):
    iterar = 60-p_buses
    camiones = np.arange(0,iterar,1)
    ns_camion = []
    cap_camion = []
    for element in camiones:
        data = mn.Capacidad_Ns(a_carril, a_berma, p_promedio,l_tramo, d_sentido, p_no_rebase, p_autos,p_buses,element, volumen)
        ns_camion.append(data[17])
        cap_camion.append(data[5])
    #Gráfica % Camiones vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(camiones, ns_camion ,color="red", label='Nivel de servicio')
    plt.scatter(p_camiones,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje camiones (%)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_2carriles_camiones.png")
    plt.close()
    #Gráfica % Camiones vs Capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(camiones, cap_camion ,color="red", label='Nivel de servicio')
    plt.scatter(p_camiones,cap, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Porcentaje de camiones')
    plt.ylabel('Capacidad (Veh/h)')
    plt.savefig("static/assets/img/sensibilidad/cap_2carriles_camiones.png")
    plt.close()