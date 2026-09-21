from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.personaje import Personaje
from services.personaje_service import es_valido

personaje_bp = Blueprint('personaje', __name__)

lista_de_personajes = [
    Personaje("Atreuz", "Guerrero", 23, 100),
    Personaje("Muad'Dib", "Mago", 56, 100)
]

@personaje_bp.route('/', methods=['GET', 'POST'])
def personajes():
    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        clase = request.form.get('clase')
        
        try:
            nivel = int(request.form.get('nivel'))
        except (ValueError, TypeError):
            nivel = 0

        # Validación con la Capa de Negocio
        if not es_valido(nombre, clase, nivel):
            error = "Datos de personaje no válidos. Clases permitidas: Guerrero, Mago, Arquero."
        else:
            nuevo_personaje = Personaje(nombre, clase, nivel, 100)
            lista_de_personajes.append(nuevo_personaje)
            return redirect(url_for('personaje.personajes'))

    return render_template('personajes.html', lista_personajes=lista_de_personajes, error=error)