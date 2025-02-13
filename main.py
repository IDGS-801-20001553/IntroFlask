from flask import Flask, render_template, request , jsonify

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

if __name__ == "__main__":
    app.run(debug=True,port=3000)