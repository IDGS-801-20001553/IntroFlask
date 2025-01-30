from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello word!</h1>"


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



if __name__ == "__main__":
    app.run(debug=True,port=3000)