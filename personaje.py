from flask import Flask
from flask import jsonify
app = Flask(__name__)

class Personaje:
    def __init__(self, nombre, clase, nivel, vida):
        self.nombre =nombre
        self.clase = clase
        self.nivel = nivel
        self.vida = vida

Personaje1 = Personaje("Atreuz","Guerrero", 23, 100)
Personaje2 = Personaje("Muad'Dib", "Profeta", 56, 100)

personajes = [
    {"nombre": Personaje1.nombre, "clase": Personaje1.clase, "nivel": Personaje1.nivel, "vida": Personaje1.vida},
    {"nombre": Personaje2.nombre, "clase": Personaje2.clase, "nivel": Personaje2.nivel, "vida": Personaje2.vida}
]
@app.route('/personajes')
def obtener_personaje():
    return jsonify(personajes)

if __name__ == '__main__':
    app.run(debug=True)