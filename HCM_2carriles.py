from scipy.interpolate import lagrange, interp1d
import math

def interpolacion(x,y,z):
    y_interp = interp1d(x, y,fill_value="extrapolate")
    resultado = float(y_interp(z))
    return round(resultado,3)

#Variables de entrada
clase_autopista = 2
a_carril = 10.83
a_berma = 3.28
densidad_accesos = 5
longitud_tramo = 1
pendiente_tramo = 7
Tipo_terreno = 5
p_no_rebase = 40
V_flujoLibre = 100
Longitud_adelantamiento = 2.5
#Volumen en vehiculos/hora ambos sentidos
volumen_demanda = 340
volumen_direccional = 56
periodo_analisis = 5
fhp = 0.93
p_pesados = 20
recreativos = 0

#Estimación de factor de ajuste por ancho de carril y berma
carril_factor = 0
def factor_carril(a_carril,a_berma):
    if a_carril >= 9 and a_carril < 10:
        if a_berma >= 0 and a_berma < 2:
            carril_factor = 6.4
        elif a_berma >= 2 and a_berma < 4:
            carril_factor = 4.8
        elif a_berma >= 4 and a_berma < 6:
            carril_factor = 3.5
        else:
            carril_factor = 2.2
    elif a_carril >= 10 and a_carril < 11:
        if a_berma >= 0 and a_berma < 2:
            carril_factor = 5.3
        elif a_berma >= 2 and a_berma < 4:
            carril_factor = 3.7
        elif a_berma >= 4 and a_berma < 6:
            carril_factor = 2.4
        else:
            carril_factor = 1.1
    elif a_carril >= 11 and a_carril < 12:
        if a_berma >= 0 and a_berma < 2:
            carril_factor = 4.7
        elif a_berma >= 2 and a_berma < 4:
            carril_factor = 3.0
        elif a_berma >= 4 and a_berma < 6:
            carril_factor = 1.7
        else:
            carril_factor = 0.4
    elif a_carril >= 12:
        if a_berma >= 0 and a_berma < 2:
            carril_factor = 4.2
        elif a_berma >= 2 and a_berma < 4:
            carril_factor = 2.6
        elif a_berma >= 4 and a_berma < 6:
            carril_factor = 1.3
        else:
            carril_factor = 0.0
    return carril_factor

#Estimación de factor de ajuste por densidad de puntos de accesos ( Access points per Mile (Both Sides))
tabla15_8 = [0,10,20,30,40]
tabla15_8x = [0.0,2.5,5.0,7.5,10]
def factor_accesos(puntos):
    resultado = interpolacion(tabla15_8, tabla15_8x, puntos)
    return resultado




Fls = factor_carril(a_carril, a_berma)
FA = factor_accesos(densidad_accesos)
bffs = V_flujoLibre

vel_flujo_libre = bffs - FA - Fls

########## PASO 3 AJUSTE PARA ATS (Velocidad de viaje promedio (mi/h))########
## Paso requerido para clase I y clase III ##

volumen1 = int(volumen_demanda*(volumen_direccional/100))
volumen2 = volumen_demanda- volumen1

tabla15_9 = [100,200,300,400,500,600,700,800,900]
tabla15_9x = [0.67,0.75,0.8,0.90,0.95,0.97,0.98,0.99,1.00]
## Se necesita factor fgATS de la tabla 15-9 o 15-10 ## Terreno ondulado
 

tabla3_35 = {0.25:[0.78,0.84,0.87,0.91,1.00,1.00,1.00,1.00,1.00],
            0.50:[0.75,0.83,0.86,0.90,1.00,1.00,1.00,1.00,1.00],
            0.75:[0.73,0.81,0.85,0.89,1.00,1.00,1.00,1.00,1.00],
            1.00:[0.73,0.79,0.83,0.88,1.00,1.00,1.00,1.00,1.00],
            1.50:[0.73,0.79,0.83,0.87,0.99,0.99,1.00,1.00,1.00],
            2.00:[0.73,0.79,0.82,0.86,0.98,0.98,0.99,1.00,1.00],
            3.00:[0.73,0.78,0.82,0.85,0.95,0.96,0.96,0.97,0.98],
            4.00:[0.73,0.78,0.81,0.85,0.94,0.94,0.95,0.95,0.96]}

tabla35_45 = {0.25:[0.75,0.83,0.86,0.90,1.00,1.00,1.00,100,1.00],
            0.50:[0.72,0.80,0.84,0.88,1.00,1.00,1.00,1.00,1.00],
            0.75:[0.67,0.77,0.81,0.86,1.00,1.00,1.00,1.00,1.00],
            1.00:[0.65,0.73,0.77,0.81,0.94,0.95,0.97,1.00,1.00],
            1.50:[0.63,0.72,0.76,0.80,0.93,0.95,0.96,1.00,1.00],
            2.00:[0.62,0.70,0.74,0.79,0.93,0.94,0.96,1.00,1.00],
            3.00:[0.61,0.69,0.74,0.78,0.92,0.93,0.94,0.98,1.00],
            4.00:[0.61,0.69,0.73,0.78,0.91,0.91,0.92,0.96,1.00]}
 
tabla45_55 = {0.25:[0.71,0.79,0.83,0.88,1.00,1.00,1.00,1.00,1.00],
            0.50:[0.60,0.70,0.74,0.79,0.94,0.95,0.97,1.00,1.00],
            0.75:[0.55,0.65,0.70,0.75,0.91,0.93,0.95,1.00,1.00],
            1.00:[0.54,0.64,0.69,0.74,0.91,0.93,0.95,1.00,1.00],
            1.50:[0.52,0.62,0.67,0.72,0.88,0.90,0.93,1.00,1.00],
            2.00:[0.51,0.61,0.66,0.71,0.87,0.89,0.92,0.99,1.00],
            3.00:[0.51,0.61,0.65,0.70,0.86,0.88,0.91,0.98,0.99],
            4.00:[0.51,0.60,0.65,0.69,0.84,0.86,0.88,0.95,0.97]}

tabla55_65 = {0.25:[0.57,0.68,0.72,0.77,0.93,0.94,0.96,1.00,1.00],
            0.50:[0.52,0.62,0.66,0.71,0.87,0.90,0.92,1.00,1.00],
            0.75:[0.49,0.57,0.62,0.68,0.85,0.88,0.90,1.00,1.00],
            1.00:[0.46,0.56,0.60,0.65,0.82,0.85,0.88,1.00,1.00],
            1.50:[0.44,0.54,0.59,0.64,0.81,0.84,0.87,0.98,1.00],
            2.00:[0.43,0.53,0.58,0.63,0.81,0.83,0.86,0.97,0.99],
            3.00:[0.41,0.51,0.56,0.61,0.79,0.82,0.85,0.97,0.99],
            4.00:[0.40,0.50,0.55,0.61,0.79,0.82,0.85,0.97,0.99]}

