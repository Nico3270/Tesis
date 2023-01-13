from scipy.interpolate import lagrange, interp1d
import math

def interpolacion(x,y,z):
    y_interp = interp1d(x, y,fill_value="extrapolate")
    resultado = float(y_interp(z))
    return round(resultado,3)

#### Paso 1. Ingresó de valores de muestra
carriles = 3
a_carril = 10
a_bermaDerecha = 3
a_bermaIzquierda = 3
valor = 2
pendiente = 5.2
opc_velocidad = "No"
vel_campo = 70
velocidadBase = 60
accesos = 8
volumen = 1500
fhPico = 0.89
p_pesados = 15
recreativos = 5

#### Paso 2. Estimación o ajuste de velocidad a flujo libre FFS

## Función de factor de corrección por ancho de carril 12-20
def correccionFlw(anchoCarril):
    if anchoCarril >= 12:
        data = 0.0
    elif anchoCarril >= 11:
        data = 1.9
    else:
        data = 6.6
    return data

## Función de factor de corrección por espacio lateral derecho
tabla_12_21 = {6:[0.0,0.0,0.0,0.0],5:[0.6,0.4,0.2,0.1],4:[1.2,0.8,0.4,0.2],3:[1.8,1.2,0.6,0.3],2:[2.4,1.6,0.8,0.4],1:[3.0,2.0,1.0,0.5],0:[3.6,2.4,1.2,0.6]}

carriles_12_21 = [2,3,4,5]
ancho_berma_12_21 = [0,1,2,3,4,5,6]

def puntos(valor, lista):
    var = 0
    var1 = 0
    for element in lista:
        if valor > element and valor <= lista[(lista.index(element))+1]:
            var = element
            var1 = lista[(lista.index(element))+1]
    return(var,var1) 

def correccionFrlc(numeroCarriles, lateralDerecho):
    if lateralDerecho >= 6:
        data = 0
    elif numeroCarriles >5:
        var1 = puntos(lateralDerecho, ancho_berma_12_21)[0]
        var2 = puntos(lateralDerecho, ancho_berma_12_21)[1]
        data1 = interpolacion([6,5,4,3,2,1,0],[0.0,0.1,0.2,0.3,0.4,0.5,0.6],var1)
        data2 = interpolacion([6,5,4,3,2,1,0],[0.0,0.1,0.2,0.3,0.4,0.5,0.6],var2)
        data = interpolacion([var1,var2], [data1,data2],lateralDerecho)
    else:
        var1 = puntos(lateralDerecho, ancho_berma_12_21)[0]
        var2 = puntos(lateralDerecho, ancho_berma_12_21)[1]
        data1 = interpolacion(carriles_12_21, tabla_12_21.get(var1),numeroCarriles)
        data2 = interpolacion(carriles_12_21, tabla_12_21.get(var2),numeroCarriles)
        data = interpolacion([var1,var2], [data1,data2],lateralDerecho)
    return round(data,2)

## Función de factor de correccion por espacios laterales para multicarril
tabla12_22_4carriles =[0.0,0.4,0.9,1.3,1.8,3.6,5.4]
tabla12_22_6carriles =[0.0,0.4,0.9,1.3,1.7,2.8,3.9]
def correccionFtl(espacioDerecho, espacioIzquierdo, numeroCarriles):
    total = espacioDerecho + espacioIzquierdo
    if numeroCarriles == 4:
        data = interpolacion([12,10,8,6,4,2,0],tabla12_22_4carriles,total)
    else:
        data = interpolacion([12,10,8,6,4,2,0],tabla12_22_6carriles,total)
    return data

## Función de corrección por tipo de división

def correccionFm(division):
    if division == "No dividida":
        data = 1.6
    else:
        data = 0.0
    return data

##Función de corrección por puntos de acceso

def correccionFa(puntos_accesos):
    if puntos_accesos >= 40:
        data = 10.0
    else:
        data = interpolacion([0,10,20,30,40],[0.0,2.5,5.0,7.5,10.0],puntos_accesos)
    return data

