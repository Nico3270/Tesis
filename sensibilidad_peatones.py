import numpy as np
import matplotlib
import peatones as peato
matplotlib.use('Agg')
from matplotlib import pyplot as plt

#Análisis de sensibilidad por aumento de peatones

def sen_peatones_vol(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp,cap,ns,space,velocity):
    datos = np.arange(5,6000)
    espacio = []
    velocidad = []
    capacidad = []
    nivel = []
    
    for element in datos:
        data = peato.capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, element,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        espacio.append(data[13])
        velocidad.append(data[12])
        nivel.append(data[14])
        capacidad.append(data[4])
    #Gráfica peatones vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(vol_peatonal,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Volumen peatonal (pea/hora/vía)')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_volumen.png")
    plt.close()
    #Gráfica peatones vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(vol_peatonal,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Volumen peatonal (pea/hora/vía)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_volumen.png")
    plt.close()
    #Gráfica peatones vs espacio medio peatonal
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, espacio ,color="red", label='Nivel de servicio')
    plt.scatter(vol_peatonal,space, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Volumen peatonal (pea/hora/vía)')
    plt.ylabel(r'$Espacio medio peatonal (m^{2}/p)')
    plt.savefig("static/assets/img/sensibilidad/espacio_peatones_volumen.png")
    plt.close()
    #Gráfica peatones vs velocidad media
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, velocidad ,color="red", label='Nivel de servicio')
    plt.scatter(vol_peatonal,velocity, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Volumen peatonal (pea/hora/vía)')
    plt.ylabel('Velocidad media de caminata (m/s)')
    plt.savefig("static/assets/img/sensibilidad/velocidad_peatones_volumen.png")
    plt.close()
#Análisis de sensibilidad por aumento de pendiente
def sen_peatones_pen(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp,cap,ns,space,velocity):
    datos = np.arange(0,15,0.5)
    espacio = []
    velocidad = []
    capacidad = []
    nivel = []
    for element in datos:
        data = peato.capacidad_peatones(tipo_sector, estado, element, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        espacio.append(data[13])
        velocidad.append(data[12])
        nivel.append(data[14])
        capacidad.append(data[4])
    #Gráfica peatones vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(pendiente,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_pendiente.png")
    plt.close()
    #Gráfica peatones vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(pendiente,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_pendiente.png")
    plt.close()
    #Gráfica peatones vs espacio medio peatonal
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, espacio ,color="red", label='Nivel de servicio')
    plt.scatter(pendiente,space, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel(r'$Espacio medio peatonal (m^{2}/p)$')
    plt.savefig("static/assets/img/sensibilidad/espacio_peatones_pendiente.png")
    plt.close()
    #Gráfica peatones vs velocidad media
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, velocidad ,color="red", label='Nivel de servicio')
    plt.scatter(pendiente,velocity, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Velocidad media de caminata (m/s)')
    plt.savefig("static/assets/img/sensibilidad/velocidad_peatones_pendiente.png")
    plt.close()
#Análisis de sensibilidad por aumento de ancho efectivo
def sen_peatones_ancho(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp,cap,ns,space,velocity):     
    datos = np.arange(0.1,3,0.1)
    espacio = []
    velocidad = []
    capacidad = []
    nivel = []
    for element in datos:
        data = peato.capacidad_peatones(tipo_sector, estado, pendiente, element, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        espacio.append(data[13])
        velocidad.append(data[12])
        nivel.append(data[14])
        capacidad.append(data[4])
    #Gráfica peatones vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(a_efectivo,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Ancho efectivo (m)')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_ancho.png")
    plt.close()
    #Gráfica peatones vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(a_efectivo,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Ancho efectivo (m)')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_ancho.png")
    plt.close()
    #Gráfica peatones vs espacio medio peatonal
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, espacio ,color="red", label='Nivel de servicio')
    plt.scatter(a_efectivo,space, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Ancho efectivo (m)')
    plt.ylabel(r'$Espacio medio peatonal (m^{2}/p)$')
    plt.savefig("static/assets/img/sensibilidad/espacio_peatones_ancho.png")
    plt.close()
    #Gráfica peatones vs velocidad media
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, velocidad ,color="red", label='Nivel de servicio')
    plt.scatter(a_efectivo,velocity, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Ancho efectivo (m)')
    plt.ylabel('Velocidad media de caminata (m/s)')
    plt.savefig("static/assets/img/sensibilidad/velocidad_peatones_ancho.png")
    plt.close()
#Análisis de sensibilidad por cambios en estado de la superficie
def sen_peatones_estado(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp, cap,ns):
    datos = ["Bueno","Regular","Malo"]
    capacidad = []
    nivel = []
    for element in datos:
        res = peato.capacidad_peatones(tipo_sector, element, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        capacidad.append(res[4])
        nivel.append(res[14])
    #Gráfica estado vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(estado,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Estado de superficie de la infraestructura peatonal')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_estado.png")
    plt.close()
    #Gráfica estado vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(estado,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Estado de superficie de la infraestructura peatonal')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_estado.png")
    plt.close()
    print(capacidad)
#Análisis de sensibilidad por cambios en estado de la superficie  
def sen_peatones_sector(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp, cap,ns):
    datos = ["Centro", "Educativo", "Transporte", "Otros"] 
    capacidad = []
    nivel = []
    for element in datos:
        res = peato.capacidad_peatones(element, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        capacidad .append(res[4])
        nivel.append(res[14])
    #Gráfica estado vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(tipo_sector,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Tipo de sector')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_sector.png")
    plt.close()
    #Gráfica estado vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(tipo_sector,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Tipo de sector')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_sector.png")
    plt.close()
#Anális de sensibilidad por cambios en distribución por sentidos
def sen_peatones_sentido(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp, cap,ns):
    datos = np.arange(50,100)
    capacidad = []
    nivel = []
    for element in datos:
        res = peato.capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,element, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        capacidad.append(res[4])
        nivel.append(res[14])
    #Gráfica estado vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(d_sentido,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Distribución por sentidos')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_sentido.png")
    plt.close()
    #Gráfica estado vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(d_sentido,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Distribución por sentidos')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_sentido.png")
    plt.close()
#Análisis de sensibilidad por cambios en porcentaje de hombres
def sen_peatones_hombres(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp, cap,ns):
    datos = np.arange(0,100)
    capacidad = []
    nivel = []
    for element in datos:
        res = peato.capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, element, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
        capacidad.append(res[4])
        nivel.append(res[14])
    #Gráfica %Hombres vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(p_hombres,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje de hombres')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_hombres.png")
    plt.close()
    #Gráfica %Hombres vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(p_hombres,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje de hombres')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_hombres.png")
    plt.close()
#Análisis de sensibilidad por personas acompañadas
def sen_peatones_acompanadas(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp, cap,ns):
    datos = np.arange(0,100)
    capacidad = []
    nivel = []
    for element in datos:
        res = peato.capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, element, p_fhp)
        capacidad.append(res[4])
        nivel.append(res[14])
    #Gráfica %acomapanados vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(p_acompanadas,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje de personas acompañadas')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_acompanadas.png")
    plt.close()
    #Gráfica %Hombres vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(p_acompanadas,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje de personas acompañadas')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_acompanadas.png")
    plt.close()
#Análisis de sensibilidad por personas con paquetes
def sen_peatones_paquetes(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp, cap,ns):
    datos = np.arange(100)
    capacidad = []
    nivel = []
    for element in datos:
        res = peato.capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, element, p_acompanadas, p_fhp) 
        capacidad.append(res[4])
        nivel.append(res[14])
    #Gráfica %paquetes vs capacidad
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, capacidad ,color="red", label='Capacidad')
    plt.scatter(p_paquetes,cap, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje de personas con paquetes')
    plt.ylabel('Capacidad (pea/hora/infraestructura)')
    plt.savefig("static/assets/img/sensibilidad/cap_peatones_data_paquetes.png")
    plt.close()
    #Gráfica %Hombres vs Nivel de Servicio
    plt.style.use("seaborn-dark-palette")
    plt.plot(datos, nivel ,color="red", label='Nivel de servicio')
    plt.scatter(p_paquetes,ns, label="Resultado obtenido")
    plt.grid(True)
    plt.xlabel('Porcentaje de personas con paquetes')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/ns_peatones_paquetes.png")
    plt.close() 
#sen_peatones_paquetes("Centro", "Bueno",2,2,2400,50,45,15,30,45,10,30,60,0.75,6404,"C")