tabla65 = {0.25:[0.54,0.64,0.68,0.73,0.88,0.90,0.92,1.00,1.00],
        0.5:[0.43,0.53,0.57,0.62,0.79,0.82,0.85,0.98,1.00],
        0.75:[0.39,0.49,0.54,0.59,0.77,0.80,0.83,0.96,1.00],
        1.00:[0.37,0.45,0.50,0.54,0.74,0.77,0.81,0.96,1.00],
        1.50:[0.35,0.45,0.49,0.54,0.71,0.75,0.79,0.96,1.00],
        2.00:[0.34,0.44,0.48,0.53,0.71,0.74,0.78,0.94,0.99],
        3.00:[0.34,0.44,0.48,0.53,0.70,0.73,0.77,0.93,0.98],
        4.00:[0.33,0.43,0.47,0.52,0.70,0.73,0.77,0.91,0.95]}

tabla15_10 = [100,200,300,400,500,600,700,800,900]
longitudes = [0.25, 0.50, 0.75, 1.00, 1.50, 2.00, 3.00, 4.00]
def puntos(longitud):
    for element in longitudes:
        if longitud > element and longitud <= longitudes[(longitudes.index(element))+1]:
            var = element
            var1 = longitudes[(longitudes.index(element))+1]
    return(var,var1) 
valor = 0
#print(tabla3_35.get(2.00))
### fg ATS para pendientes mayores a 3
def fgATS_pendientes(longitud, volumen, pendiente, tabla):
    vars = puntos(longitud)
    if volumen <= 100:
        valor1 = tabla.get(vars[0])[0]
        valor2 = tabla.get(vars[1])[0]
        valor = interpolacion( [vars[0], vars[1]],[valor1, valor2], longitud)
    elif volumen >100 and volumen <900:
        valor1 = interpolacion( tabla15_10,tabla.get(vars[0]), volumen)
        valor2 = interpolacion( tabla15_10,tabla.get(vars[1]), volumen)
        valor = interpolacion( [vars[0], vars[1]],[valor1, valor2], longitud)
    elif volumen >= 900:
        valor1 = tabla.get(vars[0])[8]
        valor2 = tabla.get(vars[1])[8]
        valor = interpolacion( [vars[0], vars[1]],[valor1, valor2], longitud)
    return round(valor,2)


def fgATS_pendientes1(longitud, volumen, pendiente, tabla):
    if longitud <= 0.25:
        valor = interpolacion(tabla.get(0.25), tabla15_10, volumen)
    elif longitud > 0.25 and longitud <4:
        valor = fgATS_pendientes(longitud, volumen, pendiente, tabla)
    elif longitud >= 4:
        if volumen >= 900:
            valor = tabla.get(4.00)[8]
        else:    
            valor = interpolacion( tabla15_10,tabla.get(4.00), volumen)
    return valor

## El valor  final de ajuste fgATS para pendientes especificas mayores a 3 se encuentra con la siguiente función
def fgATS_pendientes2(longitud, volumen, pendiente):
    if pendiente <= 1:
        final = 1.0
    elif pendiente <3:
        if volumen <= 100:
            final = 0.67
        elif volumen >100 and volumen <900:
            final = round(interpolacion(tabla15_9, tabla15_9x, volumen),2)
        else:
            final = 1.00
        return final
    elif pendiente >= 3 and pendiente <3.5:
        tabla = tabla3_35
    elif pendiente >= 3.5 and pendiente <4.5:
        tabla = tabla35_45
    elif pendiente >= 4.5 and pendiente < 5.5:
        tabla = tabla45_55
    elif pendiente >= 5.5 and pendiente < 6.5:
        tabla = tabla55_65
    else:
        tabla = tabla65
    final = fgATS_pendientes1(longitud, volumen, pendiente, tabla)
    return final

## Fáctores según volumen ##


fgATS1 = fgATS_pendientes2(longitud_tramo, volumen1, pendiente_tramo)
fgATS2 = fgATS_pendientes2(longitud_tramo, volumen2, pendiente_tramo)


####ATS Heavy Vehicle Adjustment Factor #########

tabla15_11 = [100,200,300,400,500,600,700,800,900]
tabla15_11x = [1.9,1.5,1.4,1.3,1.2,1.1,1.1,1.1,1.0]
tabla15_11x2 = [2.7,2.3,2.1,2.0,1.8,1.7,1.6,1.4,1.3]

tabla15_12_3_35 = {0.25:[2.6,2.4,2.3,2.2,1.8,1.8,1.7,1.3,1.1],0.50:[3.7,3.4,3.3,3.2,2.7,2.6,2.6,1.9,1.6],
0.75:[4.6,4.4,4.3,4.2,3.7,3.6,3.4,2.4,1.9],1.00:[5.2,5.0,4.9,4.9,4.4,4.2,4.1,3.0,2.3],
1.50:[6.2,6.0,5.9,5.8,5.3,5.0,4.8,3.6,2.9],2.00:[7.3,6.9,6.7,6.5,5.7,5.5,5.3,4.1,3.5],
3.00:[8.4,8.0,7.7,7.5,6.5,6.2,6.0,4.6,3.9],4.00:[9.4,8.8,8.6,8.3,7.2,6.9,6.6,4.8,3.7]}
tabla15_12_35_45 = {0.25:[3.8,3.4,3.2,3.0,2.3,2.2,2.2,1.7,1.5],0.50:[5.5,5.3,5.1,5.0,4.4,4.2,4.0,2.8,2.2],
0.75:[6.5,6.4,6.5,6.5,6.3,5.9,5.6,3.6,2.6],1.00:[7.9,7.6,7.4,7.3,6.7,6.6,6.4,5.3,4.7],
1.50:[9.6,9.2,9.0,8.9,8.1,7.9,7.7,6.5,5.9],2.00:[10.3,10.1,10.0,9.9,9.4,9.1,8.9,7.4,6.7],
3.00:[11.4,11.3,11.2,11.2,10.7,10.3,10.0,8.0,7.0],4.00:[12.4,12.2,12.2,12.1,11.5,11.2,10.8,8.6,7.5]}
tabla15_12_45_55 = {0.25:[4.4,4.0,3.7,3.5,2.7,2.7,2.7,2.6,2.5],0.50:[6.0,6.0,6.0,6.0,5.9,5.7,5.6,4.6,4.2],
0.75:[7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5,7.5],1.00:[9.2,9.2,9.1,9.1,9.0,9.0,9.0,8.9,8.8],
1.50:[10.6,10.6,10.6,10.6,10.5,10.4,10.4,10.2,10.1],2.00:[11.8,11.8,11.8,11.8,11.6,11.6,11.5,11.1,10.9],
3.00:[13.7,13.7,13.6,13.6,13.3,13.1,13.0,11.9,11.3],4.00:[15.3,15.3,15.2,15.2,14.6,14.2,13.8,11.3,10.0]}
tabla15_12_55_65 = {0.25:[4.8,4.6,4.5,4.4,4.0,3.9,3.8,3.2,2.9],0.50:[7.2,7.2,7.2,7.2,7.2,7.2,7.2,7.2,7.2],
0.75:[9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1],1.00:[10.3,10.3,10.3,10.3,10.3,10.3,10.3,10.2,10.1],
1.50:[11.9,11.9,11.9,11.9,11.8,11.8,11.8,11.7,11.6],2.00:[12.8,12.8,12.8,12.8,12.7,12.7,12.7,12.6,12.6],
3.00:[14.4,14.4,14.4,14.4,14.3,14.3,14.3,14.2,14.1],4.00:[15.4,15.4,15.3,15.3,15.2,15.1,15.1,14.9,14.8]}
tabla15_12_65 = {0.25:[5.1,5.1,5.0,5.0,4.8,4.7,4.7,4.5,4.4],0.50:[7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8,7.8],
0.75:[9.8,9.8,9.8,9.8,9.8,9.8,9.8,9.8,9.8],1.00:[10.4,10.4,10.4,10.4,10.5,10.4,10.4,10.3,10.2],
1.50:[12.0,12.0,12.0,12.0,11.9,11.9,11.9,11.8,11.7],2.00:[12.9,12.9,12.9,12.9,12.8,12.8,12.8,12.7,12.6],
3.00:[14.5,14.5,14.5,14.5,14.4,14.4,14.4,14.3,14.2],4.00:[15.4,15.4,15.4,15.4,15.3,15.3,15.3,15.2,15.1]}
#### Factor ET para camiones y pendientes menores a 3 #####

