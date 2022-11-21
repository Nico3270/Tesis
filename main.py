from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange,  URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import capacidad_NS as cap
import multicarril as mp
import Sensibilidad as sen
import numpy as np
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
ckeditor = CKEditor(app)

#Creando base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///capacidad.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONNECT TO db_blog
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_blog = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db_blog.Model):
    id = db_blog.Column(db_blog.Integer, primary_key=True)
    title = db_blog.Column(db_blog.String(250), unique=True, nullable=False)
    subtitle = db_blog.Column(db_blog.String(250), nullable=False)
    date = db_blog.Column(db_blog.String(250), nullable=False)
    body = db_blog.Column(db_blog.Text, nullable=False)
    author = db_blog.Column(db_blog.String(250), nullable=False)
    img_url = db_blog.Column(db_blog.String(250), nullable=False)

#Base de datos resultados para capacidad y nivel de servicio con dos carriles
class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Fpe = db.Column(db.Float, nullable=False)
    Fd = db.Column(db.Float, nullable=False)
    Fcb = db.Column(db.Float, nullable=False)
    Ec = db.Column(db.Float, nullable=False)
    Fp = db.Column(db.Float, nullable=False)
    cap_60 = db.Column(db.Integer, nullable=False)
    cap_5 = db.Column(db.Integer, nullable=False)
    FHP = db.Column(db.Float, nullable=False)
    v1 = db.Column(db.Float, nullable=False)
    Fu = db.Column(db.Float, nullable=False)
    Fcb1 = db.Column(db.Float, nullable=False)
    v2 = db.Column(db.Float, nullable=False)
    Ec_vel = db.Column(db.Float, nullable=False)
    Fp_vel = db.Column(db.Float, nullable=False)
    Ft = db.Column(db.Float, nullable=False)
    vM = db.Column(db.Float, nullable=False)
    Vi = db.Column(db.Integer, nullable=False)
    Final = db.Column(db.Integer, nullable=False)
    carretera = db.Column(db.String(200), nullable = False)
    proyecto = db.Column(db.String(200), nullable = False)
    a_carril = db.Column(db.Float, nullable=False)
    a_berma = db.Column(db.Float, nullable=False)
    p_promedio = db.Column(db.Float, nullable=False)
    l_sector = db.Column(db.Float, nullable=False)
    curvatura = db.Column(db.Integer, nullable=False)
    d_sentido = db.Column(db.Integer, nullable=False)
    d_sentido1 = db.Column(db.Integer, nullable=False)
    p_no_rebase = db.Column(db.Integer, nullable=False)
    p_automoviles = db.Column(db.Integer, nullable=False)
    p_buses = db.Column(db.Integer, nullable=False)
    p_camiones = db.Column(db.Integer, nullable=False)
    vol_cap = db.Column(db.Integer, nullable=False)
    terreno = db.Column(db.String(200), nullable = False)

