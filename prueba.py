from scipy.interpolate import lagrange
tabla_13 = [0.0, 0.5, 1.0, 1.5, 2.0, 3.0]
tabla_13x = [2.8, 1.6, 1.3, 0.9, 0.7, 0]   

tabla_14 = [0, 0.5, 1.0, 1.5, 1.8, 2]
tabla_14x = [7.9, 2.5, 1.7, 1.7, 0.8, 0]

tabla_15 =[5,10,15,20]
tabla_15x =[3.0,6.4,11.0,17.4]

tabla_18_1 = [5, 10, 15, 20, 25, 30, 35, 40, 50]
tabla_18_1x = [2.8, 2.2, 2.1, 2.1, 1.9, 1.9, 1.9 ,1.8, 1.8]

tabla_18 = [{},{500:[3.0,2.4,2.2,2.1,2.0,1.9,1.9,1.8,1.8],1000:[2.8,2.5,2.3,2.2,2.1,2.0,2.0,1.9,1.8],
1500:[2.8,2.5,2.4,2.2,2.1,2.0,2.0,1.9,1.8], 2000:[2.8,2.6,2.4,2.3,2.2,2.0,2.0,1.9,1.8],
2500:[2.8,2.6,2.5,2.3,2.2,2.1,2.0,2.0,1.9], 3000:[2.8,2.7,2.5,2.3,2.2,2.1,2.1,2.0,1.9],
3500:[2.8,2.7,2.6,2.3,2.2,2.1,2.1,2.0,1.9], 4000:[2.8,2.8,2.6,2.4,2.3,2.1,2.1,2.0,1.9],
5000:[2.8,2.8,2.7,2.4,2.3,2.1,2.1,2.0,1.9], 6000:[2.8,2.9,2.7,2.4,2.3,2.2,2.1,2.0,1.9],
6000:[2.9,2.9,2.7,2.4,2.3,2.2,2.1,2.0,1.9], 7000:[2.9,2.9,2.7,2.4,2.3,2.2,2.1,2.0,1.9],
7000:[2.9,2.9,2.7,2.4,2.3,2.2,2.1,2.0,1.9], 8000:[3.0,3.0,2.8,2.5,2.3,2.2,2.1,2.0,1.9]},
{500:[3.1,2.4,2.3,2.1,2.0,1.9,1.9,1.9,1.8], 1000:[3.0,2.4,2.4,2.3,2.1,2.0,2.0,1.9,1.9],
1500:[3.2,2.5,2.5,2.3,2.2,2.1,2.1,2.0,1.9], 2000:[3.2,2.6,2.6,2.4,2.2,2.1,2.1,2.0,1.9],
2000:[3.2,2.6,2.6,2.4,2.2,2.1,2.1,2.0,1.9], 2500:[3.3,2.6,2.7,2.5,2.3,2.2,2.1,2.1,2.0],
3000:[3.4,2.7,2.7,2.5,2.3,2.2,2.2,2.1,2.0], 3500:[3.4,2.8,2.8,2.6,2.4,2.3,2.2,2.1,2.0],
4000:[3.4,2.9,2.9,2.6,2.4,2.3,2.2,2.1,2.0], 5000:[3.5,3.0,3.0,2.7,2.5,2.3,2.2,2.1,2.0],
6000:[3.6,3.1,3.1,2.8,2.5,2.4,2.3,2.2,2.0], 7000:[3.7,3.3,3.1,2.8,2.5,2.4,2.3,2.2,2.0],
8000:[3.8,3.4,3.2,2.8,2.5,2.4,2.3,2.2,2.0]},
{500:[3.1,2.4,2.3,2.2,2.1,2.0,1.9,1.9,1.8], 1000:[3.2,2.6,2.4,2.3,2.2,2.1,2.0,1.9,1.9],
1500:[3.4,2.7,2.6,2.4,2.3,2.2,2.1,2.0,1.9], 2000:[3.5,2.8,2.7,2.5,2.3,2.3,2.1,2.0,2.0],
2500:[3.6,2.9,2.8,2.6,2.4,2.3,2.2,2.1,2.0], 3000:[3.7,3.1,2.9,2.6,2.5,2.4,2.2,2.1,2.1],
3500:[3.8,3.2,3.0,2.7,2.5,2.4,2.3,2.2,2.1], 4000:[3.9,3.3,3.1,2.8,2.6,2.5,2.3,2.2,2.1],
5000:[4.1,3.5,3.3,2.9,2.7,2.5,2.4,2.3,2.1], 6000:[4.2,3.7,3.4,3.0,2.7,2.6,2.4,2.3,2.2],
7000:[4.4,3.8,3.5,3.1,2.8,2.6,2.5,2.3,2.2], 8000:[4.5,4.0,3.6,3.1,2.8,2.6,2.5,2.3,2.2]},
{500:[3.1,2.4,2.3,2.2,2.1,2.0,1.9,1.9,1.8], 1000:[3.2,2.6,2.4,2.3,2.2,2.1,2.0,1.9,1.9],
1500:[3.4,2.7,2.6,2.4,2.3,2.2,2.1,2.0,1.9], 2000:[3.5,2.8,2.7,2.5,2.3,2.3,2.1,2.0,2.0],
2500:[3.6,2.9,2.8,2.6,2.4,2.3,2.2,2.1,2.0], 3000:[3.7,3.4,3.0,2.8,2.6,2.5,2.4,2.3,2.2],
3500:[3.8,3.6,3.2,2.9,2.7,2.6,2.5,2.4,2.2], 4000:[4.0,3.7,3.3,3.0,2.8,2.7,2.5,2.4,2.3],
5000:[4.4,4.0,3.5,3.1,2.9,2.8,2.6,2.5,2.3], 6000:[4.7,4.2,3.8,3.3,3.1,2.9,2.7,2.6,2.4],
7000:[5.0,4.3,3.9,3.4,3.1,2.9,2.8,2.6,2.4], 8000:[5.3,4.5,4.1,3.5,3.2,3.0,2.8,2.7,2.4]},
{500:[3.1,2.4,2.3,2.2,2.1,2.0,1.9,1.9,1.8], 1000:[3.2,2.6,2.4,2.3,2.2,2.1,2.0,1.9,1.9],
1500:[3.4,2.7,2.6,2.4,2.3,2.2,2.1,2.0,1.9], 2000:[3.5,2.8,2.7,2.5,2.3,2.3,2.1,2.0,2.0],
2500:[3.6,2.9,2.8,2.6,2.4,2.3,2.2,2.1,2.0], 3000:[3.7,3.4,3.0,2.8,2.6,2.5,2.4,2.3,2.2],
3500:[4.3,3.8,3.5,3.1,3.0,2.7,2.7,2.5,2.4], 4000:[4.6,3.9,3.6,3.3,3.1,2.8,2.8,2.6,2.4],
5000:[5.1,4.2,3.9,3.5,3.3,3.0,2.9,2.7,2.5], 6000:[5.6,4.5,4.1,3.7,3.5,3.1,3.1,2.8,2.6],
7000:[6.2,4.8,4.3,3.8,3.6,3.2,3.1,2.9,2.6], 8000:[6.8,5.0,4.5,4.0,3.7,3.3,3.2,3.0,2.7]},
{500:[3.5,2.7,2.3,2.2,2.1,2.1,2.0,1.9,1.9], 1000:[3.5,2.9,2.5,2.4,2.3,2.3,2.1,2.1,2.0],
1500:[3.6,3.1,2.7,2.5,2.5,2.4,2.3,2.2,2.1], 2000:[3.9,3.3,2.9,2.7,2.6,2.6,2.4,2.4,2.2],
2500:[4.3,3.5,3.2,2.9,2.8,2.7,2.5,2.5,2.3], 3000:[4.7,3.7,3.4,3.1,3.0,2.9,2.7,2.6,2.4],
3500:[5.0,4.0,3.7,3.3,3.1,3.0,2.8,2.7,2.5], 4000:[5.2,4.2,3.9,3.4,3.3,3.2,2.9,2.9,2.6],
5000:[5.7,4.7,4.3,3.8,3.5,3.4,3.1,3.0,2.7], 6000:[5.2,5.1,4.6,4.0,3.7,3.6,3.3,3.2,2.8],
7000:[6.7,5.4,4.9,4.2,3.9,3.7,3.4,3.3,2.9], 8000:[7.1,5.6,5.1,4.4,4.0,3.8,3.5,3.3,2.9]},
{500:[3.5,2.7,2.5,2.4,2.2,2.2,2.1,2.0,1.9], 1000:[3.6,3.0,2.8,2.6,2.4,2.4,2.2,2.2,2.0],
1500:[4.0,3.3,3.0,2.8,2.6,2.6,2.4,2.3,2.2], 2000:[4.4,3.6,3.3,3.1,2.8,2.8,2.5,2.5,2.3],
2500:[4.9,4.0,3.6,3.3,3.0,3.0,2.7,2.6,2.5], 3000:[5.3,4.3,3.9,3.6,3.2,3.2,2.9,2.8,2.6],
3500:[5.8,4.7,4.2,3.8,3.4,3.3,3.0,2.9,2.7], 4000:[6.2,5.0,4.4,4.0,3.6,3.5,3.2,3.1,2.9],
5000:[6.9,5.6,5.0,4.4,4.0,3.8,3.5,3.4,3.1], 6000:[7.4,6.1,5.4,4.7,4.2,4.0,3.7,3.5,3.2],
7000:[7.9,6.5,5.7,5.0,4.4,4.1,3.8,3.7,3.3], 8000:[8.5,6.9,6.0,5.1,4.5,4.3,3.9,3.7,3.4]},
{500:[3.3,3.1,2.8,2.4,2.3,2.2,2.1,2.0,1.9], 1000:[3.6,3.5,3.0,2.6,2.5,2.4,2.3,2.2,2.1],
1500:[4.2,3.8,3.3,2.8,2.7,2.6,2.5,2.4,2.3], 2000:[4.8,4.1,3.5,3.0,2.9,2.8,2.8,2.6,2.5],
2500:[5.4,4.4,3.8,3.2,3.1,3.1,3.0,2.8,2.7], 3000:[6.0,4.8,4.2,3.5,3.4,3.4,3.3,3.0,2.8],
3500:[6.6,5.2,4.6,3.8,3.7,3.6,3.5,3.3,3.0], 4000:[7.2,5.6,4.9,4.1,4.0,3.8,3.7,3.4,3.2],
5000:[8.1,6.3,5.6,4.6,4.4,4.2,4.1,3.7,3.4], 6000:[8.7,6.9,6.0,4.9,4.7,4.5,4.3,3.9,3.6],
7000:[9.2,7.4,6.3,5.2,4.9,4.6,4.4,4.1,3.7], 8000:[9.7,7.6,6.5,5.4,4.9,4.8,4.5,4.2,3.7]}]
tabla_18x = [5, 10, 15, 20, 25, 30, 35, 40, 50]

