import multicarril as mp
from scipy.interpolate import interp1d

#Factor de corrección Ec, de equivalente camiones para descenso
def Ec_descenso(pendiente, p_camiones, longitud):
    pendiente = abs(pendiente)
    if pendiente < 8:
        pen_inf = (mp.intervalosp(pendiente))[0]
        pen_sup = (mp.intervalosp(pendiente))[1]
        if pendiente <= 2:
            Ec_desc = mp.interpolacion(mp.tabla_19x, mp.tabla_19[2].get(500), p_camiones)
        elif pendiente > 2 and longitud < 1000:
            fac_lon_inf = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_inf].get(500), p_camiones)
            fac_lon_sup = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_inf].get(1000), p_camiones)
            Ec_desc_inf = mp.interpolacion([500,1000],[fac_lon_inf, fac_lon_sup], longitud)
            fac_lon_inf = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_sup].get(500), p_camiones)
            fac_lon_sup = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_sup].get(1000), p_camiones)
            Ec_desc_sup = mp.interpolacion([500,1000],[fac_lon_inf, fac_lon_sup], longitud)
            Ec_desc = mp.interpolacion([pen_inf,pen_sup],[Ec_desc_inf,Ec_desc_sup], pendiente)
        elif pendiente > 2 and longitud > 1000:  
            longitud_inf = mp.intervalos2(longitud)[0]
            longitud_sup = mp.intervalos2(longitud)[1]
            fac_lon_inf = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_inf].get(longitud_inf), p_camiones)
            fac_lon_sup = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_inf].get(longitud_sup), p_camiones)
            Ec_desc_inf = mp.interpolacion([longitud_inf,longitud_sup],[fac_lon_inf, fac_lon_sup], longitud)
            fac_lon_inf1 = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_sup].get(longitud_inf), p_camiones)
            fac_lon_sup1 = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pen_sup].get(longitud_sup), p_camiones)
            Ec_desc_sup = mp.interpolacion([longitud_inf,longitud_sup],[fac_lon_inf1, fac_lon_sup1], longitud)
            Ec_desc = mp.interpolacion([pen_inf,pen_sup],[Ec_desc_inf,Ec_desc_sup], pendiente)
        return [Ec_desc, longitud_inf, longitud_sup, fac_lon_inf, fac_lon_sup, Ec_desc_inf,fac_lon_inf1, fac_lon_sup1,Ec_desc_sup,mp.tabla_19[pen_inf].get(longitud_inf), mp.tabla_19[pen_sup].get(longitud_sup)]   
    if pendiente == 8 and longitud <= 1000:
        fac_lon_inf = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pendiente].get(500), p_camiones)
        fac_lon_sup = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pendiente].get(1000), p_camiones)
        Ec_desc = mp.interpolacion([500,1000],[fac_lon_inf, fac_lon_sup], longitud)    
        return Ec_desc
    elif pendiente == 8 and longitud > 1000:
        longitud_inf = mp.intervalos2(longitud)[0]
        longitud_sup = mp.intervalos2(longitud)[1]
        fac_lon_inf = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pendiente].get(longitud_inf), p_camiones)
        fac_lon_sup = mp.interpolacion(mp.tabla_19x, mp.tabla_19[pendiente].get(longitud_sup), p_camiones)
        Ec_desc = mp.interpolacion([longitud_inf,longitud_sup],[fac_lon_inf, fac_lon_sup], longitud)
        return Ec_desc, longitud_inf, longitud_sup, fac_lon_inf, fac_lon_sup, Ec_desc_inf,fac_lon_inf1, fac_lon_sup1,Ec_desc_sup, mp.tabla_19[pen_inf], mp.tabla_19[pen_sup]    


print(Ec_descenso(6.2,42,3600))
fac_lon_inf = mp.interpolacion(mp.tabla_19x, mp.tabla_19[6].get(3000), 42)
datosx = mp.tabla_19x
datosy = mp.tabla_19[6].get(3000)
punto = 25
# print([mp.tabla_19x, mp.tabla_19[6].get(3000)])
print(fac_lon_inf)
print(datosx, datosy)

y_interp = interp1d(datosx, datosy)
print(y_interp(punto)) 