#Base de datos resultados para capacidad y nivel de servicio para vías multicariil
class Multicaril_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Float, nullable=False)
    b = db.Column(db.Float, nullable=False)
    c = db.Column(db.Float, nullable=False)
    vel_generica = db.Column(db.Integer, nullable=False)
    fc = db.Column(db.Float, nullable=False)
    fs = db.Column(db.Integer, nullable=False)
    fb = db.Column(db.Integer, nullable=False)
    fa = db.Column(db.Float, nullable=False)
    V_libre = db.Column(db.Integer, nullable=False)
    vel_flujo_libre = db.Column(db.Integer, nullable=False)
    Ec = db.Column(db.Float, nullable=False)
    fhv = db.Column(db.Float, nullable=False)
    qp = db.Column(db.Integer, nullable=False)
    v_densidad = db.Column(db.Float, nullable=False)
    densidad = db.Column(db.Float, nullable=False)
    final = db.Column(db.String(10), nullable=False)
    # Valores insertados
    v1 = db.Column(db.String(10), nullable=False)
    v2 = db.Column(db.String(10), nullable=False)
    v3 = db.Column(db.String(10), nullable=False)
    v4 = db.Column(db.Float, nullable=False)
    v5 = db.Column(db.Integer, nullable=False)
    v6 = db.Column(db.Integer, nullable=False)
    v7 = db.Column(db.String(10), nullable=False)
    v8 = db.Column(db.String(10), nullable=False)
    v9 = db.Column(db.Float, nullable=False) 
    v10 = db.Column(db.Float, nullable=False)
    v11 = db.Column(db.Float, nullable=False)
    v12 = db.Column(db.Integer, nullable=False)
    v13 = db.Column(db.String(10), nullable=False)
    v14 = db.Column(db.String(10), nullable=False)
    v15 = db.Column(db.String(10), nullable=False)
    v16 = db.Column(db.Float, nullable=False)
    v17 = db.Column(db.Float, nullable=False)
    v18 = db.Column(db.Integer, nullable=False) 
    v19 = db.Column(db.String(100), nullable=False)
    v20 = db.Column(db.String(100), nullable=False)
    v21 = db.Column(db.String(10), nullable=False)


#Base de datos para análisis de sensibilidad - Multicarril
class Sensibilidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n1 = db.Column(db.String(10), nullable=False)
    n2 = db.Column(db.String(10), nullable=False)
    n3 = db.Column(db.String(10), nullable=False)
    n4 = db.Column(db.String(10), nullable=False)
    n5 = db.Column(db.String(10), nullable=False)
    n6 = db.Column(db.String(10), nullable=False)
    n7 = db.Column(db.Float, nullable=False)
    n8 = db.Column(db.Float, nullable=False)
    n9 = db.Column(db.Float, nullable=False)
    n10 = db.Column(db.Float, nullable=False)
    n11 = db.Column(db.Float, nullable=False)
    n12 = db.Column(db.Float, nullable=False)
    n13 = db.Column(db.Float, nullable=False)
    n14 = db.Column(db.Float, nullable=False)
    n15 = db.Column(db.Float, nullable=False)
    n16 = db.Column(db.Float, nullable=False)
    n17 = db.Column(db.Float, nullable=False)
    n18 = db.Column(db.Float, nullable=False)
    n19 = db.Column(db.Float, nullable=False)
    n20 = db.Column(db.Float, nullable=False)
    n21 = db.Column(db.String(10), nullable=False)
    n22 = db.Column(db.String(10), nullable=False)
    n23 = db.Column(db.String(10), nullable=False)
    n24 = db.Column(db.String(10), nullable=False)
    n25 = db.Column(db.String(10), nullable=False)
    n26 = db.Column(db.String(10), nullable=False)
    n27 = db.Column(db.String(10), nullable=False)
    n28 = db.Column(db.String(10), nullable=False)
    n29 = db.Column(db.Float, nullable=False)
    n30 = db.Column(db.Float, nullable=False)
    n31 = db.Column(db.Float, nullable=False)
    n32 = db.Column(db.Float, nullable=False)
    n33 = db.Column(db.Float, nullable=False)
    n34 = db.Column(db.Float, nullable=False)
    n35 = db.Column(db.Float, nullable=False)
    n36 = db.Column(db.Float, nullable=False)
    n37 = db.Column(db.Float, nullable=False)
    n38 = db.Column(db.Float, nullable=False)
    n39 = db.Column(db.Float, nullable=False)
    n40 = db.Column(db.Float, nullable=False)
    n41 = db.Column(db.Float, nullable=False)
    n42 = db.Column(db.Float, nullable=False)
    n43 = db.Column(db.Float, nullable=False)
    n44 = db.Column(db.Float, nullable=False)
    n45 = db.Column(db.Float, nullable=False)
    n46 = db.Column(db.Float, nullable=False)
    n47 = db.Column(db.Float, nullable=False)
    n48 = db.Column(db.Float, nullable=False)
    n49 = db.Column(db.Float, nullable=False)
    n50 = db.Column(db.Float, nullable=False)
    n51 = db.Column(db.Float, nullable=False)
    n52 = db.Column(db.Float, nullable=False)
    n53 = db.Column(db.Float, nullable=False)
    n54 = db.Column(db.Float, nullable=False)
    n55 = db.Column(db.Float, nullable=False)
    n56 = db.Column(db.Float, nullable=False)
    n57 = db.Column(db.Float, nullable=False)
    n58 = db.Column(db.Float, nullable=False)
    n59 = db.Column(db.Float, nullable=False)
    n60 = db.Column(db.String(10), nullable=False)
    n61 = db.Column(db.Float, nullable=False)
    n62 = db.Column(db.Float, nullable=False)
    n63 = db.Column(db.Float, nullable=False)
    n64 = db.Column(db.String(10), nullable=False)
    n65 = db.Column(db.Float, nullable=False)
    n66 = db.Column(db.Float, nullable=False)
    n67 = db.Column(db.Float, nullable=False)
    n68 = db.Column(db.String(10), nullable=False)
    n69 = db.Column(db.Float, nullable=False)
    n70 = db.Column(db.Float, nullable=False)
    n71 = db.Column(db.Float, nullable=False)
    n72 = db.Column(db.String(10), nullable=False)
    n73 = db.Column(db.Float, nullable=False)
    n74 = db.Column(db.Float, nullable=False)
    n75 = db.Column(db.Float, nullable=False)
    n76 = db.Column(db.String(10), nullable=False)
    n77 = db.Column(db.Float, nullable=False)
    n78 = db.Column(db.Float, nullable=False)
    n79 = db.Column(db.Float, nullable=False)
    n80 = db.Column(db.String(10), nullable=False)
    n81 = db.Column(db.Float, nullable=False)
    n82 = db.Column(db.Float, nullable=False)
    n83 = db.Column(db.Float, nullable=False)
    n84 = db.Column(db.String(10), nullable=False)
    n85 = db.Column(db.Float, nullable=False)
    n86 = db.Column(db.Float, nullable=False)
    n87 = db.Column(db.Float, nullable=False)
    n88 = db.Column(db.String(10), nullable=False)