def factorET( volumen, pendiente):
    if pendiente <= 1 and volumen >100 and volumen <900:
        final = interpolacion(tabla15_11,tabla15_11x,volumen)
    elif pendiente <= 1 and volumen <= 100:
        final = tabla15_11x[0]
    elif pendiente <= 1 and volumen >= 900:
        final = tabla15_11x[8]
    elif pendiente <3 and volumen <= 100:
        final = tabla15_11x2[0]
    elif pendiente <3 and volumen >100 and volumen <900:
        final = interpolacion( tabla15_11,tabla15_11x2,volumen)
    elif pendiente <3 and volumen >= 900:
        final = tabla15_11x2[8]
    return final

def factorETpendientes(longitud, volumen, tabla):
    vars = puntos(longitud)
    if volumen <= 100:
        data1 = tabla.get(vars[0])[0]
        data2 = tabla.get(vars[1])[0]
        final = interpolacion([vars[0], vars[1]],[data1,data2],longitud)
        return final
    elif volumen >= 900:
        data1 = tabla.get(vars[0])[8]
        data2 = tabla.get(vars[1])[8]
        final = interpolacion([vars[0], vars[1]],[data1,data2],longitud)
        return final
    elif volumen >100 and volumen <900:
        data1 = interpolacion(tabla15_10, tabla.get(vars[0]),volumen)
        data2 = interpolacion(tabla15_10, tabla.get(vars[1]),volumen)
        final = interpolacion([vars[0],vars[1]],[data1,data2], longitud)
        return final

def factorETpendientes2(longitud, volumen, pendiente):
    if pendiente <3:
        final = factorET(volumen,pendiente)
    elif pendiente <3.5:
        final = factorETpendientes(longitud,volumen,tabla15_12_3_35)
    elif pendiente <4.5:
        final = factorETpendientes(longitud,volumen,tabla15_12_35_45)
    elif pendiente <5.5:
        final = factorETpendientes(longitud,volumen,tabla15_12_45_55)
    elif pendiente <6.5:
        final = factorETpendientes(longitud,volumen,tabla15_12_55_65)
    else:
        final = factorETpendientes(longitud,volumen,tabla15_12_65)
    return round(final,1)

##### Factor ET para volumen 1 y 2 ##

facET1 = factorETpendientes2(longitud_tramo, volumen1, pendiente_tramo)
facET2 = factorETpendientes2(longitud_tramo, volumen2, pendiente_tramo)


##### Factor ER para terrenos planos y pendientes menores a 3
tabla15_13_3_35 = {0.0:[1.1,1.1,1.1,1.0,1.0,1.0,1.0,1.0,1.0],0.25:[1.2,1.2,1.1,1.1,1.0,1.0,1.0,1.0,1.0],
0.75:[1.3,1.2,1.2,1.1,1.0,1.0,1.0,1.0,1.0],1.25:[1.4,1.3,1.2,1.1,1.0,1.0,1.0,1.0,1.0],2.25:[1.5,1.4,1.3,1.2,1.0,1.0,1.0,1.0,1.0]}
tabla15_13_35_45 = {0.0:[1.3,1.2,1.2,1.1,1.0,1.0,1.0,1.0,1.0],0.75:[1.4,1.3,1.2,1.1,1.0,1.0,1.0,1.0,1.0],
3.50:[1.5,1.4,1.3,1.2,1.0,1.0,1.0,1.0,1.0]}
tabla15_13_45_55 = {0.0:[1.5,1.4,1.3,1.2,1.0,1.0,1.0,1.0,1.0],2.50:[1.6,1.5,1.4,1.2,1.0,1.0,1.0,1.0,1.0]}
tabla15_13_55_65 = {0.0:[1.5,1.4,1.3,1.1,1.0,1.0,1.0,1.0,1.0],0.75:[1.6,1.5,1.4,1.2,1.0,1.0,1.0,1.0,1.0],
2.50:[1.6,1.5,1.4,1.3,1.2,1.1,1.0,1.0,1.0],3.50:[1.6,1.6,1.6,1.5,1.5,1.4,1.3,1.2,1.1]}
tabla15_13_65 = {0.0:[1.6,1.5,1.4,1.2,1.0,1.0,1.0,1.0,1.0],2.50:[1.6,1.5,1.4,1.2,1.3,1.3,1.3,1.3,1.3],3.50:[1.6,1.6,1.6,1.5,1.5,1.5,1.4,1.4,1.4]}

def factorER(pendiente):
    if pendiente <= 1:
        final = 1.0
    elif pendiente <3:
        final = 1.1

def factorERpendientes30(longitud, volumen):
    if longitud <= 0.25:
        if volumen <= 100:
            final = tabla15_13_3_35.get(0.0)[0]
        elif volumen >= 900:
            final = tabla15_13_3_35.get(0.0)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_3_35.get(0.0),volumen)
    elif longitud <= 0.75:
        if volumen <= 100:
            final = tabla15_13_3_35.get(0.25)[0]
        elif volumen >= 900:
            final = tabla15_13_3_35.get(0.25)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_3_35.get(0.25),volumen)
    elif longitud <= 1.25:
        if volumen <= 100:
            final = tabla15_13_3_35.get(0.75)[0]
        elif volumen >= 900:
            final = tabla15_13_3_35.get(0.75)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_3_35.get(0.75),volumen)
    elif longitud <= 2.25:
        if volumen <= 100:
            final = tabla15_13_3_35.get(1.25)[0]
        elif volumen >= 900:
            final = tabla15_13_3_35.get(1.25)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_3_35.get(1.25),volumen)
    elif longitud > 2.25:
        if volumen <= 100:
            final = tabla15_13_3_35.get(2.25)[0]
        elif volumen >= 900:
            final = tabla15_13_3_35.get(2.25)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_3_35.get(2.25),volumen)
    return round(final,1)

