from flask import Flask

app = Flask(__name__)#Instanciamos Flask con nuestra estancia principal. Se relaciona con el navegador web para pedir cosas.

@app.route('/')#Nos creará una ruta en nuestro servidor.
def hello_world():
    return 'Hola, mundo'

@app.route('/otrorecurso')
def otro():
    return '''
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Mi pagina</title>
        </head>
        <body>
            <h1>Mi saludo</h1>
            <p>Hola, mundo</p>
        </body>
        </html>
        '''
    