db.create_all()

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class Capacidad(FlaskForm):
    carretera = StringField(label="Nombre de carretera o proyecto", name="carretera")
    proyecto = StringField(label="Proyecto o abscisa")
    a_carril = FloatField(label="Ancho de carril",description="Ingrese valor en metros", validators = [DataRequired(),NumberRange(min=2.7, max=3.65)])
    a_berma = FloatField(label="Ancho de berma",description="Ingrese valor en metros",  validators = [DataRequired(),NumberRange(min=0, max=3)])
    p_promedio = FloatField(label="Pendiente promedio ",description="Ingrese valor en porcentaje", validators = [DataRequired(),NumberRange(min=0, max=12)])
    l_sector = FloatField(label="Longitud del sector",description="Ingrese valor en kilometros",validators = [DataRequired(),NumberRange(min=0, max=5)])
    curvatura = IntegerField(label="Grado de curvatura",description="Ingrese valor en °/km", validators=[NumberRange(min=0, max=799)])
    d_sentido= IntegerField(label="Distribución por sentido", validators = [DataRequired(),NumberRange(min=50, max=100)])
    p_no_rebase = IntegerField(label="Porcentaje de zonas de no rebase",description="Ingrese valor en porcentaje",validators=[NumberRange(min=0, max=100)])
    p_automoviles = IntegerField(label="Porcentaje de automoviles",description="Ingrese valor en porcentaje", validators=[NumberRange(min=0, max=100)])
    p_buses = IntegerField(label="Porcentaje de buses",default=1,description="Ingrese valor en porcentaje", validators=[NumberRange(min=0, max=100)])
    p_camiones = IntegerField(label="Porcentaje de camiones",description="Ingrese valor en porcentaje", validators=[NumberRange(min=0, max=100)])
    vol_cap = IntegerField(label="Volumen horario total ambos sentidos",description="Ingrese valor Veh/h", validators = [DataRequired(),NumberRange(min=0, max=100000)])
    submit = SubmitField("Calcular Capacidad y Nivel de servicio")