## Función para corregir capacidad y velocidad de acuerdo a la población
def correccionPoblacion(poblacion):
    ##Data1 es ajuste a la capacidad
    #Data2 ajuste a la velocidad
    if poblacion == "Toda conocida":
        data1 = 1.0
        data2 = 1.0
    elif poblacion == "Mayormente conocida":
        data1 = 0.968
        data2 = 0.975
    elif poblacion == "Mezcla equilibrada":
        data1 = 0.939
        data2 = 0.950
    elif poblacion == "Mayormente desconocida":
        data1 = 0.898
        data2 = 0.913
    elif poblacion == "Totalmente desconocida":
        data1 = 0.852
        data2 = 0.863
    return (data1, data2)

## Velocidad a flujo libre ajustada
def velocidadAjustada(velocidad, poblacion):
    data = velocidad * correccionPoblacion(poblacion)[1]
    return data



### Función para calcular capacidad según tabla 12-4 y según ecuación 12-7

def capacidadTotal(velocidad):
    data1 = interpolacion([75,70,65,60,55,50,45],[2300,2300,2300,2200,2100,2000,1900],velocidad)
    if data1 >= 2300:
        data1 = 2300
    data2 = 1900 + 20 *(velocidad - 45)
    return (data1, data2)

### Capacidad ajustada
def capacidadAjustada(capacidad, poblacion):
    data = capacidad * correccionPoblacion(poblacion)[0]
    return data


# Funcion para determinar factor ET


tabla12_26_pMenos2 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.625:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.875:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],1.25:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],1.5:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97]}
tabla12_26_pend0 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.625:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.875:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],1.25:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],1.5:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97]}
tabla12_26_pend2 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[3.76,2.96,2.78,2.65,2.48,2.38,2.22,2.14,2.09],0.625:[4.47,3.33,3.08,2.91,2.68,2.54,2.34,2.23,2.17],0.875:[4.80,3.50,3.22,3.03,2.77,2.61,2.39,2.28,2.21],1.25:[5.00,3.60,3.30,3.09,2.83,2.66,2.42,2.30,2.23],1.5:[5.04,3.62,3.32,3.11,2.84,2.67,2.43,2.31,2.23]}
tabla12_26_pe2_5 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[4.11,3.14,2.93,2.78,2.58,2.46,2.28,2.19,2.13],0.625:[5.04,3.62,3.32,3.11,2.84,2.67,2.43,2.31,2.23],0.875:[5.48,3.85,3.51,3.27,2.96,2.77,2.50,2.36,2.28],1.25:[5.73,3.98,3.61,3.36,3.03,2.83,2.54,2.40,2.31],1.5:[5.80,4.02,3.64,3.38,3.05,2.84,2.55,2.41,2.32]}
tabla12_26_pe3_5 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[4.88,3.54,3.25,3.05,2.80,2.63,2.41,2.29,2.22],0.625:[6.34,4.30,3.87,3.58,3.20,2.97,2.64,2.48,2.38],0.875:[7.03,4.66,4.16,3.83,3.39,3.12,2.76,2.57,2.46],1.25:[7.44,4.87,4.33,3.97,3.50,3.22,2.82,2.62,2.50],1.5:[7.53,4.92,4.38,4.01,3.53,3.24,2.84,2.63,2.51]}
tabla12_26_pe4_5 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[5.80,4.02,3.64,3.38,3.05,2.84,2.55,2.41,2.32],0.625:[7.90,5.11,4.53,4.14,3.63,3.32,2.90,2.68,2.55],0.875:[8.91,5.64,4.96,4.50,3.92,3.56,3.07,2.82,2.67],1:[9.19,5.78,5.08,4.60,3.99,3.62,3.11,2.85,2.70]}
tabla12_26_pe5_5 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[6.87,4.58,4.10,3.77,3.35,3.09,2.73,2.55,2.44],0.625:[9.78,6.09,5.33,4.82,4.16,3.76,3.21,2.93,2.77],0.875:[11.20,6.83,5.94,5.33,4.56,4.09,3.45,3.12,2.93],1:[11.60,7.04,6.11,5.47,4.67,4.18,3.51,3.17,2.97]}
tabla12_26_pend6 = {0.125:[2.62,2.37,2.30,2.24,2.17,2.12,2.04,1.99,1.97],0.375:[7.48,4.90,4.36,3.99,3.52,3.23,2.83,2.63,2.51],0.625:[10.87,6.66,5.79,5.21,4.46,4.04,3.39,3.08,2.89],0.875:[12.54,7.54,6.51,5.81,4.94,4.40,3.67,3.30,3.08],1:[13.02,7.78,6.71,5.99,5.07,4.51,3.75,3.37,3.14]}
tabla12_26x = [2,4,5,6,8,10,15,20,25]

