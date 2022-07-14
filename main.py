from flask import Flask, render_template, request
import requests
import http.client
import urllib.parse
import json
import smtplib
app = Flask(__name__)


limite = 10
conn = http.client.HTTPConnection('api.mediastack.com')

params = urllib.parse.urlencode({
    'access_key': '78b7bf9ea1691f97779e4737d227bd58',
    'categories': 'entertainment, technology',
    'languages': 'en',
    'sort': 'popularity',
    'limit': limite,
})

MY_EMAIL = "cristiannicolasrodriguez3270@gmail.com"
MY_PASSWORD = "96032700621"
My_email = "cristiannicolasrodriguez3270@gmail.com"


def get_notice(categoria, lenguaje, limite=1):
    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': '78b7bf9ea1691f97779e4737d227bd58',
        'categories': categoria,
        'languages': lenguaje,
        'sort': 'popularity',
        'limit': limite,
    })

    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    data_info = data.decode('utf-8')
    data_json = json.loads(data_info)

    return data_json


@app.route('/')
def home():
    npoint_link = "https://api.npoint.io/55793bb09f815223433a"
    response = requests.get(url=npoint_link)
    response.raise_for_status()
    all_post = response.json()

    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    data_info = data.decode('utf-8')
    data_json = json.loads(data_info)
    return render_template("portafolio.html", posts=all_post, notices=data_json)


@app.route("/portafolio")
def portafolio():
    return render_template("portafolio.html")


# Noticias Tecnología - Deportes - Economia - Entretenimiento
tech_notice = get_notice('technology', 'en', 5)
tech_image = tech_notice['data'][0]['image']
buss_notice = get_notice('business', 'es', 3)
buss_image = buss_notice['data'][0]['image']
sport_notice = get_notice('sports', 'es', 3)
sport_image = sport_notice['data'][0]['image']
sport_image_2 = sport_notice['data'][1]['image']
health_notice = get_notice('health', 'en', 3)
general_notice = get_notice('general', 'es', 3)


@app.route("/Nico_blog")
def nico_blog():
    return render_template("blog.html",
                           technology=tech_notice,
                           image_url=tech_image,
                           bussines=buss_notice,
                           img_buss=buss_image,
                           sport=sport_notice,
                           spo_image=sport_image,
                           spo2_image=sport_image_2,
                           science=science_notice,
                           science_image=sci_image,
                           science2_image=sci2_image,
                           health=health_notice,
                           general=general_notice,
                           )


@app.route("/blog/<num>")
def get_blog(num):
    var = int(num)
    npoint_link = "https://api.npoint.io/55793bb09f815223433a"
    response = requests.get(url=npoint_link)
    response.raise_for_status()
    all_post = response.json()
    for post in all_post:
        if post["id"] == var:
            post_title = post["title"]
            post_2 = post["body"]
    return render_template("post.html", posts=all_post, post_return=post_2,
                           title_1=post_title)


@app.route("/bootstrap")
def boot_page():
    return render_template("bootsrap.html")


@app.route("/tindog")
def tindog():
    return render_template("tindog.html")


@app.route("/compras")
def compras():
    return render_template("compras.html")


@app.route("/rejilla")
def reja():
    return render_template("rejilla.html")


@app.route("/store")
def ventas():
    return render_template("prueba.html")


@app.route("/angela")
def angela():
    return render_template("index_Angela.html")


@app.route('/angela_post')
def get_all_posts():
    return render_template("index_final_blog.html", all_posts=posts)


@app.route('/form-entry', methods=['POST'])
def receive_data():
    name_blog = request.form['name']
    email_blog = request.form['email']
    subject_blog = request.form['subject']
    message_blog = request.form['message']
    print(
        f'El nombre del usuario es {name_blog}, su correo es {email_blog} contraseña {subject_blog} y mensaje {message_blog}')
    return f'Hola {name_blog} mensaje enviado correctamente'


if __name__ == "__main__":
    app.run(debug=True)