class Multicarril(FlaskForm):
    carretera = StringField(label="Nombre de carretera o proyecto", validators=[DataRequired()])
    proyecto = StringField(label="Proyecto o abscisa")
    terreno = SelectField('Tipo de terreno', choices=[('Plano', 'Plano'),('Ondulado', 'Ondulado'), ('Montañoso', 'Montañoso')])
    tipo_analisis = SelectField('¿Qué tipo de analísis desea realizar?', choices=[('Operacional', 'Operacional'), ('Planeacion', 'Planeación')])
    tipo_tramo = SelectField("¿Cuál es el tipo de tramo?", choices=[('Generico', 'Generico'), ('Ascenso', 'Ascenso'), ('Descenso', 'Descenso')])
    clasificacion = SelectField('¿Cuál es la clasificación de la vía Multicarril? (Referencia Tabla 10)', choices=[("A1", 'A1'), ("B1", 'B1'), ("C1",'C1')])
    pendiente = FloatField(label="Pendiente", validators = [DataRequired(),NumberRange(min=0, max=8)] )
    l_tramo = IntegerField(label="Longitud del tramo (metros)", validators = [DataRequired(),NumberRange(min=500, max=8000)] )
    n_carriles = IntegerField(label="Número de carriles", validators = [DataRequired(),NumberRange(min=0, max=10)])
    a_carril = SelectField('Ancho de carril (metros)', choices=[('3', '3 metros'), ('3.3', '3.3 metros'), ('3.5', '3.5 metros o mayor')])
    separador = SelectField('¿La vía cuenta con separador?', choices=[(True, 'Si'), (False, 'No')])
    a_separador = FloatField(label="Ancho de separador (metros)", validators = [DataRequired(),NumberRange(min=0, max=5)] )
    a_berma_derecha = FloatField(label="Ancho de Berma derecha (metros)", validators = [DataRequired(),NumberRange(min=0, max=5)] )
    a_berma_izquierda = FloatField(label="Ancho de Berma izquierda (metros)", validators = [DataRequired(),NumberRange(min=0, max=5)] )
    n_accesos = IntegerField(label="Número de accesos", validators = [DataRequired(),NumberRange(min=0, max=50)])
    control_accesos = SelectField('¿La vía cuenta con control de accesos?', choices=[(1, 'Si'), (2, 'No')])
    control_peatones = SelectField('¿Peatones frecuentes?', choices=[(True, 'Si'), (False, 'No')])
    fp = SelectField("¿Conductores frecuentes?", choices=[(1, 'Si'), (0.90, 'No')])
    fhpico = FloatField(label="Factor de Hora Pico", validators = [DataRequired(),NumberRange(min=0, max=5)] )
    p_camiones = FloatField(label="Porcentaje de camiones", validators = [DataRequired(),NumberRange(min=0, max=50)])
    vol_transito = IntegerField(label="Volumen del tránsito", validators = [DataRequired(),NumberRange(min=0, max=100000)])
    submit = SubmitField("Calcular Capacidad y Nivel de servicio")


#Gráfica de curva maestra
lista_maestra = np.arange(0,2500)
def velo(vel, a, b, c, valor):
    res = vel-a*((valor/b)**c)
    return res