def factorET(terreno, pendiente, longitud, pesados):
    if terreno == "Terreno plano":
        data = 2.0
    elif terreno == "Terreno ondulado":
        data = 3.0
    else:
        if pendiente <= 3.5 and longitud >= 1.5:
            longitud = 1.5
        if pendiente > 3.5 and longitud >= 1.0:
            longitud = 1.0
        
        var1 = puntos(longitud, [0.125,0.375,0.625,0.875,1.25,1.5])[0]  
        var2 = puntos(longitud, [0.125,0.375,0.625,0.875,1.25,1.5])[1]
        penMenos2_0 = interpolacion(tabla12_26x,tabla12_26_pMenos2.get(var1),  pesados)
        penMenos2_1 = interpolacion(tabla12_26x,tabla12_26_pMenos2.get(var2),  pesados)
        penMenosFinal = interpolacion([var1,var2],[penMenos2_0,penMenos2_1],longitud)
        pendiente0_0 = interpolacion(tabla12_26x, tabla12_26_pend0.get(var1),  pesados)
        pendiente0_1 = interpolacion(tabla12_26x, tabla12_26_pend0.get(var2),  pesados)
        penceroFinal = interpolacion([var1,var2],[pendiente0_0,pendiente0_1], longitud)
        pendiente2_0 = interpolacion(tabla12_26x, tabla12_26_pend2.get(var1),  pesados)
        pendiente2_1 = interpolacion(tabla12_26x, tabla12_26_pend2.get(var2),  pesados)
        pendosFinal = interpolacion([var1,var2],[pendiente2_0,pendiente2_1], longitud)
        pendiente2_5_0 = interpolacion(tabla12_26x,tabla12_26_pe2_5.get(var1),  pesados)
        pendiente2_5_1 = interpolacion(tabla12_26x,tabla12_26_pe2_5.get(var2),  pesados)
        pendos_5Final = interpolacion([var1,var2],[pendiente2_5_0,pendiente2_5_1],longitud)
        pendiente3_5_0 = interpolacion(tabla12_26x,tabla12_26_pe3_5.get(var1),  pesados)
        pendiente3_5_1 = interpolacion(tabla12_26x,tabla12_26_pe3_5.get(var2),  pesados)
        pentres_5Final = interpolacion([var1,var2],[pendiente3_5_0,pendiente3_5_1],longitud)
        if longitud >= 1:
            longitud = 1
        var1 = puntos(longitud, [0.125,0.375,0.625,0.875,1])[0]
        var2 = puntos(longitud, [0.125,0.375,0.625,0.875,1])[1]
        pendiente4_5_0 = interpolacion(tabla12_26x, tabla12_26_pe4_5.get(var1),  pesados)
        pendiente4_5_1 = interpolacion(tabla12_26x, tabla12_26_pe4_5.get(var2),  pesados)
        pencuatro_5Final = interpolacion([var1,var2],[pendiente4_5_0,pendiente4_5_1],longitud)
        pendiente5_5_0 = interpolacion(tabla12_26x, tabla12_26_pe5_5.get(var1),  pesados)
        pendiente5_5_1 = interpolacion(tabla12_26x, tabla12_26_pe5_5.get(var2),  pesados)
        pencinco_5Final = interpolacion([var1,var2],[pendiente5_5_0,pendiente5_5_1],longitud)
        pendienteSeis_0 = interpolacion(tabla12_26x, tabla12_26_pend6.get(var1),  pesados)
        pendienteSeis_1 = interpolacion(tabla12_26x, tabla12_26_pend6.get(var2),  pesados)
        penseis_Final = interpolacion([var1,var2],[pendienteSeis_0,pendienteSeis_1],longitud)
        data = interpolacion([-2,0,2,2.5,3.5,4.5,5.5,6],[penMenosFinal, penceroFinal,pendosFinal,pendos_5Final,pentres_5Final,pencuatro_5Final,pencinco_5Final,penseis_Final],pendiente)
    return round(data,2)