def factorERpendientes35(longitud,volumen):
    if longitud <= 0.75:
        if volumen <= 100:
            final = tabla15_13_35_45.get(0.0)[0]
        elif volumen >= 900:
            final = tabla15_13_35_45.get(0.0)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_35_45.get(0.0),volumen)
    elif longitud <= 3.50:
        if volumen <= 100:
            final = tabla15_13_35_45.get(0.75)[0]
        elif volumen >= 900:
            final = tabla15_13_35_45.get(0.75)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_35_45.get(0.75),volumen)
    else:
        if volumen <= 100:
            final = tabla15_13_35_45.get(3.50)[0]
        elif volumen >= 900:
            final = tabla15_13_35_45.get(3.50)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_35_45.get(3.50),volumen)
    
    return round(final,1)

def factorERpendientes45(longitud,volumen):
    if longitud <= 2.50:
        if volumen <= 100:
            final = tabla15_13_45_55.get(0.0)[0]
        elif volumen >= 900:
            final = tabla15_13_45_55.get(0.0)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_45_55.get(0.0),volumen)
    else: 
        if volumen <= 100:
            final = tabla15_13_45_55.get(2.50)[0]
        elif volumen >= 900:
            final = tabla15_13_45_55.get(2.50)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_45_55.get(2.50),volumen)
    return round(final,1)

def factorERpendientes55(longitud,volumen):
    if longitud <= 0.75:
        if volumen <= 100:
            final = tabla15_13_55_65.get(0.0)[0]
        elif volumen >= 900:
            final = tabla15_13_55_65.get(0.0)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_55_65.get(0.0),volumen)
    elif longitud <= 2.50:
        if volumen <= 100:
            final = tabla15_13_55_65.get(0.75)[0]
        elif volumen >= 900:
            final = tabla15_13_55_65.get(0.75)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_55_65.get(0.75),volumen)
    elif longitud <= 3.50:
        if volumen <= 100:
            final = tabla15_13_55_65.get(2.50)[0]
        elif volumen >= 900:
            final = tabla15_13_55_65.get(2.50)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_55_65.get(2.50),volumen)
    else:
        if volumen <= 100:
            final = tabla15_13_55_65.get(3.50)[0]
        elif volumen >= 900:
            final = tabla15_13_55_65.get(3.50)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_55_65.get(3.50),volumen)
    return round(final,1)

def factorERpendientes65(longitud,volumen):
    if longitud <= 2.50:
        if volumen <= 100:
            final = tabla15_13_65.get(0.0)[0]
        elif volumen >= 900:
            final = tabla15_13_65.get(0.0)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_65.get(0.0),volumen)
    elif longitud <= 3.50:
        if volumen <= 100:
            final = tabla15_13_65.get(2.50)[0]
        elif volumen >= 900:
            final = tabla15_13_65.get(2.50)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_65.get(2.50),volumen)

    else:
        if volumen <= 100:
            final = tabla15_13_65.get(3.50)[0]
        elif volumen >= 900:
            final = tabla15_13_65.get(3.50)[8]
        else:
            final = interpolacion(tabla15_11, tabla15_13_65.get(3.50),volumen)
    return round(final,1)

def factorERfinal(pendiente, longitud, volumen):
    if pendiente <3:
        final = factorER(pendiente)
    elif pendiente <3.5:
        final = factorERpendientes30(longitud, volumen)
    elif pendiente <4.5:
        final = factorERpendientes35(longitud, volumen)
    elif pendiente <5.5:
        final = factorERpendientes45(longitud, volumen)
    elif pendiente <6.5:
        final = factorERpendientes55(longitud, volumen)
    else:
        final = factorERpendientes65(longitud, volumen)
    return final


## Factores finales por vehiculos recreativos según volumen #####
facER1 = factorERfinal(pendiente_tramo, longitud_tramo, volumen1)
facER2 = factorERfinal(pendiente_tramo, longitud_tramo, volumen2)

#### FHVATS para volumen 1 ###### ATS Heavy vehicle Adjustment Factor
p_camiones = p_pesados/100
p_recreativos = recreativos/100

fhv1 = round(1/(1+(p_camiones*(facET1-1))+(p_recreativos*(facER1-1))),2)
fhv2 = round(1/(1+(p_camiones*(facET2-1))+(p_recreativos*(facER2-1))),2)


#### Estimación de ATS (Velocidad de viaje promedio) ##### Paso requerido para clase I y III
### Factor de ajuste por zonas de no paso en el análisis de dirección #####

tabla_ffs65 = {100:[1.1,2.2,2.8,3.0,3.1],200:[2.2,3.3,3.9,4.0,4.2],400:[1.6,2.3,2.7,2.8,2.9],600:[1.4,1.5,1.7,1.9,2.0],800:[0.7,1.0,1.2,1.4,1.5],
1000:[0.6,0.8,1.1,1.1,1.2],1200:[0.6,0.8,0.9,1.0,1.1],1200:[0.6,0.8,0.9,1.0,1.1],1400:[0.6,0.7,0.9,0.9,0.9],1600:[0.6,0.7,0.7,0.7,0.8]}
tabla_ffs60 = {100:[0.7,1.7,2.5,2.8,2.9],200:[1.9,2.9,3.7,4.0,4.2],400:[1.4,2.0,2.5,2.7,3.9],600:[1.1,1.3,1.6,1.9,2.0],800:[0.6,0.9,1.1,1.3,1.4],
1000:[0.6,0.7,0.9,1.1,1.2],1200:[0.5,0.7,0.9,0.9,1.1],1400:[0.5,0.6,0.8,0.8,0.9],1600:[0.5,0.6,0.7,0.7,0.7]}
tabla_ffs55 = {100:[0.5,1.2,2.2,2.6,2.7],200:[1.5,2.4,3.5,3.9,4.1],400:[1.3,1.9,2.4,2.7,2.8],600:[0.9,1.1,1.6,1.8,1.9],800:[0.5,0.7,1.1,1.2,1.4],
1000:[0.5,0.6,0.8,0.9,1.1],1200:[0.5,0.6,0.7,0.9,1.0],1200:[0.5,0.6,0.7,0.9,1.0],1400:[0.5,0.6,0.7,0.7,0.9],1600:[0.5,0.6,0.6,0.6,0.7]}
tabla_ffs50 = {100:[0.2,0.7,1.9,2.4,2.5],200:[1.2,2.0,3.3,3.9,4.0],400:[1.1,1.6,2.2,2.6,2.7],600:[0.6,0.9,1.4,1.7,1.9],800:[0.4,0.6,0.9,1.2,1.3],
1000:[0.4,0.4,0.7,0.9,1.1],1200:[0.4,0.4,0.7,0.8,1.0],1200:[0.4,0.4,0.7,0.8,1.0],1400:[0.4,0.4,0.6,0.7,0.8],1600:[0.4,0.4,0.5,0.5,0.5]}
tabla_ffs45 = {100:[0.1,0.4,1.7,2.2,2.4],200:[0.9,1.6,3.1,3.8,4.0],400:[0.9,0.5,2.0,2.5,2.7],600:[0.4,0.3,1.3,1.7,1.8],800:[0.3,0.3,0.8,1.1,1.2],
1000:[0.3,0.3,0.6,0.8,1.1],1200:[0.3,0.3,0.6,0.7,1.0],1400:[0.3,0.3,0.6,0.6,0.7],1600:[0.3,0.3,0.4,0.4,0.6]}
datos_tabla_15_15 = [20,40,60,80,100]


