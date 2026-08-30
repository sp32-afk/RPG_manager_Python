from flask import Blueprint, render_template
from models.personaje import Personaje

personaje_bp = Blueprint('personaje', __name__)

# Datos en memoria (Taverna)
personajes = [
    Personaje("Atreuz", "Guerrero", 23, 100),
    Personaje("Muad'Dib", "Profeta", 56, 100)
]

@personaje_bp.route('/personajes')
def listar_personajes():
    # El controlador recibe los datos del modelo y se los pasa a la Vista
    return render_template('personajes.html', lista_personajes=personajes)