tabla12_27_pMenos2 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.625:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.875:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],1.25:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],1.5:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93]}
tabla12_27_pend0 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.625:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.875:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],1.25:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],1.5:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93]}
tabla12_27_pend2 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1,93],0.375:[3.76,2.95,2.77,2.64,2.47,2.36,2.20,2.11,2.06],0.625:[4.32,3.24,3.01,2.84,2.63,2.49,2.29,2.19,2.12],0.875:[4.57,3.37,3.11,2.93,2.70,2.55,2.33,2.22,2.15],1.25:[4.71,3.45,3.17,2.99,2.74,2.58,2.36,2.24,2.17],1.5:[4.74,3.47,3.19,3.00,2.75,2.59,2.36,2.24,2.17]}
tabla12_27_pe2_5 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[4.10,3.13,2.92,2.77,2.57,2.44,2.26,2.16,2.10],0.625:[4.84,3.52,3.23,3.03,2.77,2.61,2.38,2.26,2.18],0.875:[5.17,3.69,3.37,3.15,2.87,2.69,2.43,2.30,2.22],1.25:[5.36,3.79,3.45,3.22,2.92,2.73,2.47,2.33,2.24],1.5:[5.40,3.81,3.47,3.24,2.93,2.74,2.47,2.33,2.25]}
tabla12_27_pe3_5 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[4.89,3.54,3.25,3.05,2.79,2.62,2.39,2.26,2.19],0.625:[6.05,4.15,3.75,3.47,3.11,2.89,2.58,2.42,2.32],0.875:[6.58,4.43,3.97,3.66,3.26,3.01,2.67,2.49,2.39],1.25:[6.88,4.58,4.10,3.77,3.35,3.09,2.72,2.53,2.42],1.5:[6.95,4.62,4.13,3.80,3.37,3.10,2.73,2.54,2.43]}
tabla12_27_pe4_5 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[5.83,4.03,3.65,3.39,3.05,2.84,2.55,2.39,2.30],0.625:[7.53,4.92,4.38,4.01,3.53,3.24,2.83,2.62,2.50],0.875:[8.32,5.34,4.72,4.29,3.75,3.42,2.97,2.73,2.59],1:[8.53,5.54,4.81,4.37,3.81,3.47,3.00,2.76,2.62]}
tabla12_27_pe5_5 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[6.97,4.63,4.14,3.81,3.38,3.11,2.74,2.55,2.43],0.625:[9.37,5.89,5.16,4.68,4.05,3.67,3.14,2.88,2.72],0.875:[10.49,6.48,5.65,5.09,4.37,3.93,3.34,3.03,2.85],1:[10.80,6.64,5.78,5.20,4.46,4.01,3.39,3.08,2.89]}
tabla12_27_pend6 = {0.125:[2.67,2.38,2.31,2.25,2.16,2.11,2.02,1.97,1.93],0.375:[7.64,4.98,4.43,4.05,3.56,3.26,2.85,2.64,2.51],0.625:[10.45,6.45,5.63,5.07,4.36,3.92,3.33,3.03,2.85],0.875:[11.78,7.16,6.20,5.56,4.74,4.24,3.56,3.22,3.01],1:[12.15,7.35,6.36,5.69,4.85,4.33,3.62,3.27,3.05]}