datos96 = []
datos90 = []
datos80 = []
datos70 = []
for element in lista_maestra:
    res1 = velo(80,2.375,1036.550,2.044,element)
    res2= velo(70,5.497,692.345,1.010,element)
    res3= velo(96,4.609,1124.526,1.624,element)
    res4= velo(90,1.040,882.082,2.545,element)
    datos80.append(res1)
    datos70.append(res2)
    datos96.append(res3)
    datos90.append(res4)

def maestra(flujo, vel_operacion):
    plt.plot(lista_maestra, datos96, color="black")
    plt.plot(lista_maestra, datos90, color="black")
    plt.plot(lista_maestra, datos80, color="black")
    plt.plot(lista_maestra, datos70, color="black")
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
    plt.scatter(flujo,vel_operacion, label="Resultado obtenido")
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


#Función que convierte en si o no un True or False
def True_or_false(variable):
    if variable == 1 or variable == True or variable == "1":
        return "Si"
    else:
        return "No"


def Capacidad_Ns(a_carril, a_berma, p_promedio, l_sector, d_sentido, p_no_rebase, p_autos, p_buses,
 p_camiones, vol_cap):
    p_pesados = p_buses+p_camiones
    c_ideal = 3200
    #Capacidad
    Fpe = cap.inter_compuesta_1(p_promedio, cap.tabla_1x, cap.tabla_1, l_sector)
    Fd = cap.inter_compuesta_2(d_sentido,cap.tabla_2x,cap.tabla_2,p_no_rebase)
    Fcb = cap.inter_compuesta3(cap.tabla_3x,cap.tabla_3,a_berma,a_carril)
    Ec = cap.inter_compuesta4(cap.tabla_4x, cap.tabla_4, p_promedio, p_pesados, l_sector)
    Fp = (1/(1+(p_pesados/100)*(Ec-1)))
    Fp = round(Fp,4)
    cap_60 = round(c_ideal*Fpe*Fd*Fcb*Fp,0)
    FHP = cap.inter_tabla5(cap.tabla_5,cap.tabla_5x,cap.tabla_51,cap.tabla_51x,cap_60)
    cap_5 =round(cap_60*FHP,0)
    #Nivel de servico
    v1 = cap.inter_compuesta6(cap.tabla_6x, cap.tabla_6, p_promedio, l_sector)
    Fu = cap.interpolacionp(cap.tabla_7x,cap.tabla_7,vol_cap/cap_60)
    Fcb1 = cap.inter_compuesta8(cap.tabla_8x,cap.tabla_8,a_carril,a_berma)
    v2 = round(v1* Fu * Fcb1,2)
    Ec_vel = 0
    if p_promedio < 3:
        Ec_vel = cap.inter_compuesta_plan_ond(v2,cap.tabla_9x,cap.plano,p_camiones,l_sector)
    elif  p_promedio < 6:
        Ec_vel = cap.inter_compuesta_plan_ond(v2,cap.tabla_9x,cap.ondulado,p_camiones,l_sector)
    elif  p_promedio <9:
        Ec_vel = cap.inter_compuesta_mon_esc(v2,cap.tabla_9x,cap.montanoso,p_camiones,l_sector)
    else:
        Ec_vel = cap.inter_compuesta_mon_esc(v2,cap.tabla_9x,cap.escarpado,p_camiones,l_sector)

    fp_vel = round(1/(1+((p_camiones/100)*(Ec_vel-1))),3)
    Ft = round(cap.interpolacion(cap.tabla_10x, cap.tabla_10, p_promedio),3)
    vM = round(v2*fp_vel*Ft,4)
    Vi = float((vM * 100)/90)
    Vi = round(Vi,3)

    if p_promedio < 3:
        lista = cap.plano_1
    elif  p_promedio < 6:
        lista = cap.ondulado_1
    elif  p_promedio <9:
        lista = cap.montanoso_1
    else:
        lista = cap.escarpado_1
    final = cap.index(lista, Vi)
    terreno = cap.tipo_terreno(p_promedio)
    return  Fpe,Fd,Fcb,Ec,Fp,int(cap_60),int(cap_5),FHP,v1,Fu,Fcb1,v2,Ec_vel,fp_vel,Ft,vM,Vi,final,terreno