tabla_19 =[{}, {}, {500:[3.0,2.5,2.4,2.4,2.2,2.1,2.0,1.9], 1000:[3.1,2.6,2.5,2.4,2.2,2.1,2.0,1.9],
2000:[2.9,2.5,2.4,2.4,2.2,2.0,2.0,1.9], 3000:[2.9,2.5,2.3,2.3,2.1,2.0,2.0,1.9],
4000:[2.9,2.5,2.3,2.3,2.1,2.0,2.0,1.9], 5000:[3.1,2.5,2.3,2.2,2.0,1.9,1.9,1.8],
6000:[3.5,3.3,3.2,2.8,2.5,2.5,2.3,2.1], 7000:[3.4,3.2,3.2,2.7,2.5,2.5,2.3,2.1],
8000:[3.4,3.2,3.1,2.7,2.5,2.4,2.3,2.1], 9000:[3.3,3.1,3.1,2.7,2.5,2.4,2.2,2.1]},
{500:[3.2,3.0,3.0,2.6,2.8,2.2,2.1,2.0], 1000:[3.3,2.6,2.6,2.4,2.2,2.2,2.1,2.0],
2000:[3.3,2.6,2.5,2.4,2.2,2.2,2.1,1.9], 3000:[3.2,2.6,2.5,2.3,2.2,2.2,2.1,1.9],
4000:[3.1,2.5,2.4,2.3,2.2,2.1,2.0,1.9], 5000:[3.5,2.7,2.4,2.3,2.1,2.0,1.9,1.9],
6000:[4.6,4.3,3.8,3.1,2.9,2.8,2.6,2.4], 7000:[4.5,4.2,3.7,3.1,2.9,2.7,2.6,2.4],
8000:[4.4,4.0,3.6,3.0,2.9,2.7,2.6,2.4], 9000:[4.3,3.9,3.5,3.0,2.8,2.7,2.6,2.3]},
{500:[3.6,2.8,2.7,2.6,2.3,2.3,2.1,2.0], 1000:[3.6,2.9,2.7,2.7,2.3,2.3,2.1,2.0],
2000:[3.7,2.9,2.7,2.6,2.3,2.3,2.1,2.0], 3000:[3.6,2.9,2.7,2.6,2.3,2.2,2.1,2.0],
4000:[3.5,2.8,2.6,2.5,2.2,2.2,2.1,2.0], 5000:[3.7,3.0,2.6,2.4,2.1,2.1,2.0,1.9],
6000:[5.4,5.0,4.4,3.9,3.3,3.1,2.8,2.6], 7000:[5.3,4.8,4.3,3.8,3.3,3.1,2.8,2.6],
8000:[5.2,4.6,4.1,3.7,3.2,3.0,2.8,2.6], 9000:[5.1,4.4,4.0,3.6,3.1,3.0,2.7,2.5]},
{500:[3.5,3.2,3.0,2.8,2.5,2.4,2.3,2.1], 1000:[3.5,3.2,3.0,2.9,2.5,2.4,2.3,2.1],
2000:[3.5,3.2,3.0,2.8,2.5,2.4,2.3,2.1], 3000:[3.4,3.1,2.9,2.7,2.4,2.3,2.2,2.1],
4000:[3.3,3.0,2.8,2.6,2.4,2.3,2.2,2.0], 5000:[3.7,3.1,2.7,2.5,2.2,2.2,2.1,1.9],
6000:[6.5,5.3,5.1,4.3,3.6,3.4,3.1,2.8], 7000:[6.5,5.1,4.9,4.3,3.6,3.3,3.0,2.7],
8000:[6.4,5.0,4.7,4.2,3.5,3.3,3.0,2.7], 9000:[6.1,4.8,4.5,4.1,3.4,3.2,2.9,2.6]},
{500:[3.7,3.3,3.2,2.9,2.7,2.5,2.4,2.2], 1000:[3.7,3.3,3.3,3.0,2.7,2.5,2.4,2.2],
2000:[3.6,3.3,3.2,2.9,2.7,2.5,2.4,2.2], 3000:[3.5,3.2,3.1,2.8,2.6,2.4,2.4,2.2],
4000:[3.5,3.1,3.0,2.7,2.5,2.4,2.3,2.1], 5000:[3.9,3.1,2.9,2.6,2.4,2.2,2.2,2.0],
6000:[7.6,6.7,5.2,4.9,3.7,3.5,3.2,2.8], 7000:[7.2,6.4,5.2,4.9,3.7,3.4,3.2,2.8],
8000:[7.1,6.3,5.0,4.7,3.6,3.3,3.2,2.8], 9000:[6.8,6.0,4.7,4.5,3.5,3.2,3.1,2.8]},
{500:[4.4,3.6,3.4,3.1,2.8,2.6,2.5,2.3], 1000:[4.5,3.6,3.4,3.1,2.8,2.6,2.5,2.3],
2000:[4.4,3.6,3.3,3.0,2.7,2.6,2.4,2.3], 3000:[4.2,3.4,3.2,2.9,2.7,2.5,2.4,2.2],
4000:[4.0,3.4,3.1,2.8,2.6,2.5,2.3,2.2], 5000:[4.3,3.5,3.0,2.7,2.4,2.3,2.2,2.1],
6000:[8.8,7.2,5.2,4.9,3.9,3.6,3.4,3.1], 7000:[8.6,6.9,5.1,4.7,4.0,3.6,3.5,3.1],
8000:[8.4,6.7,4.9,4.6,3.9,3.6,3.4,3.0], 9000:[8.0,6.4,4.7,4.4,3.7,3.4,3.3,3.0]},
{500:[4.2,3.7,3.7,3.3,2.9,2.7,2.6,2.4], 1000:[4.3,3.8,3.7,3.2,2.9,2.7,2.6,2.4],
2000:[4.2,3.7,3.6,3.2,2.9,2.7,2.6,2.3], 3000:[4.1,3.5,3.5,3.1,2.8,2.6,2.5,2.3],
4000:[3.9,3.4,3.3,3.0,2.7,2.5,2.5,2.3], 5000:[4.4,3.5,3.1,2.8,2.5,2.4,2.3,2.1],
6000:[9.8,7.1,5.7,4.9,4.0,3.8,3.6,3.3], 7000:[9.6,6.8,5.5,4.8,4.0,3.7,3.6,3.2],
8000:[9.4,6.6,5.3,4.7,4.0,3.7,3.6,3.2], 9000:[9.0,6.3,5.1,4.5,3.8,3.6,3.4,3.1]}]
tabla_19x = [5,10,15,20,30,35,40,50]