volumenes = [100,200,400,600,800,1000,1200,1400,1600]
def puntos2(volumen):
    for element in volumenes:
        if volumen > element:
            var = element
            var1 = volumenes[(volumenes.index(element))+1]
    return(var,var1) 


def fnp_ats(vol_opposing, no_pase,tabla):
    if vol_opposing <= 100:
        final = interpolacion(datos_tabla_15_15, tabla.get(100), no_pase)
    elif vol_opposing >= 1600:
        final = interpolacion(datos_tabla_15_15, tabla.get(1600), no_pase)
    else:
        vars = puntos2(vol_opposing)
        data1 = interpolacion(datos_tabla_15_15,tabla.get(vars[0]),no_pase)
        data2 = interpolacion(datos_tabla_15_15,tabla.get(vars[1]),no_pase)
        final = interpolacion( [vars[0],vars[1]],[data1,data2],vol_opposing)
    return round(final,1)

def fns_ats_final(vol_opposing, no_pase,velocidad):
    if velocidad <= 45:
        final = fnp_ats(vol_opposing, no_pase, tabla_ffs45)
    elif velocidad <= 50:
        final = fnp_ats(vol_opposing, no_pase, tabla_ffs50)
    elif velocidad <= 55:
        final = fnp_ats(vol_opposing, no_pase, tabla_ffs55)
    elif velocidad < 65:
        final = fnp_ats(vol_opposing, no_pase, tabla_ffs60)
    elif velocidad >= 65:
        final = fnp_ats(vol_opposing, no_pase, tabla_ffs65)
    return final

### Volumenes ajustados para estimación de ATS ###
### Para volumen 1 ###

vol_ats1 = volumen1/(fhp*fgATS1*fhv1)
vol_ats2 = volumen2/(fhp*fgATS2*fhv2)


factor_fnp_ats1 = fns_ats_final(volumen2, p_no_rebase, vel_flujo_libre)
factor_fnp_ats2 = fns_ats_final(volumen1, p_no_rebase, vel_flujo_libre)


ATSd1 = round(vel_flujo_libre - 0.00776*(vol_ats1 + vol_ats2) - factor_fnp_ats1,2)
ATSd2 = round(vel_flujo_libre - 0.00776*(vol_ats1 + vol_ats2) - factor_fnp_ats2,2)

### Paso 5: Demand Adjustment for PTSF, este fáctor es utilizado para las clases I y II ###

tabla15_16 = [100,200,300,400,500,600,700,800,900]
tabla15_16x = [0.73,0.80,0.85,0.90,0.96,0.97,0.99,1.00,1.00]
## Factor por ajuste de pendiente fgPTSF ##
def factor_fgPTS(volumen, pendiente):
    if pendiente <= 1 or volumen >= 900:
        final = 1.0
    elif volumen <= 100:
        final = 0.73
    else:
        final = interpolacion(tabla15_16, tabla15_16x, volumen)
    return round(final,2)

tabla15_17_3_35 = {0.25:[1.00,0.99,0.97,0.96,0.92,0.92,0.92,0.92,0.92],0.50:[1.00,0.99,0.98,0.97,0.93,0.93,0.93,0.93,0.93],
0.75:[1.00,0.99,0.98,0.97,0.93,0.93,0.93,0.93,0.93],1.00:[1.00,0.99,0.98,0.97,0.93,0.93,0.93,0.93,0.93],1.50:[1.00,0.99,0.98,0.97,0.94,0.94,0.94,0.94,0.94],
2.00:[1.00,0.99,0.98,0.98,0.95,0.95,0.95,0.95,0.95],3.00:[1.00,1.00,0.99,0.99,0.97,0.97,0.97,0.96,0.96],4.00:[1.00,1.00,1.00,1.00,1.00,0.99,0.99,0.97,0.97]}
tabla15_17_35_45 = {0.25:[1.00,0.99,0.98,0.97,0.94,0.93,0.93,0.92,0.92],0.50:[1.00,1.00,0.99,0.99,0.97,0.97,0.97,0.96,0.95],
0.75:[1.00,1.00,0.99,0.99,0.97,0.97,0.97,0.96,0.96],1.00:[1.00,1.00,0.99,0.99,0.97,0.97,0.97,0.97,0.97],1.50:[1.00,1.00,0.99,0.99,0.97,0.97,0.97,0.97,0.97],
2.00:[1.00,1.00,0.99,0.99,0.98,0.98,0.98,0.98,0.98],3.00:[1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00],4.00:[1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00]}
tabla15_17_45_55 = {0.25:[1.00,1.00,1.00,1.00,1.00,0.99,0.99,0.97,0.97],0.50:[1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00,1.00]}
tabla15_17x = [100,200,300,400,500,600,700,800,900]
longitudes2 = [0.25,0.50,0.75,1.00,1.50,2.00,3.00,4.00]

def puntos3(longitud):
    for element in longitudes2:
        if longitud > element:
            var = element
            var1 = longitudes2[(longitudes2.index(element))+1]
    return(var,var1) 

def factor_fgPTS_pendientes(longitud, volumen, pendiente):
    if pendiente >= 3 and pendiente <3.5:
        if longitud <= 0.25:
            final = interpolacion(tabla15_17x,tabla15_17_3_35.get(0.25),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_17_3_35.get(4.00),volumen)
        else:
            vars = puntos3(longitud)
            data1 = interpolacion(tabla15_17x, tabla15_17_3_35.get(vars[0]),volumen)
            data2 = interpolacion(tabla15_17x, tabla15_17_3_35.get(vars[1]),volumen)
            final = interpolacion([vars[0],vars[1]],[data1,data2],longitud)
    elif pendiente >= 3.5 and pendiente <4.5:
        if longitud <= 0.25:
            final = interpolacion(tabla15_17x,tabla15_17_35_45.get(0.25),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_17_35_45.get(4.00),volumen)
        else:
            vars = puntos3(longitud)
            data1 = interpolacion(tabla15_17x, tabla15_17_35_45.get(vars[0]),volumen)
            data2 = interpolacion(tabla15_17x, tabla15_17_35_45.get(vars[1]),volumen)
            final = interpolacion([vars[0],vars[1]],[data1,data2],longitud)
    elif pendiente >= 4.5 and pendiente <5.5:
        if longitud <= 0.25:
            final = interpolacion(tabla15_17x, tabla15_17_45_55.get(0.25),volumen)
        elif longitud >= 0.50:
            final = interpolacion(tabla15_17x, tabla15_17_45_55.get(0.50),volumen)
        else:
            data1 = interpolacion(tabla15_17x, tabla15_17_45_55.get(0.25),volumen)
            data2 = interpolacion(tabla15_17x, tabla15_17_45_55.get(0.50),volumen)
            final = interpolacion([0.25,0.50],[data1,data2],longitud)
    else:
        final = 1.0
    return round(final,2)

