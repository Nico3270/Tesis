from scipy.interpolate import lagrange, interp1d
import math

def interpolacion(x,y,z):
    y_interp = interp1d(x, y,fill_value="extrapolate")
    resultado = float(y_interp(z))
    return round(resultado,3)

resultado = interpolacion([0.0,0.5,1.0,1.5,2.0,3.0],[2.80,1.60,1.30,0.90,0.70,0.0],1.3)
print(resultado)