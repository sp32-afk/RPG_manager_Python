from flask import Flask
from controllers.personaje_controller import personaje_bp

app = Flask(__name__)
app.register_blueprint(personaje_bp)

if __name__ == '__main__':
    app.run(debug=True)