def factorET2(terreno, pendiente, longitud, pesados):
    if terreno == "Terreno plano":
        data = 2.0
    elif terreno == "Terreno ondulado":
        data = 3.0
    else:
        if pendiente <= 3.5 and longitud >= 1.5:
            longitud = 1.5
        if pendiente > 3.5 and longitud >= 1.0:
            longitud = 1.0
        
        var1 = puntos(longitud, [0.125,0.375,0.625,0.875,1.25,1.5])[0]  
        var2 = puntos(longitud, [0.125,0.375,0.625,0.875,1.25,1.5])[1]
        penMenos2_0 = interpolacion(tabla12_26x,tabla12_27_pMenos2.get(var1),  pesados)
        penMenos2_1 = interpolacion(tabla12_26x,tabla12_27_pMenos2.get(var2),  pesados)
        penMenosFinal = interpolacion([var1,var2],[penMenos2_0,penMenos2_1],longitud)
        pendiente0_0 = interpolacion(tabla12_26x, tabla12_27_pend0.get(var1),  pesados)
        pendiente0_1 = interpolacion(tabla12_26x, tabla12_27_pend0.get(var2),  pesados)
        penceroFinal = interpolacion([var1,var2],[pendiente0_0,pendiente0_1], longitud)
        pendiente2_0 = interpolacion(tabla12_26x, tabla12_27_pend2.get(var1),  pesados)
        pendiente2_1 = interpolacion(tabla12_26x, tabla12_27_pend2.get(var2),  pesados)
        pendosFinal = interpolacion([var1,var2],[pendiente2_0,pendiente2_1], longitud)
        pendiente2_5_0 = interpolacion(tabla12_26x,tabla12_27_pe2_5.get(var1),  pesados)
        pendiente2_5_1 = interpolacion(tabla12_26x,tabla12_27_pe2_5.get(var2),  pesados)
        pendos_5Final = interpolacion([var1,var2],[pendiente2_5_0,pendiente2_5_1],longitud)
        pendiente3_5_0 = interpolacion(tabla12_26x,tabla12_27_pe3_5.get(var1),  pesados)
        pendiente3_5_1 = interpolacion(tabla12_26x,tabla12_27_pe3_5.get(var2),  pesados)
        pentres_5Final = interpolacion([var1,var2],[pendiente3_5_0,pendiente3_5_1],longitud)
        if longitud >= 1:
            longitud = 1
        var1 = puntos(longitud, [0.125,0.375,0.625,0.875,1])[0]
        var2 = puntos(longitud, [0.125,0.375,0.625,0.875,1])[1]
        pendiente4_5_0 = interpolacion(tabla12_26x, tabla12_27_pe4_5.get(var1),  pesados)
        pendiente4_5_1 = interpolacion(tabla12_26x, tabla12_27_pe4_5.get(var2),  pesados)
        pencuatro_5Final = interpolacion([var1,var2],[pendiente4_5_0,pendiente4_5_1],longitud)
        pendiente5_5_0 = interpolacion(tabla12_26x, tabla12_27_pe5_5.get(var1),  pesados)
        pendiente5_5_1 = interpolacion(tabla12_26x, tabla12_27_pe5_5.get(var2),  pesados)
        pencinco_5Final = interpolacion([var1,var2],[pendiente5_5_0,pendiente5_5_1],longitud)
        pendienteSeis_0 = interpolacion(tabla12_26x, tabla12_27_pend6.get(var1),  pesados)
        pendienteSeis_1 = interpolacion(tabla12_26x, tabla12_27_pend6.get(var2),  pesados)
        penseis_Final = interpolacion([var1,var2],[pendienteSeis_0,pendienteSeis_1],longitud)
        data = interpolacion([-2,0,2,2.5,3.5,4.5,5.5,6],[penMenosFinal, penceroFinal,pendosFinal,pendos_5Final,pentres_5Final,pencuatro_5Final,pencinco_5Final,penseis_Final],pendiente)
    return round(data,2)