@app.route("/", methods=["GET","POST"])
def home():
    form = Capacidad()
    if form.validate_on_submit():
        if form.p_no_rebase == 0:
            form.p_no_rebase = 1
        if form.p_buses == 0:
            form.p_buses == 1
        if form.p_camiones == 0:
            form.p_camiones == 1
        res = Capacidad_Ns(form.a_carril.data,form.a_berma.data,form.p_promedio.data,form.l_sector.data,
        form.d_sentido.data,form.p_no_rebase.data,form.p_automoviles.data,form.p_buses.data,
        form.p_camiones.data,form.vol_cap.data)
        d_sen = 100-form.d_sentido.data
        new_object = Resultado(Fpe=res[0],Fd=res[1],Fcb=res[2],Ec=res[3],Fp=res[4],cap_60=res[5],
        cap_5=res[6], FHP=res[7],v1=res[8],Fu=res[9],Fcb1=res[10],v2=res[11],Ec_vel=res[12],
        Fp_vel=res[13],Ft=res[14],vM=res[15],Vi=res[16],Final=res[17], carretera=form.carretera.data,
        proyecto = form.proyecto.data, a_carril=form.a_carril.data,a_berma=form.a_berma.data, p_promedio=form.p_promedio.data,
        l_sector=form.l_sector.data, curvatura=form.curvatura.data, d_sentido=form.d_sentido.data, d_sentido1=d_sen, p_no_rebase =form.p_no_rebase.data,
        p_automoviles=form.p_automoviles.data, p_buses=form.p_buses.data, p_camiones=form.p_camiones.data, vol_cap= form.vol_cap.data, terreno = res[18])
        db.session.add(new_object)
        db.session.commit()
        return redirect(url_for('resultado'))
    return render_template ('index.html', form=form)
datos = ["","0","1","2","3","4","5","6","7","8","9","10","0","1","2","3","4","5","6","7","8","9","10",
        "0","1","2","3","4","5","6","7","8","9","0","1","2","3","4","5","6","7","8","9","10","0","1","2","3","4","5","6","7","8","9","10",
        "0","1","2","3","4","5","6","7","8","9","10","0","1","2","3","4","5","6","7","8","9","10",
        "0","81","83","84","85","86","87","84","85","76","86","88","89","90","91","92","93","94","95","96","97",
        "98","99","100","101"]