def factorfgPTSF_final(pendiente, longitud, volumen):
    if pendiente <3:
        final = factor_fgPTS(volumen, pendiente)
    else:
        final = factor_fgPTS_pendientes(longitud, volumen, pendiente)
    return final

fg_PTSF1 = factorfgPTSF_final(pendiente_tramo, longitud_tramo, volumen1)
fg_PTSF2 = factorfgPTSF_final(pendiente_tramo, longitud_tramo, volumen2)
fg_PTSF_total = factorfgPTSF_final(pendiente_tramo, longitud_tramo, volumen_demanda)


##### PTSF Heavy Vehicle Adjustment Factor ####
tabla15_19_30_35 = {2.00:[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],3.00:[1.5,1.3,1.3,1.2,1.0,1.0,1.0,1.0,1.0],4.00:[1.6,1.4,1.3,1.3,1.0,1.0,1.0,1.0,1.0]}
tabla15_19_35_45 = {1.00:[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],1.50:[1.1,1.1,1.0,1.0,1.0,1.0,1.0,1.0,1.0],2.00:[1.6,1.3,1.0,1.0,1.0,1.0,1.0,1.0,1.0],
3.00:[1.8,1.4,1.1,1.2,1.2,1.2,1.2,1.2,1.2],4.00:[2.1,1.9,1.8,1.7,1.4,1.4,1.4,14,1.4]}
tabla15_19_45_55 = {1.00:[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],1.50:[1.1,1.1,1.1,1.2,1.2,1.2,1.2,1.2,1.2],2.00:[1.7,1.6,1.6,1.6,1.5,1.4,1.4,1.3,1.3],
3.00:[2.4,2.2,2.2,2.1,1.9,1.8,1.8,1.7,1.7],4.00:[3.5,3.1,2.9,2.7,2.1,2.0,2.0,1.8,1.8]}
tabla15_19_55_65 = {0.75:[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],1.00:[1.0,1.0,1.1,1.1,1.2,1.2,1.2,1.2,1.2],1.50:[1.5,1.5,1.5,1.6,1.6,1.6,1.6,1.6,1.6],
2.00:[1.9,1.9,1.9,1.9,1.9,1.9,1.9,1.8,1.8],3.00:[3.4,3.2,3.0,2.9,2.4,2.3,2.3,1.9,1.9],4.00:[4.5,4.1,3.9,3.7,2.9,2.7,2.6,2.0,2.0]}
tabla15_19_65 = {0.50:[1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0],0.75:[1.0,1.0,1.0,1.0,1.1,1.1,1.1,1.0,1.0],1.00:[1.3,1.3,1.3,1.4,1.4,1.5,1.5,1.4,1.4],
1.50:[2.1,2.1,2.1,2.1,2.0,2.0,2.0,2.0,2.0],2.00:[2.9,2.8,2.7,2.7,2.4,2.4,2.3,2.3,2.3],3.00:[4.2,3.9,3.7,3.6,3.0,2.8,2.7,2.2,2.2],4.00:[5.0,4.6,4.4,4.2,3.3,3.1,2.9,2.7,2.5]}


def puntos4(longitud,lista):
    var = 0
    var1 = 1
    for element in lista:
        if longitud > element and longitud < lista[(lista.index(element))+1]:
            var = element
            var1 = lista[(lista.index(element))+1]
    return(var,var1) 
print(puntos4(52,[10,20,30,40,50,60,70]))

def factorETptsf(pendiente, volumen):
    if pendiente <= 1:
        if volumen <= 100:
            final = 1.1
        elif volumen <= 900:
            final = 1.0
        else:
            final = interpolacion(tabla15_17x, [1.1,1.1,1.1,1.1,1.0,1.0,1.0,1.0,1.0],volumen)
    else:
        final= interpolacion(tabla15_17x, [1.9,1.8,1.7,1.6,1.4,1.2,1.0,1.0,1.0],volumen)
    return round(final,1)

def factorETptsf_pendientes(pendiente, longitud, volumen):
    if pendiente >= 3 and pendiente <3.5:
        if longitud <= 2.00:
            final = interpolacion(tabla15_17x,tabla15_19_30_35.get(2.00),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_19_30_35.get(2.00),volumen)
        elif longitud >2.0 and longitud <= 3.0:
            data1 = interpolacion(tabla15_17x,tabla15_19_30_35.get(2.00),volumen)
            data2 = interpolacion(tabla15_17x,tabla15_19_30_35.get(3.00),volumen)
            final = interpolacion([2.00,3.00],[data1,data2],longitud)
        else:
            data1 = interpolacion(tabla15_17x,tabla15_19_30_35.get(3.00),volumen)
            data2 = interpolacion(tabla15_17x,tabla15_19_30_35.get(4.00),volumen)
            final = interpolacion([3.00,4.00],[data1,data2],longitud)
    elif pendiente < 4.5:
        if longitud <= 1.00:
            final = interpolacion(tabla15_17x,tabla15_19_35_45.get(1.00),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_19_35_45.get(4.00),volumen)
        else:
            vars = puntos4(longitud,[1.00,1.50,2.00,3.00,4.00])
            data1 = interpolacion(tabla15_17x,tabla15_19_35_45.get(vars[0]),volumen)
            data2 = interpolacion(tabla15_17x,tabla15_19_35_45.get(vars[1]),volumen)
            final = interpolacion([vars[0],vars[1]],[data1,data2],longitud)
    elif pendiente < 5.5:
        if longitud <= 1.00:
            final = interpolacion(tabla15_17x,tabla15_19_45_55.get(1.00),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_19_45_55.get(4.00),volumen)
        else:
            vars = puntos4(longitud,[1.00,1.50,2.00,3.00,4.00])
            data1 = interpolacion(tabla15_17x,tabla15_19_45_55.get(vars[0]),volumen)
            data2 = interpolacion(tabla15_17x,tabla15_19_45_55.get(vars[1]),volumen)
            final = interpolacion([vars[0],vars[1]],[data1,data2],longitud)
    elif pendiente < 6.5:
        if longitud <= 1.00:
            final = interpolacion(tabla15_17x,tabla15_19_55_65.get(0.75),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_19_55_65.get(4.00),volumen)
        else:
            vars = puntos4(longitud,[0.75,1.00,1.50,2.00,3.00,4.00])
            data1 = interpolacion(tabla15_17x,tabla15_19_55_65.get(vars[0]),volumen)
            data2 = interpolacion(tabla15_17x,tabla15_19_55_65.get(vars[1]),volumen)
            final = interpolacion([vars[0],vars[1]],[data1,data2],longitud)
    else: 
        if longitud <= 1.00:
            final = interpolacion(tabla15_17x,tabla15_19_65.get(0.50),volumen)
        elif longitud >= 4.00:
            final = interpolacion(tabla15_17x,tabla15_19_65.get(4.00),volumen)
        else:
            vars = puntos4(longitud,[0.50,0.75,1.00,1.50,2.00,3.00,4.00])
            data1 = interpolacion(tabla15_17x,tabla15_19_65.get(vars[0]),volumen)
            data2 = interpolacion(tabla15_17x,tabla15_19_65.get(vars[1]),volumen)
            final = interpolacion([vars[0],vars[1]],[data1,data2],longitud)
    return round(final,1)

