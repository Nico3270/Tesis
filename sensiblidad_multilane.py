
import multicarril as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
v3 = 0
import HCM_Multilane as hcmln



def sensibilidadCarriles(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, 
volumenResultado):
    lista = np.arange(3,8)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    for element in lista:
        data = hcmln.hcmMultilaneFunction(element, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(numeroCarriles, capacidadResultado,color="red" )
    plt.scatter(numeroCarriles, volumenResultado, color="teal"  )
    plt.axvline(numeroCarriles,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Carriles")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/carril_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(numeroCarriles, nivelResultado, color="red" )
    plt.axvline(numeroCarriles,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Carriles")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/carril_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.scatter(numeroCarriles, densidadResultado, color="red" )
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(numeroCarriles, velocidadResultado, color="darkcyan" )
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axvline(numeroCarriles,color="k", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Carriles")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/carril_densidad.png")
    plt.close()

def sensibilidadAnchoCarril(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(9.2,11.5,0.1)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, element,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(anchoCarril, capacidadResultado,color="red" )
    plt.scatter(anchoCarril, volumenResultado, color="teal"  )
    plt.axvline(anchoCarril,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Ancho de carril (ft)")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/anchoCarril_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(anchoCarril, nivelResultado, color="red" )
    plt.axvline(anchoCarril,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Ancho de carril (ft)")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/anchoCarril_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(anchoCarril, densidadResultado, color="red" )
    plt.scatter(anchoCarril, velocidadResultado, color="darkcyan" )
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axvline(anchoCarril,color="k", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Ancho de carril (ft)")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/anchoCarril_densidad.png")
    plt.close()

def sensibilidadAnchoBermas(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(0,15,0.1)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    anchoBermas = anchoBermaDerecha + anchoBermaIzquierda
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, anchoCarril,tipoSeparacion, 0, element, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(anchoBermas, capacidadResultado,color="red" )
    plt.scatter(anchoBermas, volumenResultado, color="teal"  )
    plt.axvline(anchoBermas,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Ancho de bermas  (ft)")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/anchoBermas_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(anchoBermas, nivelResultado, color="red" )
    plt.axvline(anchoBermas,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Ancho de bermas (ft)")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/anchoBermas_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(anchoBermas, densidadResultado, color="red" )
    plt.scatter(anchoBermas, velocidadResultado, color="darkcyan" )
    plt.axvline(anchoBermas,color="k", ls="dotted")
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Ancho de bermas (ft)")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/anchoBermas_densidad.png")
    plt.close()

def sensibilidadLongitud(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(0.5,5,0.1)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, element,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(longitudTramo, capacidadResultado,color="red" )
    plt.scatter(longitudTramo, volumenResultado, color="teal"  )
    plt.axvline(longitudTramo,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Longitud del tramo (mi)")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/Longitud_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(longitudTramo, nivelResultado, color="red" )
    plt.axvline(longitudTramo,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Longitud del tramo (mi)")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/Longitud_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(longitudTramo, densidadResultado, color="red" )
    plt.scatter(longitudTramo, velocidadResultado, color="darkcyan" )
    plt.axvline(longitudTramo,color="k", ls="dotted")
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Longitud del tramo (mi)")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/Longitud_densidad.png")
    plt.close()

def sensibilidadPendiente(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(0,12,0.1)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    anchoBermas = anchoBermaDerecha + anchoBermaIzquierda
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,"Pendiente específica", 
element, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(pendienteTramo, capacidadResultado,color="red" )
    plt.scatter(pendienteTramo, volumenResultado, color="teal"  )
    plt.axvline(pendienteTramo,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Pendiente del tramo (%)")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/pendiente_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(pendienteTramo, nivelResultado, color="red" )
    plt.axvline(pendienteTramo,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Pendiente (%)")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/pendiente_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(pendienteTramo, densidadResultado, color="red" )
    plt.scatter(pendienteTramo, velocidadResultado, color="darkcyan" )
    plt.axvline(pendienteTramo,color="k", ls="dotted")
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Pendiente del tramo (%)")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/pendiente_densidad.png")
    plt.close()

def sensibilidadAccesos(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(0,25)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    anchoBermas = anchoBermaDerecha + anchoBermaIzquierda
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, element, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(numeroAccesos, capacidadResultado,color="red" )
    plt.scatter(numeroAccesos, volumenResultado, color="teal"  )
    plt.axvline(numeroAccesos,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Accesos/milla")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/accesos_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(numeroAccesos, nivelResultado, color="red" )
    plt.axvline(numeroAccesos,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Accesos/milla")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/accesos_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(numeroAccesos, densidadResultado, color="red" )
    plt.scatter(numeroAccesos, velocidadResultado, color="darkcyan" )
    plt.axvline(numeroAccesos,color="k", ls="dotted")
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Accesos/milla")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/accesos_densidad.png")
    plt.close()

def sensibilidadPesados(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(0,50)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    anchoBermas = anchoBermaDerecha + anchoBermaIzquierda
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
element, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(porcentajePesados, capacidadResultado,color="red" )
    plt.scatter(porcentajePesados, volumenResultado, color="teal"  )
    plt.axvline(porcentajePesados,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Porcentaje de vehículos pesados (%)")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/pesados_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(porcentajePesados, nivelResultado, color="red" )
    plt.axvline(porcentajePesados,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Porcentaje de vehículos pesados (%)")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/pesados_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(porcentajePesados, densidadResultado, color="red" )
    plt.scatter(porcentajePesados, velocidadResultado, color="darkcyan" )
    plt.axvline(porcentajePesados,color="k", ls="dotted")
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Porcentaje de vehículos pesados (%)")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/pesados_densidad.png")
    plt.close()

def sensibilidadVolumen(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas,velocidadResultado, capacidadResultado, nivelResultado, densidadResultado, volumenResultado):
    lista = np.arange(100,2800, 2)
    velocidadLista = []
    capacidadLista = []
    volumenLista = []
    nivelLista = []
    densidadLista = []
    anchoBermas = anchoBermaDerecha + anchoBermaIzquierda
    for element in lista:
        data = hcmln.hcmMultilaneFunction(numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, 
pendienteTramo, opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, element,tipoPoblacion ,factorHoraPico, 
porcentajePesados, porcentajeCamiones, porcentajeMulas)
        velocidadLista.append(data[5])
        capacidadLista.append(data[8])
        volumenLista.append(data[11])
        nivelLista.append(data[13])
        densidadLista.append(data[12])
    #Grafica que presenta la variación de vollumen ajustado y capacidad final al modificar el número de carriles
    plt.plot(lista, capacidadLista ,color="red",label="Capacidad ajustada")
    plt.plot(lista, volumenLista ,color="teal",label="Volumen ajustado")
    plt.scatter(volumenDemanda, capacidadResultado,color="red" )
    plt.scatter(volumenDemanda, volumenResultado, color="teal"  )
    plt.axvline(volumenDemanda,color="k", ls="dotted")
    plt.axhline(capacidadResultado,color="red", ls="dotted")
    plt.axhline(volumenResultado,color="teal", ls="dotted")
    plt.xlabel("Volumen de demanda (veh/h/carril)")
    plt.ylabel("pc/h/carril")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/volumen_capacidad.png")
    plt.close()

    #Grafica que presenta la variación del nivel de servicio  al modificar el número de carriles
    plt.plot(lista, nivelLista ,color="red",label="Nivel de Servicio")
    plt.scatter(volumenDemanda, nivelResultado, color="red" )
    plt.axvline(volumenDemanda,color="k", ls="dotted")
    plt.axhline(nivelResultado,color="red", ls="dotted")
    plt.xlabel("Volumen de demanda (veh/h/carril)")
    plt.ylabel("Nivel de Servicio")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/volumen_nivel.png")
    plt.close()

     #Grafica que presenta la variación de la densidad al modificar el número de carriles
    plt.plot(lista, densidadLista ,color="red",label="Densidad (pc/mi/carril)")
    plt.plot(lista, velocidadLista ,color="darkcyan",label="Velocidad (mi/h)")
    plt.scatter(volumenDemanda, densidadResultado, color="red" )
    plt.scatter(volumenDemanda, velocidadResultado, color="darkcyan" )
    plt.axvline(volumenDemanda,color="k", ls="dotted")
    plt.axhline(velocidadResultado,color="darkcyan", ls="dotted")
    plt.axhline(densidadResultado,color="red", ls="dotted")
    plt.xlabel("Volumen de demanda (veh/h/carril)")
    plt.ylabel("Densidad (pc/mi/carril) - Velocidad (mi/h)")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    fig.subplots_adjust(top=0.95)
    plt.savefig("static/assets/img/sensibilidadMultiline/volumen_densidad.png")
    plt.close()


