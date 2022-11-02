import numpy as np
import matplotlib.pyplot as plt
import main as mn
print(mn.datos)
lista1 = np.arange(0,2500)
def vel(vel, a, b, c, valor):
    res = vel-a*((valor/b)**c)
    return res
datos96 = []
datos90 = []
datos80 = []
datos70 = []
lista1 = np.arange(0,2500)
for element in lista1:
    res1 = vel(80,2.375,1036.550,2.044,element)
    res2= vel(70,5.497,692.345,1.010,element)
    res3= vel(96,4.609,1124.526,1.624,element)
    res4= vel(90,1.040,882.082,2.545,element)
    datos80.append(res1)
    datos70.append(res2)
    datos96.append(res3)
    datos90.append(res4)

plt.plot(lista1, datos96, color="black")
plt.plot(lista1, datos90, color="black")
plt.plot(lista1, datos80, color="black")
plt.plot(lista1, datos70, color="black")
plt.plot([0,600],[0,100])
plt.plot([0,1100],[0,100])
plt.plot([0,1600],[0,100])
plt.plot([0,2200],[0,100])
plt.plot([0,2300],[0,82])
plt.text(150.0,70.0,"70")
plt.text(150.0,80.0,"80")
plt.text(150.0,90.0,"90")
plt.text(150.0,96.0,"96")
plt.text(30.0,55.0,"Nivel A",weight="bold")
plt.text(400.0,60.0,"Nivel B",weight="bold")
plt.text(810.0,68.0,"Nivel C",weight="bold")
plt.text(1700.0,90.0,"Nivel D",weight="bold")
plt.text(2050.0,88.0,"Nivel E",weight="bold")
plt.scatter(1429,81, label="Resultado obtenido")
plt.ylim([0,100])
plt.xlim([0,2300])
plt.xlabel("Flujo vehicular, qp, (ades/hora/carril)")
plt.ylabel("Velocidad (km/h)")
plt.xticks(np.arange(0,2201,200))
plt.yticks(np.arange(0,101,10))
plt.legend(loc="lower right")
plt.grid()
plt.savefig("static/assets/img/sensibilidad/plot17.png")
plt.close()




