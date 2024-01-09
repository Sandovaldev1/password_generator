from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar_contrasena', methods=['POST'])
def generar_contrasena():

    try:
        selector_longitud = int(request.form['selector_longitud'])
        contrasena_generada = generar_contrasenas(selector_longitud)

        if selector_longitud not in[8, 9, 10, 11, 12]:
            raise ValueError("La longitud debe ser 8 o 12 para generar una contraseña segura.")
        
        return render_template('index.html', contrasena_generada=contrasena_generada, error=None)
    except ValueError as e:
        return render_template('index.html', contrasena_generada=None, error=str(e))
    
def generar_contrasenas(longitud=12):
    letras = string.ascii_uppercase
    numeros = string.digits   

    contrasena = random.sample(letras, k= longitud // 2) + random.sample(numeros, k=longitud // 2)
    random.shuffle(contrasena)
    
    contrasena = 'Tu nueva contraseña es: ' + ''.join(contrasena)

    return contrasena

if __name__ == '__main__':
    app.run(debug=True)