#Función tipo de terreno
def tipo_terreno(num):
    if num < 3:
        return "Terreno Plano"
    elif num < 5:
        return "Terreno Ondulado"
    else:
        return "Terreno Montañoso"

#Función de interpolación
def interpolacion(x,y,z):
    p = lagrange(x,y)
    resultado = (z)
    return round(p(z),3)

#Función que devuelve un Bool si un numero se encuentra dentro de un rango
def in_range(rango,numero):
    return numero in range(*rango)

#Función para determinar los limites inferior y superior, para la intrpolación Ec en tabla 18 para longitudes menores a 4000
def intervalos(num):
    inf = 0
    sup = 0
    list = [500,1000,1500,2000,2500,3000,3500,4000]
    for x in list:
        if num - x >=0 and num - x <= 500:
            inf = x
            sup= list[list.index(inf)+1]
    return(inf,sup)

#Función para determinar los limites inferior y superior, para la intrpolación Ec en tabla 18 para longitudes menores a 4000
def intervalos1(num):
    inf = 0
    sup = 0
    list = [4000,5000,6000,7000,8000]
    for x in list:
        if num - x >=0 and num - x <= 1000:
            inf = x
            sup= list[list.index(inf)+1]
    return(inf,sup)

#Función para determinar los limites inferior y superior, para la intrpolación Ec en tabla 19 para longitudes mayores a 1000
def intervalos2(num):
    inf = 0
    sup = 0
    list = [1000, 2000, 3000,4000,5000,6000,7000,8000,9000]
    for x in list:
        if num - x >=0 and num - x <= 1000:
            inf = x
            sup= list[list.index(inf)+1]
    return(inf,sup)

