from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def principal():
    columnas = 8
    filas = 8
    return render_template('index.html', columnas=int(columnas), filas=int(filas))

@app.route('/<nfilas>', methods=['GET'])
def actualiza(nfilas=8):
    columnas = 8
    filas = nfilas
    return render_template('index.html', columnas=int(columnas), filas=int(filas))

@app.route('/<nfilas>/<ncolumnas>', methods=['GET'])
def actualizaFC(nfilas=8, ncolumnas=8):
    columnas = ncolumnas
    filas = nfilas
    return render_template('index.html', columnas=int(columnas), filas=int(filas))

@app.route('/<nfilas>/<ncolumnas>/<color1>/<color2>', methods=['GET'])
def actualizarFCColor(nfilas=8, ncolumnas=8, color1="red", color2="black"):
    columnas = ncolumnas
    filas = nfilas
    nColor1 = color1
    nColor2 = color2
    return render_template('index.html', columnas=int(columnas), filas=int(filas), color1=nColor1, color2=nColor2)

if __name__ == "__main__":
    app.run(debug=True)