tabla12_28_pMenos2 = {0.125:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],0.375:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],0.625:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],0.875:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],1.25:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],1.5:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83]}
tabla12_28_pend0 = {0.125:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],0.375:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],0.625:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],0.875:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],1.25:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83],1.5:[2.39,2.18,2.12,2.07,2.01,1.96,1.89,1.85,1.83]}
tabla12_28_pend2 = {0.125:[2.67,2.32,2.23,2.17,2.08,2.03,1.94,1.89,1.86],0.375:[3.36,2.82,2.64,2.52,2.35,2.25,2.10,2.02,1.97],0.625:[4.12,3.08,2.85,2.69,2.49,2.36,2.18,2.08,2.02],0.875:[4.37,3.21,2.96,2.78,2.56,2.42,2.22,2.11,2.05],1.25:[4.53,3.29,3.02,2.84,2.60,2.45,2.24,2.13,2.07],1.5:[4.58,3.31,3.04,2.86,2.61,2.46,2.25,2.14,2.07]}
tabla12_28_pe2_5 = {0.125:[2.75,2.36,2.27,2.20,2.11,2.04,1.95,1.90,1.87],0.375:[4.01,3.02,2.80,2.65,2.46,2.33,2.16,2.06,2.01],0.625:[4.66,3.35,3.08,2.88,2.64,2.48,2.26,2.15,2.08],0.875:[4.99,3.52,3.21,3.00,2.73,2.56,2.32,2.19,2.13],1.25:[5.20,3.64,3.30,3.08,2.79,2.60,2.35,2.22,2.14],1.5:[5.26,3.67,3.33,3.10,2.80,2.62,2.36,2.23,2.15]}
tabla12_28_pe3_5 = {0.125:[2.93,2.45,2.34,2.26,2.16,2.09,1.98,1.92,1.89],0.375:[4.86,3.46,3.16,2.96,2.69,2.53,2.30,2.18,2.10],0.625:[5.88,3.99,3.59,3.32,2.98,2.76,2.46,2.31,2.22],0.875:[6.40,4.26,3.81,3.51,3.12,2.88,2.55,2.38,2.28],1.25:[6.74,4.43,3.96,3.63,3.21,2.96,2.60,2.42,2.32],1.5:[6.83,4.48,3.99,3.66,3.24,2.98,2.62,2.44,2.33]}
tabla12_28_pe4_5 = {0.125:[3.13,2.56,2.43,2.34,2.21,2.13,2.01,1.95,1.91],0.375:[5.88,3.99,3.59,3.32,2.98,2.76,2.46,2.31,2.22],0.625:[7.35,4.75,4.22,3.85,3.39,3.10,2.71,2.51,2.39],0.875:[8.11,5.15,4.54,4.13,3.60,3.27,2.83,2.61,2.47],1:[8.33,5.27,4.63,4.21,3.66,3.33,2.87,2.64,2.50]}
tabla12_28_pe5_5 = {0.125:[3.37,2.69,2.53,2.42,2.28,2.19,2.05,1.98,1.94],0.375:[7.09,4.62,4.11,3.76,3.31,3.04,2.66,2.47,2.36],0.625:[9.13,5.68,4.97,4.79,3.88,3.51,3.00,2.74,2.59],0.875:[10.21,6.24,5.43,4.88,4.18,3.76,3.18,2.89,2.71],1:[10.52,6.41,5.57,5.00,4.27,3.83,3.24,2.93,2.75]}
tabla12_28_pend6 = {0.125:[3.51,2.76,2.59,2.47,2.32,2.22,2.08,2.00,1.95],0.375:[7.78,4.98,4.40,4.01,3.51,3.20,2.78,2.56,2.44],0.625:[10.17,6.23,5.42,4.87,4.17,3.75,3.18,2.88,2.71],0.875:[11.43,6.88,5.95,5.32,4.53,4.04,3.39,3.06,2.86],1:[11.81,7.07,6.11,5.46,4.64,4.13,3.45,3.11,2.90]}