#Para tramo generico

pendiente = 4
a_carril = 3.3
a_berma_der = 2.0
a_berma_izq = 1.0
acc_laterales = 6
vol_transito = 1850
fhp = 0.90
p_camiones = 30
num_carriles = 2
longitud = 3000

#Opciones de los tramos (Generico, Ascenso, Descenso)
tramo = "Ascenso"

#Preguntar si tiene separador en caso de que si lo tenga ingresar cantidad
separador = True
lon_separador = 1.5
accesos = True
terreno = tipo_terreno(pendiente)

#Paso 2 - Estimación de Velocidad a flujo libre (VL)
#Preguntar la clasificación de la carretera multicarril - Tipo A1 - B1 - C1

#Función para calcular la velocidad generica
def Vl(Tipo, separador,accesos,peatones):
    vel_fl = 0
    if Tipo == "A1":
        vel_fl = 120
    elif Tipo == "B1" and separador == True and accesos == True:
        vel_fl = 100
    elif Tipo == "B1" and separador == False and accesos == True:
        vel_fl = 90
    elif Tipo == "B1" and separador == True and accesos == False:
        vel_fl = 90
    elif Tipo == "B1" and separador == False and accesos == False:
        vel_fl = 80
    elif Tipo == "C1" and separador == True and peatones == True:
        vel_fl = 70
    elif Tipo == "C1" and separador == False and peatones == True:
        vel_fl = 60
    elif Tipo == "C1" and separador == True and peatones == False:
        vel_fl = 80
    elif Tipo == "C1" and separador == False and peatones == False:
        vel_fl = 70
    return vel_fl
    
