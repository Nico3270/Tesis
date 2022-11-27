import numpy as np
from scipy.interpolate import lagrange, interp1d
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def interpolacion(x,y,z):
    y_interp = interp1d(x, y,fill_value="extrapolate")
    resultado = float(y_interp(z))
    return round(resultado,3)

#Tabla 4
tabla_4 = {"Suave":[1.0,0.965,0.931], "Media":[0.929,0.894,0.859],"Alta":[0.857,0.823,0.788]}

def pendi(pen):
    if pen <3:
        return "Suave"
    elif pen >= 3 and pen <7:
        return "Media"
    else:
        return "Alta"
def estado(esta):
    if esta == "Bueno":
        return 0
    elif esta == "Regular":
        return 1
    else:
        return 2
def factor_fpe(pend, est):
    val_1 = pendi(pend)
    val_2 = estado(est)
    factor = tabla_4.get(val_1)[val_2]
    return factor


cap_ideal = 3850
#Cálcuo factor fpe

#Cálculo factor fd
tabla5 = [50,60,70,80,90,100]
tabla_5x = [1.0,0.87,0.78,0.7,0.64,0.58]


#Cálculo de Nivel de servicio 
tabla_2 = {"Suave":[1.45], "Media":[1.32],"Alta":[1.2]}

tabla6 = [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0]
tabla6x = [1.0,0.99,0.98,0.95,0.92,0.87,0.82,0.75,0.68,0.59,0.55,0.50]


#Factor de ajuste Fo
tabla7 = {"Suave":[1.045], "Media":[1.286],"Alta":[1.543]}


#Factor de ajuste Fz
tabla8 = {"Centro":1.000, "Educativo":1.266, "Transporte":1.139, "Otros":1.063}


tabla9 = [2.0,1.9,1.8,1.7,1.6,1.5,1.4,1.3,1.2,1.1,1.0,0.9,0.8,0.7,0.6,0.5]
tabla9x =[0.987,0.978,0.962,0.940,0.912,0.879,0.839,0.793,0.741,0.683,0.619,0.550,0.474,0.392,0.304,0.210]
#Factor de ajuste far
def ancho_far(a_efectivo):
    if a_efectivo >= 2.1:
        return 1.0
    elif a_efectivo <= 0.4:
        return 0.110
    else:
        return interpolacion(tabla9, tabla9x, a_efectivo)


#Nivel de servicio

def nivel(espacio):
    if espacio > 5.3:
        return "A"
    elif espacio >3.5 and espacio <= 5.3:
        return "B"
    elif espacio > 2.4 and espacio <= 3.5:
        return "C"
    elif espacio > 1.5 and espacio <= 2.4:
        return "D"
    elif espacio >0.65 and espacio <= 1.5:
        return "E"
    else:
        return "F"

def capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp):
    p_mujeres = (100-p_hombres)/100
    p_hombres = p_hombres/100
    p_acompanadas = p_acompanadas/100
    p_paquetes = p_paquetes/100
    En_1 = ((p_ninos/100)*0.21*p_hombres) + (p_jovenes/100)*0*p_hombres + (p_adultos/100)*0.12*p_hombres + (p_mayores/100)*0.224*p_hombres
    En_2 = (p_ninos/100)*0.29*p_mujeres + (p_jovenes/100)*0.061*p_mujeres + (p_adultos/100)*0.197*p_mujeres + (p_mayores/100)*0.317*p_mujeres
    En_t = round(1 +En_1 + En_2,7)
    feg = round(1/En_t,3)
    fpe = factor_fpe(pendiente, estado)
    fd = interpolacion(tabla5, tabla_5x, d_sentido)
    fac = round(1/(1+(p_acompanadas*(1.078-1))),3)
    capacidad =int(cap_ideal * a_efectivo * feg * fpe * fd * fac)
    vfl = tabla_2.get(pendi(pendiente))[0]
    relacion_vc = round(((vol_peatonal/p_fhp)/capacidad),3)
    fu = interpolacion(tabla6,tabla6x, relacion_vc)
    Eo = tabla7.get(pendi(pendiente))[0]
    fo = round(1/(1+(p_paquetes*(Eo-1))),3)
    fz = tabla8.get(tipo_sector)
    far = ancho_far(a_efectivo)
    vel_media = round(vfl * fu * fo * fz * far,2)
    espacio_medio = round((vel_media * p_fhp * a_efectivo * 3600)/vol_peatonal,3)
    nivel_de_s = nivel(espacio_medio)
    return feg, fpe, fd, fac, capacidad, vfl, relacion_vc, fu, Eo, fo, fz, far, vel_media, espacio_medio, nivel_de_s


def sen_peatones_vol(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp,cap,ns,space,velocity):
    datos = np.arange(5,6000)
    espacio = []
    velocidad = []
    capacidad = []
    nivel = []
    
    for element in datos:
        data = capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, element,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        data = capacidad_peatones(tipo_sector, estado, element, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        data = capacidad_peatones(tipo_sector, estado, pendiente, element, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        res = capacidad_peatones(tipo_sector, element, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        res = capacidad_peatones(element, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        res = capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,element, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        res = capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, element, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, p_acompanadas, p_fhp)
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
        res = capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, p_paquetes, element, p_fhp)
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
        res = capacidad_peatones(tipo_sector, estado, pendiente, a_efectivo, vol_peatonal,d_sentido, p_hombres, p_ninos, p_jovenes, p_adultos, p_mayores, element, p_acompanadas, p_fhp) 
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