from flask import Blueprint, render_template
from models.personaje import Personaje
from flask import request, redirect, url_for
from services.personaje_service import es_valido

personaje_bp = Blueprint('personaje', __name__)

# Datos en memoria 
lista_de_personajes = [
    Personaje("Atreuz", "Guerrero", 23, 100),
    Personaje("Muad'Dib", "Profeta", 56, 100)
]

@personaje_bp.route('/personajes', methods=['GET', 'POST'])
def personajes():
        if request.method == 'POST':
            # Extrae los datos que vienen del HTML
            nombre = request.form.get('nombre')
            clase = request.form.get('clase')
            nivel = int(request.form.get('nivel'))

            # Instancia y guarda el nuevo personaje en la lista del modelo
            nuevo_personaje = Personaje(nombre, clase, nivel, 100)

            if not es_valido(nombre, clase, nivel):
                return jsonify({"error": "Datos inválidos"}), 400
            else:
                return jsonify({"message": "Datos válidos"}), 200

            lista_de_personajes.append(nuevo_personaje)
        
            # Redirige a la misma ruta para actualizar la pantalla
            return redirect(url_for('personaje.personajes'))
        
            # Si es GET (al cargar la pagina por primera vez):
        return render_template('personajes.html', lista_personajes=lista_de_personajes)