#Correcciones
#Corrección por ancho de carril - Tabla 12 del Manual
def correccion_carril(a_carril):
    fc = 0
    if a_carril == 3.0:
        fc = 14.8
    elif a_carril == 3.3:
        fc = 2.0
    elif a_carril == 3.5:
        fc = 0.0
    return fc

#Corrección por ancho de separador - Tabla 13 del Manual
def correccion_separador(a_separador):
    fs = 0
    if in_range([0,3], a_separador):
        fs = interpolacion(tabla_13, tabla_13x, a_separador)
    return fs
    
#Corrección por ancho promedio de bermas - Tabla 14 del Manual
def correccion_bermas(a_berma_der, a_berma_izq):
    a_bermas = (a_berma_der + a_berma_izq)/2
    fb = 0
    if in_range([0,2], a_bermas):
        fb = interpolacion(tabla_14, tabla_14x, a_bermas)   
    return fb


#Corrección por densidad de accesos - Tabla 15 del Manual

def correccion_accesos(puntos):
    fa = 0
    if puntos >= 20:
        fa = 17.4
    else:    
        fa = interpolacion(tabla_15, tabla_15x,puntos)
    return fa
print(correccion_accesos(0))

#Función final para determinar velocidad a flujo libre del sector de anáisis (VL)

