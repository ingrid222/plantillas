from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "instituto": ["Instituto Superior de Formación  Técnica No. 12 - Ara General Belgrano"],
    "direccion": ["Calle 76 n°611 e/7 y 8, Villa Elvira, La Plata, Pcia. de Bs.As."],
    "donde queda el Instituto": ["Calle 76 n°611 e/7 y 8, Villa Elvira, La Plata, Pcia. de Bs.As."],
    "direccion?": ["Calle 76 n°611 e/7 y 8, Villa Elvira, La Plata, Pcia. de Bs.As."],
    "dirección?": ["Calle 76 n°611 e/7 y 8, Villa Elvira, La Plata, Pcia. de Bs.As."],
    "especialidades": ["El Instituto Superior de Formación  Técnica No. 12 ofrece las siguientes especialidades: - Tecnico Superior en Seguridad e Higiene,Tecnico Superior en Desarrollo de Software,Tecnico Superior en Ceremonial y Protocolo,Tecnico Superior en Administracion "],
    "correo": ["Correo electrónico: tecnicai12delaplata@eest5.com"],
    "default": ["No estoy seguro de entender completamente.", "Podrías reformular la pregunta?"],
    "telefono": ["El telefono de el Instituto es: 0221 452 1954"],
    "teléfono": ["El telefono de el Instituto es: 0221 452 1954"],
    "que especialidades hay en el Instituto?": ["Las especialidades son: Tecnico Superior en Seguridad e Higiene,Tecnico Superior en Desarrollo de Software,Tecnico Spoerior en Ceremonial y Protocolo,Tecnico Superior en Administracion "],
    "que especialidades hay?": ["Tecnico Superior en Seguridad e Higiene,Tecnico Superior en Desarrollo de Software,Tecnico Superior en Ceremonial y Protocolo,Tecnico Superior en Administracion "],
    #"Especialidades": ["Tecnico Superior en Seguridad e Higiene,Tecnico Superior en Desarrollo de Software,Tecnico Superior en Ceremonial y Protocolo,Tecnico Superior en Administracion ],
    "asignaturas":["Tecnico Superior en Seguridad e Higiene,Tecnico Superior en Desarrollo de Software,Tecnico Superior en Ceremonial y Protocolo,Tecnico Superior en Administracion"],
    "asignatura": ["Tecnico Superior en Seguridad e Higiene,Tecnico Superior en Desarrollo de Software,Tecnico Superior en Ceremonial y Protocolo,Tecnico Superior en Administracion"],
    "app de el Instituto": ["La app de el Instituto se llama: Instituto Técnico 12 La Plata"],
    "aplicacion":  ["La app de el Instituto se llama: Instituto Técnico 12 La Plata"],
    "app":  ["La app de el Instituto se llama: Instituto Técnico 12 La Plata"],
    "aplicacion de el Instituto":  ["La app de el Instituto se llama: Instituto Técnico 12 La Plata"],
    "instituto": ["El Instituto se llama: Instituto  Superior de Formación Técnica N°12 - Ara General Belgrano"],
    "ayuda": ["Por supuesto, ¿en qué puedo ayudarte?", "Estoy aquí para vos."],
    "default": ["No estoy seguro de entender completamente.", "Podrías reformular la pregunta?"],
    "hola": ["Hola"],
    "Hola": ["Hola"],
    "chau": ["Chau"],
    "Chau": ["Chau"],
    "gracias": ["De nada"],
    "Gracias": ["De nada"],
    "saludos": ["Saludos"],
    "Saludos": ["Saludos"],
    "Buen día": ["Buen día"],
    "buen día": ["Buen día"],
    "buen dia": ["Buen día"],
    "Buenas tardes": ["Buenas tardes"],
    "buenas tardes": ["Buenas tardes"],
    "buenas noches": ["Buenas noches"],
    "Buenas noches": ["Buenas noches"]
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"].lower()
    response = responses.get(user_input, random.choice(responses["default"]))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