@app.route("/multicarril", methods=["GET","POST"])
def multicarril():
    form = Multicarril()
    if form.validate_on_submit():
        v1 = form.tipo_analisis.data
        v2 = form.tipo_tramo.data
        v3 = form.clasificacion.data
        v4 = form.pendiente.data
        v5 = form.l_tramo.data
        v6 = form.n_carriles.data
        v7 = float(form.a_carril.data)
        v8 = bool(form.separador.data)
        v9 = form.a_separador.data
        v10 = form.a_berma_derecha.data
        v11 = form.a_berma_izquierda.data
        v12 = form.n_accesos.data
        v13 = form.control_accesos.data
        v19 = form.carretera.data
        v20 = form.proyecto.data
        v21 = form.terreno.data
        if v13 == 1:
            v13 = True
        else:
            v13 = False
        v14 = bool(form.control_peatones.data)
        v15 = float(form.fp.data)
        v16 = float(form.fhpico.data)
        v17 = form.p_camiones.data
        v18 = form.vol_transito.data
        if v4 >= 8:
            v4 = 7.99
        print(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        #análisis de sensibilidad
        rs= mp.calc_multicarril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        vol = sen.sensibilidad_volumen(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,rs[15],v18,rs[13],rs[12],rs[14])
        pen = sen.sensibilidad_pendiente(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15, rs[15],v18,rs[13],rs[12],rs[14])
        fin = sen.sensibilidad_bool(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15)
        sen.sensibilidad_camiones(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,rs[15],v18,rs[13],rs[12],rs[14])
        sen.sensiblidad_carriles(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15,rs[15])
        sen.sensibilidad_ancho_carril(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15, rs[15])
        sen.sensibilidad_ancho_separador(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15, rs[15])
        sen.sensibilidad_ancho_bermas(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15, rs[15])
        sen.sensibilidad_n_accesos(v1,v2,v3,v8,v13,v14,v7,v9,v10,v11,v12,v4,v17,v5,v18,v16,v6,v15, rs[15])
        maestra(rs[12], rs[13])       
        v8 = True_or_false(v8)
        v13 = True_or_false(v13)
        v14 = True_or_false(v14)
        calculo = Multicaril_db(a=rs[0], b=rs[1], c=rs[2], vel_generica=rs[3], fc=rs[4], fs=rs[5], fb=rs[6],
        fa=rs[7], V_libre=rs[8], vel_flujo_libre=rs[9],Ec=rs[10], fhv=rs[11],qp=rs[12], v_densidad=rs[13],
        densidad=rs[14], final=rs[15], v1=v1, v2=v2, v3=v3, v4=v4, v5=v5, v6=v6, v7=v7, v8=v8, v9=v9, v10=v10,
        v11=v11, v12=v12, v13=v13, v14=v14, v15=v15, v16=v16, v17=v17, v18=v18, v19=v19, v20=v20, v21=v21)
        db.session.add(calculo)
        db.session.commit()
        datos[0]="element"
        datos[1]=int(vol[0])
        datos[2]=int(vol[1])
        datos[3]=int(vol[2])
        datos[4]=int(vol[3])
        datos[5]=int(vol[4])
        datos[6]=int(vol[5])
        datos[7]=int(vol[6])
        datos[8]=int(vol[7])
        datos[9]=int(vol[8])
        datos[10]=vol[9]
        datos[11]=vol[10]
        datos[12]=vol[11]
        datos[13]=vol[12]
        datos[14]=vol[13]
        datos[15]=vol[14]
        datos[16]=vol[15]
        datos[17]=vol[16]
        datos[18]=vol[17]
        datos[19]=vol[18]
        datos[20]=vol[19]
        datos[21]=pen[0]
        datos[22]=pen[1]
        datos[23]=pen[2]
        datos[24]=pen[3]
        datos[25]=pen[4]
        datos[26]=pen[5]
        datos[27]=pen[6]
        datos[28]=pen[7]
        datos[29]=pen[8]
        datos[30]=pen[9]
        datos[31]=pen[10]
        datos[32]=pen[11]
        datos[33]=pen[12]
        datos[34]=pen[13]
        datos[35]=pen[14]
        datos[36]=pen[15]
        datos[37]=pen[16]
        datos[38]=pen[17]
        datos[39]=pen[18]
        datos[40]=pen[19]
        datos[41]=pen[20]
        datos[42]=pen[21]
        datos[43]=pen[22]
        datos[44]=pen[23]
        datos[45]=pen[24]
        datos[46]=pen[25]
        datos[47]=pen[26]
        datos[48]=pen[27]
        datos[49]=pen[28]
        datos[50]=pen[29]
        datos[51]=pen[30]
        datos[52]=pen[31]
        datos[53]=pen[32]
        datos[54]=pen[33]
        datos[55]=pen[34]
        datos[56]=pen[35]
        datos[57]=fin[0]
        datos[58]=fin[1]
        datos[59]=fin[2]
        datos[60]=fin[3]
        datos[61]=fin[4]
        datos[62]=fin[5]
        datos[63]=fin[6]
        datos[64]=fin[7]
        datos[65]=fin[8]
        datos[66]=fin[9]
        datos[67]=fin[10]
        datos[68]=fin[11]
        datos[69]=fin[12]
        datos[70]=fin[13]
        datos[71]=fin[14]
        datos[72]=fin[15]
        datos[73]=fin[16]
        datos[74]=fin[17]
        datos[75]=fin[18]
        datos[76]=fin[19]
        datos[77]=fin[20]
        datos[78]=fin[21]
        datos[79]=fin[22]
        datos[80]=fin[23]
        datos[81]=fin[24]
        datos[82]=fin[25]
        datos[83]=fin[26]
        datos[84]=fin[27]
        datos[85]=fin[28]
        datos[86]=fin[29]
        datos[87]=fin[30]
        datos[88]=fin[31]
        datos[89]=fin[32]
        datos[90]=fin[33]
        datos[91]=fin[34]
        datos[92]=fin[35]
        datos[93]=fin[36]
        datos[94]=fin[37]
        datos[95]=fin[38]
        datos[96]=fin[39]
        datos[97]=fin[40]
        datos[98]=fin[41]
        datos[99]=fin[42]
        datos[100]=fin[43]
        plt.close()
        matplotlib.use('Agg')
        print(datos)
        return redirect(url_for("resultado_Multicarril"))
    return render_template("multicarril.html", form = form)

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    id = len(db.session.query(Resultado).all())
    registro = Resultado.query.get(id)
    return render_template('resultados_2_carriles.html',datos=registro)

@app.route("/resultado_Multicarril", methods=["GET","POST"])
def resultado_Multicarril():
    id = len(db.session.query(Multicaril_db).all())
    registro = Multicaril_db.query.get(id)
    id1 = len(db.session.query(Sensibilidad).all())
    return render_template('resultados_multicarril.html',datos=registro, data=datos)

@app.route("/tabla_18")
def tabla_18():
    return render_template("tabla18mp.html")

@app.route("/tabla_19")
def tabla_19():
    return render_template("tabla19mp.html")

@app.route("/registro/<int:index>", methods=["GET","POST"])
def registro(index):
    registro = Resultado.query.get(index)
    return render_template('resultados.html',datos=registro)

@app.route("/resultados",methods=["GET","POST"])
def resultados():
    all_records = db.session.query(Resultado).all()
    return render_template('data.html', datos=all_records)

@app.route("/capacidad-NS", methods=["GET","POST"])
def data():
    id = len(db.session.query(Resultado).all()) + 1
    registro = Resultado.query.get(id)
    return render_template('data.html',datos=registro)

@app.route("/blog", methods=["GET","POST"])
def blog():
    posts = db_blog.session.query(BlogPost).all()
    return render_template ('blog_final.html',  all_posts=posts)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = db_blog.session.query(BlogPost).all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post = requested_post)

@app.route("/new-post", methods=["GET","POST"])
def New_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=form.author.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db_blog.session.add(new_post)
        db_blog.session.commit()
        return redirect(url_for("blog"))
    return render_template("make-post.html", form=form, title_post="Nuevo Post")

@app.route("/edit-post/<post_id>", methods=["GET","POST"])
def edit(post_id):
    form = CreatePostForm()
    if form.validate_on_submit():
        edit_post = BlogPost.query.get(post_id)
        edit_post.title = form.title.data
        edit_post.subtitle = form.subtitle.data
        edit_post.body = form.body.data
        edit_post.img_url = form.img_url.data
        edit_post.author =form.author.data
        edit_post.date = date.today().strftime("%B %d, %Y")
        db_blog.session.commit()
        return redirect(url_for("blog"))
    return render_template("make-post.html", form=form, title_post="Editar Post")

@app.route("/delete/<post_id>", methods =["GET","POST"])
def delete(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db_blog.session.delete(post_to_delete)
    db_blog.session.commit()
    return render_template("blog_final.html")
if __name__ == "__main__":
    app.run(debug=True)

