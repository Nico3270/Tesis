from scipy.interpolate import lagrange
tramos = 3
tabla_15 =[5,10,15,20]
tabla_15x =[3.0,6.4,11.0,17.4]
#Función tipo de terreno
def tipo_terreno(num):
    if num < 3:
        return "Terreno Plano"
    elif num < 5:
        return "Terreno Ondulado"
    else:
        return "Terreno Montañoso"

def interpolacion(x,y,z):
    p = lagrange(x,y)
    resultado = (z)
    return round(p(z),3)

def in_range(rango,numero):
    return numero in range(*rango)

#Para tramo generico
pendiente = 3
lon_tramo = 2.2
a_carril = 3.3
a_berma_der = 2.0
a_berma_izq = 1.0
acc_laterales = 6
vol_transito = 1850
fhp = 0.90
p_camiones = 30
num_carriles = 2

#Preguntar si tiene separador en caso de que si lo tenga ingresar cantidad
separador = True
lon_separador = 1.3

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
    if a_separador == 0.0:
        fs = 2.8
    elif a_separador == 0.5:
        fs = 1.6
    elif a_separador == 1.0:
        fs = 1.30
    elif a_separador == 1.5:
        fs = 0.90
    elif a_separador == 2.0:
        fs = 0.70
    else:
        fs = 0.0
    return fs

#Corrección por ancho promedio de bermas - Tabla 14 del Manual
def correccion_bermas(a_berma_der, a_berma_izq):
    a_bermas = (a_berma_der + a_berma_izq)/2
    fb = 0
    if a_bermas == 0.0:
        fb = 7.9
    elif a_bermas == 0.5:
        fb = 2.5
    elif a_bermas >= 1.0 and a_bermas <= 1.5:
        fb = 1.7
    elif a_bermas == 1.8:
        fb = 0.8
    elif a_bermas >= 2.0:
        fb = 0
    return fb

#Corrección por densidad de accesos - Tabla 15 del Manual

def correccion_accesos(puntos):
    fa = 0
    fa = interpolacion(tabla_15, tabla_15x,puntos)
    return fa
    
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

#Factor de corrección por camiones
#preguntar porcentaje camiones

fhv = round(1/((1+(p_camiones/100)*(Ec-1))),3)


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
    
final = n_servicio(densidad, Tipo)
print(f"El nivel de servicio es {final}")