def factorET3(terreno, pendiente, longitud, pesados):
    
    if terreno == "Terreno plano":
        data = 2.0
    elif terreno == "Terreno ondulado":
        data = 3.0
    else:
        if pendiente <= 3.5 and longitud >= 1.5:
            longitud = 1.5
        if pendiente > 3.5 and longitud >= 1.0:
            longitud = 1.0
        
        var1 = puntos(longitud, [0.125,0.375,0.625,0.875,1.25,1.5])[0]  
        var2 = puntos(longitud, [0.125,0.375,0.625,0.875,1.25,1.5])[1]
        penMenos2_0 = interpolacion(tabla12_26x,tabla12_28_pMenos2.get(var1),  pesados)
        penMenos2_1 = interpolacion(tabla12_26x,tabla12_28_pMenos2.get(var2),  pesados)
        penMenosFinal = interpolacion([var1,var2],[penMenos2_0,penMenos2_1],longitud)
        pendiente0_0 = interpolacion(tabla12_26x, tabla12_28_pend0.get(var1),  pesados)
        pendiente0_1 = interpolacion(tabla12_26x, tabla12_28_pend0.get(var2),  pesados)
        penceroFinal = interpolacion([var1,var2],[pendiente0_0,pendiente0_1], longitud)
        pendiente2_0 = interpolacion(tabla12_26x, tabla12_28_pend2.get(var1),  pesados)
        pendiente2_1 = interpolacion(tabla12_26x, tabla12_28_pend2.get(var2),  pesados)
        pendosFinal = interpolacion([var1,var2],[pendiente2_0,pendiente2_1], longitud)
        pendiente2_5_0 = interpolacion(tabla12_26x,tabla12_28_pe2_5.get(var1),  pesados)
        pendiente2_5_1 = interpolacion(tabla12_26x,tabla12_28_pe2_5.get(var2),  pesados)
        pendos_5Final = interpolacion([var1,var2],[pendiente2_5_0,pendiente2_5_1],longitud)
        pendiente3_5_0 = interpolacion(tabla12_26x,tabla12_28_pe3_5.get(var1),  pesados)
        pendiente3_5_1 = interpolacion(tabla12_26x,tabla12_28_pe3_5.get(var2),  pesados)
        pentres_5Final = interpolacion([var1,var2],[pendiente3_5_0,pendiente3_5_1],longitud)
        if longitud >= 1:
            longitud = 1
        var1 = puntos(longitud, [0.125,0.375,0.625,0.875,1])[0]
        var2 = puntos(longitud, [0.125,0.375,0.625,0.875,1])[1]
        pendiente4_5_0 = interpolacion(tabla12_26x, tabla12_28_pe4_5.get(var1),  pesados)
        pendiente4_5_1 = interpolacion(tabla12_26x, tabla12_28_pe4_5.get(var2),  pesados)
        pencuatro_5Final = interpolacion([var1,var2],[pendiente4_5_0,pendiente4_5_1],longitud)
        pendiente5_5_0 = interpolacion(tabla12_26x, tabla12_28_pe5_5.get(var1),  pesados)
        pendiente5_5_1 = interpolacion(tabla12_26x, tabla12_28_pe5_5.get(var2),  pesados)
        pencinco_5Final = interpolacion([var1,var2],[pendiente5_5_0,pendiente5_5_1],longitud)
        pendienteSeis_0 = interpolacion(tabla12_26x, tabla12_28_pend6.get(var1),  pesados)
        pendienteSeis_1 = interpolacion(tabla12_26x, tabla12_28_pend6.get(var2),  pesados)
        penseis_Final = interpolacion([var1,var2],[pendienteSeis_0,pendienteSeis_1],longitud)
        data = interpolacion([-2,0,2,2.5,3.5,4.5,5.5,6],[penMenosFinal, penceroFinal,pendosFinal,pendos_5Final,pentres_5Final,pencuatro_5Final,pencinco_5Final,penseis_Final],pendiente)
    return round(data,2)


