from flask import Flask
import random

app = Flask(__name__)

list = [
    'Gato',
    'Perro',
    'Leon',
    'Tigre',
    'Pato'
]

@app.route("/")
def home():
    return f"""
    <h1> ¡Bienvenido! </h1>
    <a href = "/random.animal"> ¿Un animal? </a>
    <a href = "/random.number"> Adivina un número </a>

    """

@app.route("/random.animal")
def random_animal():
    return f"""
    <p> {random.choice(list)} </p>
    <a href = "/"> Volver al inicio </a>
    """
@app.route("/random.number")
def random_number():
    return f"""
    <h1> {random.randint(1,100)} </h1>
    <a href = "/"> Volver al inicio </a>
    """
app.run(debug = True)
