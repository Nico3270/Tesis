import multicarril as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
v3 = 0
datos = ["Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1]

def sensibilidad_volumen(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel,volumen,v_op,flujo,densidad):
    list = np.arange(1,4000,10)
    Nivel = []
    Densidad = []
    Velocidad = []
    Flujo = []
    #Analisis variando el volumen de tránsito, veh/h/sentido
    for element in list:
        v18 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
        Densidad.append(resultado[14])
        Velocidad.append(resultado[13])
        Flujo.append(resultado[12])
    N_servicio =  [list[(Nivel.index('B'))], list[(Nivel.index('C'))], list[(Nivel.index('D'))], list[(Nivel.index('E'))], list[(Nivel.index('F'))],
    Flujo[(Nivel.index('B'))], Flujo[(Nivel.index('C'))], Flujo[(Nivel.index('D'))], Flujo[(Nivel.index('E'))],Flujo[(Nivel.index('F'))], 
    Densidad[(Nivel.index('B'))], Densidad[(Nivel.index('C'))], Densidad[(Nivel.index('D'))], Densidad[(Nivel.index('E'))],Densidad[(Nivel.index('F'))],
    Velocidad[(Nivel.index('B'))], Velocidad[(Nivel.index('C'))], Velocidad[(Nivel.index('D'))], Velocidad[(Nivel.index('E'))],Velocidad[(Nivel.index('F'))]]
    #Gráfica Nivel de servicio vs Volumen de tránsito
    plt.style.use("seaborn-dark-palette")
    plt.plot(list, Nivel ,color="red", label='Nivel de servicio')
    plt.scatter(volumen,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, veh/h/sentido')
    plt.ylabel('Nivel de servicio')
    plt.savefig("static/assets/img/sensibilidad/plot.png")
    plt.close()
    #Gráfica Velocidad de operación vs Volumen de tránsito
    plt.plot(list, Velocidad ,color="red",label='Análisis de sensibilidad')
    plt.scatter(volumen,v_op, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, veh/h/sentido')
    plt.ylabel('Velocidad de operación (km/h)')
    plt.savefig("static/assets/img/sensibilidad/plot1.png")
    plt.close()
    #Gráfica Densidad del sector de análisis vs Volumen de tránsito
    plt.plot(list, Densidad ,color="red",label='Análisis de sensibilidad')
    plt.scatter(volumen,densidad, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, veh/h/sentido')
    plt.ylabel('Densidad del sector de análisis (veh/km/carril)')
    plt.savefig("static/assets/img/sensibilidad/plot2.png")
    plt.close()
    #Gráfica Flujo del sector de análisis vs Volumen de tránsito
    plt.plot(list, Flujo ,color="red",label='Análisis de sensibilidad')
    plt.scatter(volumen,flujo, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, (veh/h/sentido)')
    plt.ylabel('Flujo vehicular (veh/h/sentido)')
    plt.savefig("static/assets/img/sensibilidad/plot3.png")
    plt.close()
    return N_servicio

#print(sensibilidad_volumen("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1))

def sensibilidad_pendiente(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel,volumen,v_op,flujo,densidad):
    list = np.arange(0,9)
    pendiente = v4
    Nivel1 = []
    Densidad = []
    Velocidad = []
    Flujo = []
    #Analisis variando pendiente
    for element in list:
        v4 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel1.append(resultado[15])
        Densidad.append(resultado[14])
        Velocidad.append(resultado[13])
        Flujo.append(resultado[12])
    data = [Nivel1[0],Nivel1[1],Nivel1[2],Nivel1[3],Nivel1[4],Nivel1[5],Nivel1[6],Nivel1[7],Nivel1[8],
    Flujo[0],Flujo[1],Flujo[2],Flujo[3],Flujo[4],Flujo[5],Flujo[6],Flujo[7],Flujo[8],
    Velocidad[0],Velocidad[1],Velocidad[2],Velocidad[3],Velocidad[4],Velocidad[5],Velocidad[6],Velocidad[7],Velocidad[8],
    Densidad[0],Densidad[1],Densidad[2],Densidad[3],Densidad[4],Densidad[5],Densidad[6],Densidad[7],Densidad[8]]
    plt.plot(list, Nivel1 ,color="red", label="Análisis de sensibilidad")
    plt.scatter(pendiente,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto de la pendiente sobre el Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot4.png")
    plt.close()
    plt.plot(list, Flujo,color="red", label="Análisis de sensibilidad")
    plt.scatter(pendiente,flujo, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Flujo vehicular (veh/h/sentido)')
    plt.title('Efecto de la pendiente sobre el flujo vehicular')
    plt.savefig("static/assets/img/sensibilidad/plot5.png")
    plt.close()
    plt.plot(list, Velocidad,color="red", label="Análisis de sensibilidad")
    plt.scatter(pendiente,v_op, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Velocidad de operación (km/h)')
    plt.title('Efecto de la pendiente sobre la velocidad de operación')
    plt.savefig("static/assets/img/sensibilidad/plot6.png",bbox_inches='tight')
    plt.close()
    plt.plot(list, Densidad,color="red", label="Análisis de sensibilidad")
    plt.scatter(pendiente,densidad, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Densidad (veh/km/carril')
    plt.title('Efecto de la pendiente sobre la densidad')
    plt.savefig("static/assets/img/sensibilidad/plot7.png",bbox_inches='tight')
    plt.close()
    return data

#casa = sensibilidad_pendiente("Operacional", "Ascenso", "B1", True, False, True, 3.3, 1.5, 2.0, 1.0, 6, 4.0, 30, 2200, 1850, 0.9, 2, 1.0)
#print(casa)
#Función sensibilidad camiones
def sensibilidad_camiones(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel,volumen,v_op,flujo,densidad):
    list = np.arange(0, 50)
    camiones = v17
    Nivel1 = []
    Densidad = []
    nivel = str(nivel)
    Velocidad = []
    Flujo = []
    for element in list:
        v17 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel1.append(resultado[15])
        Densidad.append(resultado[14])
        Velocidad.append(resultado[13])
        Flujo.append(resultado[12])
    plt.plot(list, Nivel1 ,color="red",label="Análisis de sensibilidad")
    plt.scatter(camiones,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Porcentaje camiones (%)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto del porcentaje de camiones sobre el Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot8.png")
    plt.close()
    plt.plot(list, Flujo ,color="red", label="Análisis de sensibilidad")
    plt.scatter(camiones,flujo, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Porcentaje camiones (%)')
    plt.ylabel('Flujo vehicular (veh/h/sentido)')
    plt.title('Efecto del porcentaje de camiones sobre el Flujo vehicular')
    plt.savefig("static/assets/img/sensibilidad/plot9.png")
    plt.close()
    plt.plot(list, Velocidad ,color="red", label = "Análiis de sensibilidad")
    plt.scatter(camiones,v_op, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Porcentaje camiones (%)')
    plt.ylabel('Velocidad de operación (km/h)')
    plt.title('Efecto del porcentaje de camiones sobre la velocidad de operación')
    plt.savefig("static/assets/img/sensibilidad/plot10.png")
    plt.close()
    plt.plot(list, Densidad ,color="red", label="Análisis de sensibilidad")
    plt.scatter(camiones,densidad, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Porcentaje camiones (%)')
    plt.ylabel('Densidad (veh/km/carril)')
    plt.title('Efecto del porcentaje de camiones sobre la Densidad')
    plt.savefig("static/assets/img/sensibilidad/plot11.png")
    plt.close()
   
#Función sensibilidad carriles
def sensiblidad_carriles(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel):
    list = np.arange(2,8)
    Nivel = []
    carril = v6
    for element in list:
        v6 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red", label="Análisis de sensibilidad")
    plt.scatter(carril,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Número de carriles')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto del número de carriles sobre el Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot12.png")
    plt.close()
    return Nivel

#Función sensibilidad a_carril
def sensibilidad_ancho_carril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel):
    list = ['3', '3.3', '3.5']
    Nivel = []
    ancho = str(v7)
    for element in list:
        v7 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red", label="Análisis de sensibilidad")
    plt.scatter(ancho,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Ancho de carril (metros)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto del ancho de carril sobre el Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot13.png")
    plt.close()
    return Nivel

#Función sensibilidad ancho del separador
def sensibilidad_ancho_separador(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel):
    list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
    Nivel = []
    separador = v9
    for element in list:
        v9 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red", label="Análisis de sensibilidad")
    plt.scatter(separador,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Ancho de separador (metros)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto del ancho del separador sobre el Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot14.png")
    plt.close()
    return Nivel
#sensibilidad_ancho_separador("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1)
#Función sensibilidad ancho promedio de bermas

def sensibilidad_ancho_bermas(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,nivel):
    list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
    Nivel = []
    berma = (v10+v11)/2
    for element in list:
        v10 = element
        v11 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red", label="Análisis de sensibilidad")
    plt.scatter(berma,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Ancho promedio de bermas (metros)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto del ancho promedio de bermas sobre el Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot15.png")
    plt.close()
    return Nivel

#sensibilidad_ancho_bermas("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1)

#Función para determinar sensibilidad por número de accesos
def sensibilidad_n_accesos(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15, nivel):
    list = np.arange(0,20)
    Nivel = []
    accesos = v12
    for element in list:
        v12 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red", label="Análisis de sensibilidad")
    plt.scatter(accesos,nivel, label="Resultado obtenido")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.xlabel('Densidad de accesos ')
    plt.ylabel('Nivel de Servicio')
    plt.title('Efecto de la densidad de accesos sobre Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot16.png")
    plt.close()
    return Nivel

#sensibilidad_n_accesos("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1)
def sensibilidad_bool(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    sep_1 = mp.calc_multicarril(v1,v2,v3,True,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
    sep_0 = mp.calc_multicarril(v1,v2,v3,False,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
    acc_1= mp.calc_multicarril(v1,v2,v3,v8,True,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
    acc_0 = mp.calc_multicarril(v1,v2,v3,v8,False,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
    pea_1= mp.calc_multicarril(v1,v2,v3,v8,v13,True,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
    pea_0 = mp.calc_multicarril(v1,v2,v3,v8,v13,False,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
    con_1 = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,1)
    con_0 = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,0.90)
    data = [sep_1[12], sep_1[13], sep_1[14], sep_1[15], sep_0[12], sep_0[13], sep_0[14], sep_0[15],
    acc_1[12], acc_1[13], acc_1[14], acc_1[15], acc_0[12], acc_0[13], acc_0[14], acc_0[15],
    pea_1[12], pea_1[13], pea_1[14], pea_1[15], pea_0[12], pea_0[13], pea_0[14], pea_0[15],
    con_1[12], con_1[13], con_1[13], con_1[14], con_0[12], con_0[13], con_0[13], con_0[14],]
    return data
