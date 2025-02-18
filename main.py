from flask import Flask, render_template, request , jsonify, url_for

app = Flask(__name__, template_folder="template")



@app.route("/")
def index():
    titulo="IDGS801"
    lista=["pedro","juan","luis"]
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo.html")


@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")



@app.route("/hola")
def hola():
    return "<h1>hello word -- hola!</h1>"

@app.route("/user/<string:user>")
def user(user):
    return f"<h1>hola , {user}!</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>el numero es: {n}!</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>hola! {username}! tu id es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>la suma es: ! {n1+n2}! </h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func(param="juan"):
    return f"<h1>hola , {param}!</h1>"


@app.route("/operas")
def operas():
    return '''
        <form>
        < label for="name"> Name:</label>
        <input type= "text" id-"name" name="name" required>

        < label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>

        </form>
            '''
@app.route("/operasBass")
def operas1():
    return render_template("operaBass.html")


@app.route("/resultado",methods=["POST","GET"])
def result():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    return "la multiplicación de {}x {} es {}".format(n1,n2,str(int(n1)*int(n2)))

@app.route("/resultado2", methods=["POST"])
def resultado2():
    
        n1 = float(request.form.get("n1"))
        n2 = float(request.form.get("n2"))
        operacion = request.form.get("operacion")

        if operacion == "suma":
            resultado = n1 + n2
        elif operacion == "resta":
            resultado = n1 - n2
        elif operacion == "multiplicacion":
            resultado = n1 * n2
        elif operacion == "division":
            resultado = n1 / n2 
        else:
            resultado = "Operación no válida"

        return str(resultado)

@app.route("/cinepolis")
def cine():
    return render_template("cinepolis.html")

@app.route("/calculo_Cine", methods=["POST"])
def calculo_Cine():
    data = request.json
    personas = int(data.get("cantidadPersonas", 0))
    boletos = int(data.get("cantidadBoletos", 0))
    cineco = data.get("tarjeta")
    
    max_boletos = personas * 7
    precio = 12
    
    if boletos > max_boletos:
        return jsonify({"error": f"Solo puedes comprar hasta {max_boletos} boletos."}), 400
    
    total = boletos * precio
    
    if boletos > 5:
        total *= 0.85
    elif boletos >= 3:
        total *= 0.90
    
    if cineco == "si":
        total *= 0.90
    
    return jsonify({"total": f"${total:.2f}"})


@app.route("/zodiacoChino")
def zodiaco():
    return render_template("zodiacoChino.html")

def signo_chino(anio):
    signos_chinos = {
        "Rata": [1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020],
        "Buey": [1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021],
        "Tigre": [1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022],
        "Conejo": [1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023],
        "Dragón": [1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024],
        "Serpiente": [1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025],
        "Caballo": [1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026],
        "Cabra": [1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027],
        "Mono": [1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028],
        "Gallo": [1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029],
        "Perro": [1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030],
        "Cerdo": [1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031]
    }

    imagenes = {
        "Rata": url_for('static', filename='img/rata.png'),
        "Buey": url_for('static', filename='img/wey.png'),
        "Tigre": url_for('static', filename='img/tigre.png'),
        "Conejo": url_for('static', filename='img/conejo.png'),
        "Dragón": url_for('static', filename='img/dragon.png'),
        "Serpiente": url_for('static', filename='img/serpiente.png'),
        "Caballo": url_for('static', filename='img/caballo.png'),
        "Cabra": url_for('static', filename='img/cabra.png'),
        "Mono": url_for('static', filename='img/mono.png'),
        "Gallo": url_for('static', filename='img/gallo.png'),
        "Perro": url_for('static', filename='img/perro.png'),
        "Cerdo": url_for('static', filename='img/cerdo.png')
    }

    for signo, años in signos_chinos.items():
        if anio in años:
            return signo, imagenes[signo]

@app.route('/zodiacoChino', methods=['POST'])
def zodiaco_chino():
    nombre = request.form.get('nombre')
    apaterno = request.form.get('apaterno')
    amaterno = request.form.get('amaterno')
    anio = int(request.form.get('anio'))
    
    edad = 2025 - anio
    resultado_signo, imagen = signo_chino(anio)

    return jsonify({
        "nombre": nombre,
        "apaterno": apaterno,
        "amaterno": amaterno,
        "edad": edad,
        "signo_chino": resultado_signo,
        "imagen": imagen
    })

if __name__ == "__main__":
    app.run(debug=True,port=3000)