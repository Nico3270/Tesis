from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange,  URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import requests
import capacidad_NS as cap


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


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class Capacidad(FlaskForm):
    a_carril = FloatField(label="Ancho de carril (metros)",validators = [DataRequired(),NumberRange(min=0, max=10)])
    a_berma = FloatField(label="Ancho de berma",  validators = [DataRequired(),NumberRange(min=0, max=3)])
    p_promedio = FloatField(label="Pendiente promedio ", validators = [DataRequired(),NumberRange(min=0, max=12)])
    l_sector = FloatField(label="Longitud del sector",validators = [DataRequired(),NumberRange(min=0, max=50)])
    d_sentido= IntegerField(label="Distribución por sentido", validators = [DataRequired(),NumberRange(min=0, max=100)])
    p_no_rebase = IntegerField(label="Porcentaje de zonas de no rebase", validators = [DataRequired(),NumberRange(min=0, max=100)])
    p_automoviles = IntegerField(label="Porcentaje de automoviles", validators = [DataRequired(),NumberRange(min=0, max=100)])
    p_buses = IntegerField(label="Porcentaje de buses", validators = [DataRequired(),NumberRange(min=0, max=100)])
    p_camiones = IntegerField(label="Porcentaje de camiones", validators = [DataRequired(),NumberRange(min=0, max=100)])
    vol_cap = IntegerField(label="Volumen horario total ambos sentidos", validators = [DataRequired(),NumberRange(min=0, max=100000)])
    submit = SubmitField("Calcular Capacidad y Nivel de servicio")

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
db.create_all()



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
    Fu = cap.interpolacion(cap.tabla_7x,cap.tabla_7,vol_cap/cap_60)
    Fcb1 = cap.inter_compuesta8(cap.tabla_8x,cap.tabla_8,a_carril,a_berma)
    v2 = v1* Fu * Fcb1
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
    vM = v2*fp_vel*Ft
    Vi = int((vM * 100)/90)

    if p_promedio < 3:
        lista = cap.plano_1
    elif  p_promedio < 6:
        lista = cap.ondulado_1
    elif  p_promedio <9:
        lista = cap.montanoso_1
    else:
        lista = cap.escarpado_1
    final = cap.index(lista, Vi)
    return  Fpe,Fd,Fcb,Ec,Fp,int(cap_60),int(cap_5),FHP,v1,Fu,Fcb1,v2,Ec_vel,fp_vel,Ft,vM,Vi,final


@app.route("/", methods=["GET","POST"])
def home():
    form = Capacidad()
    if form.validate_on_submit():
        res = Capacidad_Ns(form.a_carril.data,form.a_berma.data,form.p_promedio.data,form.l_sector.data,
        form.d_sentido.data,form.p_no_rebase.data,form.p_automoviles.data,form.p_buses.data,
        form.p_camiones.data,form.vol_cap.data)
        new_object = Resultado(Fpe=res[0],Fd=res[1],Fcb=res[2],Ec=res[3],Fp=res[4],cap_60=res[5],
        cap_5=res[6], FHP=res[7],v1=res[8],Fu=res[9],Fcb1=res[10],v2=res[11],Ec_vel=res[12],
        Fp_vel=res[13],Ft=res[14],vM=res[15],Vi=res[16],Final=res[17])
        db.session.add(new_object)
        db.session.commit()
        return redirect(url_for('resultado'))
    return render_template ('index.html', form=form)

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    id = len(db.session.query(Resultado).all())
    registro = Resultado.query.get(id)
    return render_template('resultados.html',datos=registro)

@app.route("/registro/<int:index>", methods=["GET","POST"])
def registro(index):
    id = len(db.session.query(Resultado).all())
    registro = Resultado.query.get(id)
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