def v_flujo_libre(Tipo, separador, accesos, peatones, a_carril, a_separador,a_berma_der,a_berma_izq, puntos):
    fc=0
    fs=0
    fb=0
    fa=0
    V_libre = 0
    vel_generica = Vl(Tipo, separador, accesos,peatones)
    fc = correccion_carril(a_carril)
    fs = correccion_separador(a_separador)
    fb = correccion_bermas(a_berma_der,a_berma_izq)
    fa = correccion_accesos(puntos)
    V_libre = vel_generica-fc-fs-fb-fa
    return V_libre

#Ejemplo de prueba
resultado = int(v_flujo_libre("B1", True, False, True, 3.3, 1.5,2.0,1.0,6))

#Selección de la curva maestra de referencia
def tipo(numero):
    if in_range([0,75],numero):
        tipo = "Tipo 4"
    elif in_range([75,85], numero):
        tipo = "Tipo 3"
    elif in_range([85,95],numero):
        tipo = "Tipo 2"
    else:
        tipo = "Tipo 1"
    if tipo == "Tipo 1":
        vel_f_libre = 96
        a = 4.609
        b = 1124.526
        c = 1.624
    elif tipo == "Tipo 2":
        vel_f_libre = 90
        a = 1.040
        b = 882.082
        c = 1036.550
        d = 692.345
    if tipo == "Tipo 3":
        vel_f_libre = 80
        a = 2.375
        b = 1036.550
        c = 2.044
    if tipo == "Tipo 4":
        vel_f_libre = 70
        a = 5.497
        b = 692.345
        c = 1.010
    return tipo, vel_f_libre, a, b, c

    
Tipo = tipo(resultado)[0]
vel_flujo_libre = tipo(resultado)[1]
a = tipo(resultado)[2]
b = tipo(resultado)[3]
c = tipo(resultado)[4]

#Cálculo del flujo vehicular - Paso 3
#Equivalente de camiones Ec

def Ec_generico():
    Ec = 0
    if terreno == "Terreno Plano":
        Ec = 1.8
    elif terreno == "Terreno Ondulado":
        Ec = 2.3
    elif terreno == "Terreno Montañoso":
        Ec = 4.4
    return Ec
Ec = Ec_generico()

#Factor de corrección por camiones - Equivalente de camiones Ec para tramos en ascenso
def Ec_ascenso(pendiente, p_camiones, longitud):
    if longitud >= 8000:
        longitud = 7999
    if pendiente < 1:
        Ec_asc = interpolacion(tabla_18_1, tabla_18_1x, p_camiones)
    elif pendiente >= 1 and longitud < 4000:
        longitud_inf = intervalos(longitud)[0]
        longitud_sup = intervalos(longitud)[1]
        fac_lon_inf = interpolacion(tabla_18x, tabla_18[pendiente].get(longitud_inf), p_camiones)
        fac_lon_sup = interpolacion(tabla_18x, tabla_18[pendiente].get(longitud_sup), p_camiones)
        Ec_asc = interpolacion([longitud_inf,longitud_sup],[fac_lon_inf, fac_lon_sup], longitud)
    elif pendiente >= 1 and longitud >= 4000:  
        longitud_inf = intervalos1(longitud)[0]
        longitud_sup = intervalos1(longitud)[1]
        fac_lon_inf = interpolacion(tabla_18x, tabla_18[pendiente].get(longitud_inf), p_camiones)
        fac_lon_sup = interpolacion(tabla_18x, tabla_18[pendiente].get(longitud_sup), p_camiones)
        Ec_asc = interpolacion([longitud_inf,longitud_sup],[fac_lon_inf, fac_lon_sup], longitud)
    return Ec_asc



