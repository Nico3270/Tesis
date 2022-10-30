from main import resultado
import multicarril as mp
import numpy as np
import matplotlib.pyplot as plt
v3 = 0
datos = ["Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1]

def sensibilidad_volumen(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = np.arange(1,3000)
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
    Velocidad[0], Velocidad[500],Velocidad[1000],Velocidad[1500],Velocidad[2000] ,Velocidad[2500],Velocidad[2998],
    Velocidad[(Nivel.index('B'))], Velocidad[(Nivel.index('C'))], Velocidad[(Nivel.index('D'))], Velocidad[(Nivel.index('E'))],Velocidad[(Nivel.index('F'))],
    Densidad[0], Densidad[500],Densidad[1000],Densidad[1500],Densidad[2000] ,Densidad[2500],Densidad[2998],
    Densidad[(Nivel.index('B'))], Densidad[(Nivel.index('C'))], Densidad[(Nivel.index('D'))], Densidad[(Nivel.index('E'))],Densidad[(Nivel.index('F'))],
    Flujo[0], Flujo[500],Flujo[1000],Flujo[1500],Flujo[2000] ,Flujo[2500],Flujo[2998],
    Flujo[(Nivel.index('B'))], Flujo[(Nivel.index('C'))], Flujo[(Nivel.index('D'))], Flujo[(Nivel.index('E'))],Flujo[(Nivel.index('F'))],  ]
    #Gráfica Nivel de servicio vs Volumen de tránsito
    plt.style.use("seaborn-dark-palette")
    plt.plot(list, Nivel ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, veh/h/sentido')
    plt.ylabel('Nivel de servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot.png")
    plt.close()
    #Gráfica Velocidad de operación vs Volumen de tránsito
    plt.plot(list, Velocidad ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, veh/h/sentido')
    plt.ylabel('Velocidad de operación (km/h)')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot3.png")
    plt.close()
    #Gráfica Densidad del sector de análisis vs Volumen de tránsito
    plt.plot(list, Densidad ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, veh/h/sentido')
    plt.ylabel('Densidad del sector de análisis (veh/km/carril)')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot4.png")
    plt.close()
    plt.plot(list, Flujo ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Volumen de tránsito, (veh/h/sentido)')
    plt.ylabel('Flujo vehicular (veh/h/sentido)')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot6.png")
    plt.close()
    return N_servicio

#print(sensibilidad_volumen("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1))

def sensibilidad_pendiente(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = np.arange(0,9)
    Nivel1 = []
    Densidad = []
    Velocidad = []
    Flujo = []
    #Analisis variando pendiente
    for element in list:
        v4 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel1.append(resultado[15])
    plt.plot(list, Nivel1 ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot8.png")
    plt.close()
    return Nivel1

#Función sensibilidad camiones
def sensibilidad_camiones(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = np.arange(0, 50)
    Nivel1 = []
    for element in list:
        v17 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel1.append(resultado[15])
    plt.plot(list, Nivel1 ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Porcentaje camiones (%)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot9.png")
    plt.close()
    return Nivel1

#Función sensibilidad carriles
def sensiblidad_carriles(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = np.arange(2,8)
    Nivel = []
    for element in list:
        v6 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Número de carriles')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot10.png")
    plt.close()
    return Nivel

#Función sensibilidad a_carril
def sensibilidad_ancho_carril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = ['3', '3.3', '3.5']
    Nivel = []
    for element in list:
        v7 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Ancho de carril (metros)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot11.png")
    plt.close()
    return Nivel

#Función sensibilidad ancho del separador
def sensibilidad_ancho_separador(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
    Nivel = []
    for element in list:
        v9 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Ancho de separador (metros)')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot12.png")
    plt.close()
    return Nivel
#sensibilidad_ancho_separador("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1)
#Función sensibilidad ancho promedio de bermas

def sensibilidad_ancho_bermas(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]
    Nivel = []
    for element in list:
        v10 = element
        v11 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Ancho promedio de bermas (metros')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot13.png")
    plt.close()
    return Nivel

#sensibilidad_ancho_bermas("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1)

#Función para determinar sensibilidad por número de accesos
def sensibilidad_n_accesos(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15):
    list = np.arange(0,20)
    Nivel = []
    for element in list:
        v12 = element
        resultado = mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        Nivel.append(resultado[15])
    plt.plot(list, Nivel ,color="red")
    plt.legend(['Análisis de sensibilidad'])
    plt.grid(True)
    plt.xlabel('Densidad de accesos ')
    plt.ylabel('Nivel de Servicio')
    plt.title('Variación del Nivel de Servicio')
    plt.savefig("static/assets/img/sensibilidad/plot14.png")
    plt.close()
    return Nivel
sensibilidad_n_accesos("Operacional", "Generico", "B1", True, False, True, '3.3', 1.5, 2.0, 1.0, 6, 4, 30, 2200,1850,0.90,2,1)