def factorETfinal(terreno, pendiente, longitud, tractomulas, camiones,pesados):
    if abs(tractomulas - camiones) < 10:
        data = factorET2(terreno, pendiente, longitud,pesados)
    elif tractomulas > camiones:
        data = factorET(terreno, pendiente, longitud,pesados)
    else:
        data = factorET3(terreno, pendiente, longitud,pesados)
    return data
    

#### Funcion para determinar factor Fhv
def factorFHV(PorcentajePesados, correccionEt):
    PorcentajePesados = round(PorcentajePesados/100,2)
    data = 1/(1+(PorcentajePesados*(correccionEt-1)))
    return round(data,2)



##Función para estimar el volumen ajustado

def volumenAjustado(numero_carriles, factorPHF, factorFhv, volumen):
    data = volumen/(factorPHF * numero_carriles * factorFhv)
    return round(data,0)

## Función nivel de servicio

def nivelServicio(capacidad, volumen, densidad):
    if volumen >= capacidad:
        data = "F"
    else:
        if densidad <= 11:
            data = "A"
        elif densidad < 18:
            data = "B"
        elif densidad < 26:
            data = "C"
        elif densidad  < 35:
            data = "D"
        elif densidad < 45:
            data = "E"
        else:
            data = "F"
    return data


### Funcion completa

def hcmMultilaneFunction (numeroCarriles, anchoCarril,tipoSeparacion, anchoBermaDerecha, anchoBermaIzquierda, longitudTramo,tipoTerreno, pendienteTramo,
opcionVelocidad, velocidadCampo, velocidadFfsBase, numeroAccesos, volumenDemanda,tipoPoblacion ,factorHoraPico, porcentajePesados, porcentajeCamiones, porcentajeMulas):
    if opcionVelocidad == "Si":
        velocidadFlujoLibre = velocidadCampo
    else:
        factorAnchoCarril = correccionFlw(anchoCarril)
        factorBermas = correccionFtl(anchoBermaDerecha , anchoBermaIzquierda, numeroCarriles)
        factorSeparacion = correccionFm(tipoSeparacion)
        factorAccesos = correccionFa(numeroAccesos)
        velocidadFlujoLibre = velocidadFfsBase - factorAnchoCarril - factorBermas - factorSeparacion - factorAccesos
    velocidadFFS_ajustada = round(velocidadAjustada(velocidadFlujoLibre,tipoPoblacion),1)
    capacidadTabla = int(capacidadTotal(velocidadFFS_ajustada)[0])
    capacidadFormula = int(capacidadTotal(velocidadFFS_ajustada)[1])
    capacidadFinal = int(capacidadAjustada(capacidadFormula,tipoPoblacion))
    factorPesados = factorETfinal(tipoTerreno, pendienteTramo,longitudTramo, porcentajeMulas, porcentajeCamiones, porcentajePesados)
    factorAjusteFhv = round(factorFHV(porcentajePesados, factorPesados),3)
    volumenAjustadoFinal = volumenAjustado(numeroCarriles, factorHoraPico, factorAjusteFhv, volumenDemanda)
    densidadFinal = round((volumenAjustadoFinal/velocidadFFS_ajustada),2)
    nivelDeServicio = nivelServicio(capacidadTabla, volumenAjustadoFinal, densidadFinal)
    return (factorAnchoCarril, factorBermas, factorSeparacion,factorAccesos, velocidadFlujoLibre, velocidadFFS_ajustada, capacidadTabla, capacidadFormula, capacidadFinal, 
     factorPesados,factorAjusteFhv,volumenAjustadoFinal, densidadFinal, nivelDeServicio)

