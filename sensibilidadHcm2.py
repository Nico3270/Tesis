import multicarril as mp
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
v3 = 0
import HCM_2carriles as hcm2

def sensibilidad_clase(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = [1,2,3]
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(element, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(element,a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la clase
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(clase, pffs_in,color="red" )
    plt.scatter(clase, ats_in, color="teal"  )
    plt.scatter(clase, ptsf_in, color="gold")
    plt.scatter(clase, vel_flujo_libre, color="mediumorchid")
    plt.axvline(clase,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Clase de la vía de dos carriles')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/clase_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la clase

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(clase, volumen_ats,color="red" )
    plt.scatter(clase, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(clase,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Clase de la vía de dos carriles')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/clase_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la clase

    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(clase, nivel,color="red" )
    plt.axvline(clase,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Clase de la vía de dos carriles')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/clase_nivel.png")
    plt.close()

def sensibilidad_carril(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(9,12,0.1)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, element, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,element, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el ancho de carril
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(a_carril, pffs_in,color="red" )
    plt.scatter(a_carril, ats_in, color="teal"  )
    plt.scatter(a_carril, ptsf_in, color="gold")
    plt.scatter(a_carril, vel_flujo_libre, color="mediumorchid")
    plt.axvline(a_carril,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de carril (pies)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/anchoCarril_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar el ancho de carril

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(a_carril, volumen_ats,color="red" )
    plt.scatter(a_carril, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(a_carril,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de carril (m)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/anchoCarril_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar el ancho de carril

    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(a_carril, nivel,color="red" )
    plt.axvline(a_carril,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de carril (pies)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/anchoCarril_nivel.png")
    plt.close()
    
def sensibilidad_berma(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0.05,8,0.2)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, element,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,a_carril, element,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el ancho de berma
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(a_berma, pffs_in,color="red" )
    plt.scatter(a_berma, ats_in, color="teal"  )
    plt.scatter(a_berma, ptsf_in, color="gold")
    plt.scatter(a_berma, vel_flujo_libre, color="mediumorchid")
    plt.axvline(a_berma,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de berma (pies)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/anchoBerma_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar el ancho de berma

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(a_berma, volumen_ats,color="red" )
    plt.scatter(a_berma, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(a_berma,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de berma (m)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/anchoBerma_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar el ancho de la berma

    plt.plot(lista, level ,color="red",label="Nivel de servicio")
    plt.scatter(a_berma, nivel,color="red" )
    plt.axvline(a_berma,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Ancho de berma (pies)')
    plt.ylabel('Nivel de servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/anchoBerma_nivel.png")
    plt.close()
   
def sensibilidad_longitud(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0.3,4,0.1)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma, element,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,a_carril, a_berma,element,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la longitud del tramo
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(longitud, pffs_in,color="red" )
    plt.scatter(longitud, ats_in, color="teal"  )
    plt.scatter(longitud, ptsf_in, color="gold")
    plt.scatter(longitud, vel_flujo_libre, color="mediumorchid")
    plt.axvline(longitud,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Longitud del tramo (millas)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/Longitud_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar la longitud del tramo

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(longitud, volumen_ats,color="red" )
    plt.scatter(longitud, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(longitud,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Longitud del tramo (millas)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/Longitud_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar la longitud del tramo

    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(longitud, nivel,color="red" )
    plt.axvline(longitud,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Longitud del tramo (millas)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/Longitud_nivel.png")
    plt.close()
  
def sensibilidad_pendiente(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0,12,0.5)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,element,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,a_carril, a_berma,longitud,asc_desc,element,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la pendiente
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(pendiente, pffs_in,color="red" )
    plt.scatter(pendiente, ats_in, color="teal"  )
    plt.scatter(pendiente, ptsf_in, color="gold")
    plt.scatter(pendiente, vel_flujo_libre, color="mediumorchid")
    plt.axvline(pendiente,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/pendiente_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar la pendiente

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(pendiente, volumen_ats,color="red" )
    plt.scatter(pendiente, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(pendiente,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/pendiente_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar la pendiente

    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(pendiente, nivel,color="red" )
    plt.axvline(pendiente,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Pendiente (%)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/pendiente_nivel.png")
    plt.close()
 
def sensibilidad_camiones(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0,50,2)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,element,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,element,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el porcentaje de camiones
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(p_camiones, pffs_in,color="red" )
    plt.scatter(p_camiones, ats_in, color="teal"  )
    plt.scatter(p_camiones, ptsf_in, color="gold")
    plt.scatter(p_camiones, vel_flujo_libre, color="mediumorchid")
    plt.axvline(p_camiones,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Porcentaje de Vehículos pesados (%)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/camiones_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar el porcentaje de vehículos pesados

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(p_camiones, volumen_ats,color="red" )
    plt.scatter(p_camiones, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(p_camiones,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Porcentaje de vehículos pesados (%)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/camiones_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar el porcentaje de vehículos pesados
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(p_camiones, nivel,color="red" )
    plt.axvline(p_camiones,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Porcentaje de vehículos pesados (%)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/camiones_nivel.png")
    plt.close()

def sensibilidad_recreativos(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0,50,2)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            element,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            element,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el porcentaje de vehículos recreativos
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(p_recreativos, pffs_in,color="red" )
    plt.scatter(p_recreativos, ats_in, color="teal"  )
    plt.scatter(p_recreativos, ptsf_in, color="gold")
    plt.scatter(p_recreativos, vel_flujo_libre, color="mediumorchid")
    plt.axvline(p_recreativos,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Porcentaje de Vehículos recreativos (%)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/recreativos_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el porcentaje de vehículos recreativos

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(p_recreativos, volumen_ats,color="red" )
    plt.scatter(p_recreativos, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(p_recreativos,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Porcentaje de Vehículos recreativos (%)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/recreativos_volumens.png")
    plt.close()
 
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el porcentaje de vehículos recreativos
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(p_recreativos, nivel,color="red" )
    plt.axvline(p_recreativos,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Porcentaje de Vehículos recreativos (%)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/recreativos_nivel.png")
    plt.close()


def sensibilidad_volumenAnalisis(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0,1000,10)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,element,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,element,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el volumen de análisis
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(vol_analisis, pffs_in,color="red" )
    plt.scatter(vol_analisis, ats_in, color="teal"  )
    plt.scatter(vol_analisis, ptsf_in, color="gold")
    plt.scatter(vol_analisis, vel_flujo_libre, color="mediumorchid")
    plt.axvline(vol_analisis,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volumen vehicular en sentido de análisis (veh/h)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/volumenAnalisis_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar el volumen vehicular en sentido de análisis

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(vol_analisis, volumen_ats,color="red" )
    plt.scatter(vol_analisis, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(vol_analisis,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volumen vehicular en sentido de análisis (veh/h)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/volumenAnalisis_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar el volumen vehicular en sentido de análisis
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(vol_analisis, nivel,color="red" )
    plt.axvline(vol_analisis,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volumen vehicular en sentido de análisis (veh/h)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/volumenAnalisis_nivel.png")
    plt.close()

def sensibilidad_volumenOpuesto(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0,700,10)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,element,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase,a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,element,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el volumen opuestp
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(vol_opuesto, pffs_in,color="red" )
    plt.scatter(vol_opuesto, ats_in, color="teal"  )
    plt.scatter(vol_opuesto, ptsf_in, color="gold")
    plt.scatter(vol_opuesto, vel_flujo_libre, color="mediumorchid")
    plt.axvline(vol_opuesto,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volumen vehicular en sentido contrario (veh/h)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/volumenOpuesto_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar el volumen vehicular en sentido de análisis

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(vol_opuesto, volumen_ats,color="red" )
    plt.scatter(vol_opuesto, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(vol_opuesto,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volumen vehicular en sentido contrario (veh/h)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/volumenOpuesto_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar el volumen vehicular en sentido de análisis
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(vol_opuesto, nivel,color="red" )
    plt.axvline(vol_opuesto,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Volumen vehicular en sentido contrario (veh/h)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/volumenOpuesto_nivel.png")
    plt.close()

def sensibilidad_velCampo(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(30,100,5)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,"Si", element,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,"Si", element,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la velocidad medida en campo
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(vel_campo, pffs_in,color="red" )
    plt.scatter(vel_campo, ats_in, color="teal"  )
    plt.scatter(vel_campo, ptsf_in, color="gold")
    plt.scatter(vel_campo, vel_flujo_libre, color="mediumorchid")
    plt.axvline(vel_campo,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Velocidad a flujo libre medida en campo (mi/h)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/velCampo_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar la velocidad medida en campo

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(vel_campo, volumen_ats,color="red" )
    plt.scatter(vel_campo, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(vel_campo,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Velocidad a flujo libre medida en campo (mi/h)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/velCampo_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar la velocidad medida en campo
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(vel_campo, nivel,color="red" )
    plt.axvline(vel_campo,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Velocidad a flujo libre medida en campo (mi/h)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/velCampo_nivel.png")
    plt.close()

def sensibilidad_velEstimada(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(30,100,5)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,element,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,"No", vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,element,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
            p_recreativos,"No", vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar la velocidad a flujo libre base
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(velocidad, pffs_in,color="red" )
    plt.scatter(velocidad, ats_in, color="teal"  )
    plt.scatter(velocidad, ptsf_in, color="gold")
    plt.scatter(velocidad, vel_flujo_libre, color="mediumorchid")
    plt.axvline(velocidad,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Velocidad a flujo libre base (mi/h)')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/velEstimada_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar la velocidad a flujo libre base

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(velocidad, volumen_ats,color="red" )
    plt.scatter(velocidad, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(velocidad,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Velocidad a flujo libre base (mi/h)')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/velEstimada_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar la velocidad a flujo libre base
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(velocidad, nivel,color="red" )
    plt.axvline(velocidad,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Velocidad a flujo libre base (mi/h)')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/velEstimada_nivel.png")
    plt.close()

def sensibilidad_accesos(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,accesos,p_no_rebase,fhp,p_camiones,
p_recreativos,opc_velocidad, vel_campo,camiones_freno,vel_flujo_libre, nivel, volumen_ats, ats_in, volumen_ptsf, ptsf_in, pffs_in):
    lista = np.arange(0,20,2)
    flujo_libre = []
    vol_ats = []
    ats = []
    vol_ptsf = []
    ptsf = []
    pffs =[]
    level = []
    for element in lista: 
        if asc_desc == "Ascenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,element,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
        elif asc_desc == "Descenso":
            datos = hcm2.hcm2_final_asc(clase, a_carril, a_berma,longitud,asc_desc,pendiente,velocidad,vol_analisis,vol_opuesto,element,p_no_rebase,fhp,p_camiones,
            p_recreativos,opc_velocidad, vel_campo,camiones_freno)
            flujo_libre.append(datos[3])
            vol_ats.append(datos[16])
            ats.append(datos[20])
            vol_ptsf.append(datos[28])
            ptsf.append(datos[37])
            pffs.append(datos[39])
            level.append(datos[41])
    
    #Grafica que presenta la variación de ATS - PFFS - PTSSF - Vel Flujo libre al modificar el número de accesos
    plt.plot(lista, pffs ,color="red",label="PFFS")
    plt.plot(lista, ats ,color="teal",label="ATS")
    plt.plot(lista, ptsf ,color="gold",label="PTSF")
    plt.plot(lista, flujo_libre ,color="mediumorchid",label="FFS")
    plt.scatter(accesos, pffs_in,color="red" )
    plt.scatter(accesos, ats_in, color="teal"  )
    plt.scatter(accesos, ptsf_in, color="gold")
    plt.scatter(accesos, vel_flujo_libre, color="mediumorchid")
    plt.axvline(accesos,color="k", ls="dotted")
    plt.axhline(pffs_in,color="red", ls="dotted")
    plt.axhline(ats_in,color="teal", ls="dotted")
    plt.axhline(ptsf_in,color="gold", ls="dotted")
    plt.axhline(vel_flujo_libre,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Accesos en ambos sentidos / milla')
    plt.ylabel('Velocidad (mi/h) - %')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/accesos_velocidades.png")
    plt.close()

    #Grafica que presenta la variación de volumenes ajustados  al modificar el número de accesos

    plt.plot(lista, vol_ats ,color="red",label="Volumen ATS")
    plt.plot(lista, vol_ptsf ,color="mediumorchid",label="Volumen PTSF")
    plt.scatter(accesos, volumen_ats,color="red" )
    plt.scatter(accesos, volumen_ptsf, color="mediumorchid"  )
    plt.axvline(accesos,color="k", ls="dotted")
    plt.axhline(volumen_ats,color="red", ls="dotted")
    plt.axhline(volumen_ptsf,color="mediumorchid", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Accesos en ambos sentidos / milla')
    plt.ylabel('Volumen ajustado (pc/h)')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/accesos_volumens.png")
    plt.close()
 
 #Grafica que presenta la variación del nivel de Servicio al modificar el número de accesos
    plt.plot(lista, level ,color="red",label="Nivel de Servicio")
    plt.scatter(accesos, nivel,color="red" )
    plt.axvline(accesos,color="k", ls="dotted")
    plt.axhline(nivel,color="red", ls="dotted")
    plt.legend()
    plt.grid(True)
    plt.xlabel('Accesos en ambos sentidos / milla')
    plt.ylabel('Nivel de Servicio')
    fig = plt.gcf()
    fig.subplots_adjust(right=0.98)
    fig.subplots_adjust(left=0.1)
    plt.savefig("static/assets/img/sensibilidadHcm2/acceos_nivel.png")
    plt.close()
        