def factorETptsf_final(pendiente, longitud,volumen):
    if pendiente <3:
        final = factorETptsf(pendiente, volumen)
    else:
        final = factorETptsf_pendientes(pendiente, longitud,volumen)
    return final

ETptsf1 = factorETptsf_final(pendiente_tramo,longitud_tramo,volumen1)
ETptsf2 = factorETptsf_final(pendiente_tramo,longitud_tramo,volumen2)

## heavy vehicle adjustment factor for PTSF determination ###
fhvptsf1 = 1/(1+p_camiones*(ETptsf1-1)+p_recreativos*(1-1))
fhvptsf2 = 1/(1+p_camiones*(ETptsf2-1)+p_recreativos*(1-1))

## Demand flow rate i for determination of PTSF (pc/h) ###
vol_ptsf1 = volumen1/(fhp*fg_PTSF1*fhvptsf1)
vol_ptsf2 = volumen2/(fhp*fg_PTSF2*fhvptsf2)

###Estimación de PTSF para cada sentido ####

## Coeficientes a y b
tabla15_20 = [200,400,600,800,1000,1200,1400,1600]
tabla15_20a = [-0.0014,-0.0022,-0.0033,-0.0045,-0.0049,-0.0054,-0.0058,-0.0062]
tabla15_20a1 = [14,22,33,45,49,54,58,68]
tabla15_20b = [0.973,0.923,0.870,0.833,0.829,0.825,0.821,0.817]

def coeficientes(volumen):
    final1 = interpolacion(tabla15_20, tabla15_20a1,volumen)
    final1 = final1/-10000
    final2 = interpolacion(tabla15_20, tabla15_20b,volumen)
    return (round(final1,4),round(final2,3))

coef_1 = coeficientes(volumen1)
coef_2 = coeficientes(volumen2)

BTSF1 = round(100*(1-math.exp(coef_1[0]*(volumen1**coef_1[1]))),2)
BTSF2 = round(100*(1-math.exp(coef_1[0]*(volumen2**coef_2[1]))),2)


### Fáctor fnp
tabla15_21_50 = {200:[9.0,29.2,43.4,49.4,51.0,52.6],400:[16.2,41.0,54.2,61.6,63.8,65.8],600:[15.8,38.2,47.8,53.2,55.2,56.8],
800:[15.8,33.8,40.4,44.0,44.8,46.6],1400:[12.8,20.0,23.8,26.2,27.4,28.6],2000:[10.0,13.6,15.8,17.4,18.2,18.8],2600:[5.5,7.7,8.7,9.5,10.1,10.3],3200:[3.3,4.7,5.1,5.5,5.7,6.1]}
tabla15_21_60 = {200:[11.0,30.6,41.0,51.2,52.3,53.5],400:[14.6,36.1,44.8,53.4,55.0,56.3],600:[14.8,36.9,44.0,51.1,52.8,54.6],
800:[13.6,28.2,33.4,38.6,39.9,41.3],1400:[11.8,18.9,22.1,25.4,26.4,27.3],2000:[9.1,13.5,15.6,16.0,16.8,17.3],2600:[5.9,7.7,8.6,9.6,10.0,10.2]}
tabla15_21_70 = {200:[9.9,28.1,38.0,47.8,48.5,49.0],400:[10.6,30.3,38.6,46.7,47.7,48.8],600:[10.9,30.9,37.5,43.9,45.4,47.0],
800:[10.3,23.6,28.4,33.3,34.5,35.5],1400:[8.0,14.6,17.7,20.8,21.6,22.3],2000:[7.3,9.7,11.7,13.3,14.0,14.5]}
tabla15_21_80 = {200:[8.9,27.1,37.1,47.0,47.4,47.9],400:[6.6,26.1,34.5,42.7,43.5,44.1],600:[4.0,24.5,31.3,38.1,39.1,40.0],
800:[3.8,18.5,23.5,28.4,29.1,29.9],1400:[3.5,10.3,13.3,16.3,16.9,32.2],2000:[3.5,7.0,8.5,10.1,10.4,10.7]}
tabla15_21_90 = {200:[4.6,24.1,33.6,43.1,43.4,43.6],400:[0.0,20.2,28.3,36.3,36.7,37.0],600:[-3.1,16.8,23.5,30.1,30.6,31.1],
800:[-2.8,10.5,15.2,19.9,20.3,20.8],1400:[-1.2,5.5,8.3,11.0,11.5,11.9]}
tabla15_21x = [0,20,40,60,80,100]

def factornp(volumen, direccional, no_pase):
    if direccional <60:
        if volumen <= 200: 
            final = interpolacion(tabla15_21x, tabla15_21_50.get(200), no_pase)
        else:
            vars = puntos4(volumen,[200,400,600,800,1400,2000,2600,3200])
            data1 = interpolacion(tabla15_21x, tabla15_21_50.get(vars[0]), no_pase)
            data2 = interpolacion(tabla15_21x, tabla15_21_50.get(vars[1]), no_pase)
            final = interpolacion([vars[0], vars[1]],[data1,data2], volumen)
    elif direccional <70:
        if volumen <= 200: 
            final = interpolacion(tabla15_21x, tabla15_21_60.get(200), no_pase)
        else:
            vars = puntos4(volumen,[200,400,600,800,1400,2000,2600])
            data1 = interpolacion(tabla15_21x, tabla15_21_60.get(vars[0]), no_pase)
            data2 = interpolacion(tabla15_21x, tabla15_21_60.get(vars[1]), no_pase)
            final = interpolacion([vars[0], vars[1]],[data1,data2], volumen)
    elif direccional <80:
        if volumen <= 200: 
            final = interpolacion(tabla15_21x, tabla15_21_70.get(200), no_pase)
        else:
            vars = puntos4(volumen,[200,400,600,800,1400,2000])
            data1 = interpolacion(tabla15_21x, tabla15_21_70.get(vars[0]), no_pase)
            data2 = interpolacion(tabla15_21x, tabla15_21_70.get(vars[1]), no_pase)
            final = interpolacion([vars[0], vars[1]],[data1,data2], volumen)
    elif direccional <90:
        if volumen <= 200: 
            final = interpolacion(tabla15_21x, tabla15_21_80.get(200), no_pase)
        else:
            vars = puntos4(volumen,[200,400,600,800,1400,2000])
            data1 = interpolacion(tabla15_21x, tabla15_21_80.get(vars[0]), no_pase)
            data2 = interpolacion(tabla15_21x, tabla15_21_80.get(vars[1]), no_pase)
            final = interpolacion([vars[0], vars[1]],[data1,data2], volumen)
    elif direccional <100:
        if volumen <= 200: 
            final = interpolacion(tabla15_21x, tabla15_21_90.get(200), no_pase)
        else:
            vars = puntos4(volumen,[200,400,600,800,1400])
            data1 = interpolacion(tabla15_21x, tabla15_21_90.get(vars[0]), no_pase)
            data2 = interpolacion(tabla15_21x, tabla15_21_90.get(vars[1]), no_pase)
            final = interpolacion([vars[0], vars[1]],[data1,data2], volumen)
    return round(final,1)

