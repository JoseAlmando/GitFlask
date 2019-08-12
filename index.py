from flask import Flask #Importar Flask

app = Flask(__name__) 

@app.route("/") #Decorador
def index():
    return "Hello Jose!"

@app.route("/hola") #Urls
def hola():
    return "Hola!"

@app.route("/users/<string:usuario>") #urls con variables
def users(usuario):
    return "Hola "+usuario    

@app.route("/numero/<int:x>") #urls con variables
def numero(x):
    return f"Numero {x}"   


@app.route("/users/<int:id>/<string:usuario>") #urls con variables
def username(id, usuario):
    return "Hola "+usuario+" Numero {}".format(id)  

@app.route("/default/")
@app.route("/default/<string:dft>")
def dft(dft):
    return "Mensaje: "+dft

if __name__ == "__main__":
    app.run(debug=True, port=5000) #!debug, para detectar cambios y reiniciar server
                        #port, para el puerto