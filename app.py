from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
#Parametro con ruta
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"""
    <h1>¡Hola, {nombre}!</h1>
    <p>Bienvenido a esta pagina personalizada.</p>
    <a href ="/">Volver al inicio</a>
    """
#Formulario
@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    return render_template("formulario.html")

#Ruta que procesa, responde
@app.route("/resultado", methods=["POST"])
def resultado():
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    return render_template("resultado.html", nombre=nombre, edad=edad)

if __name__ == "__main__":
    app.run(debug=True)