fnp_ptsf = factornp(volumen_demanda, volumen_direccional, p_no_rebase)

ptsf1 = BTSF1+fnp_ptsf*(vol_ptsf1/(vol_ptsf1+vol_ptsf2))
ptsf2 = BTSF2+fnp_ptsf*(vol_ptsf2/(vol_ptsf1+vol_ptsf2))

#### Paso 7 Estimate the PFFS ###
PFFS1 = (ATSd1/vel_flujo_libre)*100
PFFS2 = (ATSd2/vel_flujo_libre)*100
print(PFFS1,PFFS2)
def nivel_servicio(clase,ats,ptsf,pffs):
    if clase == 1:
        if ats >55 or ptsf <= 35:
            final = "A"
        elif ats > 50 or ptsf >35:
            final = "B"
        elif ats > 45 or ptsf > 50:
            final = "C"
        elif ats > 40 or ptsf > 65:
            final = "D"
        elif  ats <= 40 or ptsf > 80:
            final = "E"
        else:
            final = "F"
    elif clase == 2:
        if ptsf <= 40:
            final = "A"
        elif ptsf >40 and ptsf <= 55:
            final = "B"
        elif ptsf >55 and ptsf <= 70:
            final = "C"
        elif ptsf >70 and ptsf <= 85:
            final = "D"
        elif ptsf > 85:
            final = "E"
    elif clase == 3:
        if pffs > 91.7:
            final = "A"
        elif pffs > 83.3 and pffs <= 91.7:
            final = "B"
        elif pffs > 75.0 and pffs <= 83.3:
            final = "C"
        elif pffs > 66.7 and pffs <= 75.0:
            final = "D"
        elif pffs <= 66.7:
            final = "E"
    return final
#Paso 8 - Nivel de Servicio - ####

level1 = (nivel_servicio(clase_autopista,ATSd1,ptsf1,PFFS1))
level2 = (nivel_servicio(clase_autopista,ATSd1,ptsf1,PFFS1))

def hcm2_final(clase,a_carril,a_berma,longitud,pendiente,velocidad,volumen_inicial,d_sentido,accesos,p_no_rebase,fhp,p_pesados,recreativos):
    clase = int(clase)
    a_carril = float(a_carril)
    a_berma = float(a_berma)
    longitud = float(longitud)
    pendiente = float(pendiente)
    velocidad = float(velocidad)
    volumen_inicial = int(volumen_inicial)
    d_sentido = float(d_sentido)
    FA = factor_accesos(accesos)
    Fls = factor_carril(a_carril, a_berma)
    bffs = velocidad
    vel_flujo_libre = bffs - FA - Fls   
    volumen1 = int(volumen_inicial*(d_sentido/100))
    volumen2 = volumen_inicial- volumen1
    volumen1 = float(volumen1)
    volumen2 = float(volumen2)
    fgATS1 = fgATS_pendientes2(longitud, volumen1, pendiente)
    fgATS2 = fgATS_pendientes2(longitud, volumen2, pendiente)
    facET1 = factorETpendientes2(longitud, volumen1, pendiente)
    facET2 = factorETpendientes2(longitud, volumen2, pendiente)
    facER1 = factorERfinal(pendiente, longitud, volumen1)
    facER2 = factorERfinal(pendiente, longitud, volumen2) 
    p_camiones = p_pesados/100
    p_recreativos = recreativos/100
    print("No encuentro el error")
    print(fhp)
    print("Nada aún")
    fhv1 = round(1/(1+(p_camiones*(facET1-1))+(p_recreativos*(facER1-1))),2)
    fhv2 = round(1/(1+(p_camiones*(facET2-1))+(p_recreativos*(facER2-1))),2)
    print(fhp,fgATS1,fhv1)
    vol_ats1 = volumen1/(fhp*fgATS1*fhv1)
    vol_ats2 = volumen2/(fhp*fgATS2*fhv2)
    factor_fnp_ats1 = fns_ats_final(volumen2, p_no_rebase, vel_flujo_libre)
    factor_fnp_ats2 = fns_ats_final(volumen1, p_no_rebase, vel_flujo_libre)
    ATSd1 = round(vel_flujo_libre - 0.00776*(vol_ats1 + vol_ats2) - factor_fnp_ats1,2)
    ATSd2 = round(vel_flujo_libre - 0.00776*(vol_ats1 + vol_ats2) - factor_fnp_ats2,2)
    fg_PTSF1 = factorfgPTSF_final(pendiente, longitud, volumen1)
    fg_PTSF2 = factorfgPTSF_final(pendiente, longitud, volumen2)
    ETptsf1 = factorETptsf_final(pendiente,longitud,volumen1)
    ETptsf2 = factorETptsf_final(pendiente,longitud,volumen2)
    fhvptsf1 = 1/(1+p_camiones*(ETptsf1-1)+p_recreativos*(1-1))
    fhvptsf2 = 1/(1+p_camiones*(ETptsf2-1)+p_recreativos*(1-1))
    vol_ptsf1 = volumen1/(fhp*fg_PTSF1*fhvptsf1)
    vol_ptsf2 = volumen2/(fhp*fg_PTSF2*fhvptsf2)
    coef_1 = coeficientes(volumen1)
    coef_2 = coeficientes(volumen2)
    BTSF1 = round(100*(1-math.exp(coef_1[0]*(volumen1**coef_1[1]))),2)
    BTSF2 = round(100*(1-math.exp(coef_1[0]*(volumen2**coef_2[1]))),2)
    fnp_ptsf = factornp(volumen_demanda, volumen_direccional, p_no_rebase)
    ptsf1 = round(BTSF1+fnp_ptsf*(vol_ptsf1/(vol_ptsf1+vol_ptsf2)),2)
    ptsf2 = round(BTSF2+fnp_ptsf*(vol_ptsf2/(vol_ptsf1+vol_ptsf2)),2)
    PFFS1 = round((ATSd1/vel_flujo_libre*100),2)
    PFFS2 = round((ATSd2/vel_flujo_libre*100),2)
    level1 = (nivel_servicio(clase,ATSd1,ptsf1,PFFS1))
    level2 = (nivel_servicio(clase,ATSd2,ptsf2,PFFS2))
    return (FA,Fls,bffs,vel_flujo_libre,volumen1,volumen2,fgATS1,fgATS2,facET1,facET2,facER1,facER2,p_camiones,p_recreativos,
    fhv1,fhv2,vol_ats1,vol_ats2,factor_fnp_ats1,factor_fnp_ats2,ATSd1,ATSd2,fg_PTSF1,fg_PTSF2,ETptsf1,ETptsf2,fhvptsf1,fhvptsf2,
    vol_ptsf1,vol_ptsf2,coef_1[0],coef_1[1],coef_2[0],coef_2[1],BTSF1,BTSF2,fnp_ptsf,ptsf1,ptsf2,PFFS1,PFFS2,level1,level2)