#Factor de corrección Ec, de equivalente camiones para descenso
def Ec_descenso(pendiente, p_camiones, longitud):
    pendiente = abs(pendiente)
    if pendiente <= 2:
        Ec_desc = interpolacion(tabla_19x, tabla_19[2].get(500), p_camiones)
    elif pendiente > 2 and longitud < 1000:
        fac_lon_inf = interpolacion(tabla_19x, tabla_19[pendiente].get(500), p_camiones)
        fac_lon_sup = interpolacion(tabla_19x, tabla_19[pendiente].get(1000), p_camiones)
        Ec_desc = interpolacion([500,1000],[fac_lon_inf, fac_lon_sup], longitud)
    elif pendiente > 2 and longitud > 1000:  
        longitud_inf = intervalos2(longitud)[0]
        longitud_sup = intervalos2(longitud)[1]
        fac_lon_inf = interpolacion(tabla_19x, tabla_19[pendiente].get(longitud_inf), p_camiones)
        fac_lon_sup = interpolacion(tabla_19x, tabla_19[pendiente].get(longitud_sup), p_camiones)
        Ec_desc = interpolacion([longitud_inf,longitud_sup],[fac_lon_inf, fac_lon_sup], longitud)
    return Ec_desc 


Ec = 0
if tramo == "Generico":
    Ec = Ec_generico()
elif tramo == "Ascenso":
    Ec = Ec_ascenso(pendiente, p_camiones, longitud)

elif tramo == "Descenso":
    Ec = Ec_descenso(pendiente, p_camiones, longitud)
print("Resultado Ec")
print(Ec)

#preguntar porcentaje camiones

print(Ec)
fhv = round(1/((1+(p_camiones/100)*(Ec-1))),3)
print(fhv)
#Factor de conocimiento de la vía - Preguntar

fp = 1

#Flujo vehicular qp
qp = int(vol_transito/(fhp*num_carriles*fhv*fp))

print(qp)

#Paso 4 - Determinación de la velocidad de operación en el sector de análisis

v_densidad = round((vel_flujo_libre - a*((qp/b)**c)),1)

#Paso 5 - Cálculo de la densidad 

densidad = round((qp/v_densidad),2)

def n_servicio(densidad):
    if Tipo == "Tipo 1" or Tipo == "Tipo 2":
        if densidad <= 6:
            ns = "A"
        elif densidad >6 and densidad <= 11:
            ns = "B"
        elif densidad >11 and densidad <= 16:
            ns = "C"
        elif densidad >16 and densidad <= 22:
            ns = "D"
        elif densidad >22 and densidad <= 28:
            ns = "E"
        else: 
            ns = "F"
    elif Tipo == "Tipo 3":
        if densidad <= 7:
            ns = "A"
        elif densidad >7 and densidad <= 12:
            ns = "B"
        elif densidad >12 and densidad <= 18:
            ns = "C"
        elif densidad >18 and densidad <= 25:
            ns = "D"
        elif densidad >25 and densidad <= 31:
            ns = "E"
        else: 
            ns = "F"
    elif Tipo == "Tipo 4":
        if densidad <= 8:
            ns = "A"
        elif densidad >8 and densidad <= 15:
            ns = "B"
        elif densidad >15 and densidad <= 23:
            ns = "C"
        elif densidad >23 and densidad <= 32:
            ns = "D"
        elif densidad >32 and densidad <= 40:
            ns = "E"
        else: 
            ns = "F"
    return ns
print(densidad)
final = n_servicio(densidad)
print(f"El nivel de servicio es {final}")


