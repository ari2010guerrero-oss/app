from flask import Blueprint, render_template, request

routes = Blueprint("routes", __name__)

INTERESES = {
    "musica": "Música",
    "videojuegos": "Videojuegos",
    "deportes": "Deportes",
    "series": "Series",
    "lectura": "Lectura",
    "arte": "Arte y dibujo",
}


@routes.get("/")
def inicio():
    return render_template("index.html", intereses=INTERESES)


@routes.post("/enviar")
def enviar():
    nombre = request.form.get("nombre", "").strip()
    interes = request.form.get("interes", "").strip()

    if not nombre or interes not in INTERESES:
        return render_template(
            "index.html",
            intereses=INTERESES,
            error="Escribe tu nombre y selecciona un interés.",
            nombre=nombre,
        ), 400

    return render_template(
        "gracias.html",
        nombre=nombre,
        interes=INTERESES[interes],
        interes_id=interes,
    )
