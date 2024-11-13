from flask import Flask, render_template, request
app = Flask(__name__)
# Instancia de app Flask

# Ruta de página principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ruta de ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        resultado = None
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = sum([nota1, nota2, nota3]) / 3

        if promedio >= 40 and asistencia >= 75:
            resultado = "APROBADO"
        else:
            resultado = "REPROBADO"
        return render_template('ejercicio1.html', promedio= promedio, resultado=resultado, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia)
    return render_template('ejercicio1.html')

# Ruta de ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        maximo = None
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])

        chrnombre1 = int(len(nombre1))
        chrnombre2 = int(len(nombre2))
        chrnombre3 = int(len(nombre3))

        maximoC = max(chrnombre1, chrnombre2,chrnombre3)

        if maximoC == chrnombre1:
            maximo = str(nombre1)

        elif maximoC == chrnombre2:
            maximo = str(nombre2)

        else:
            maximo = str(nombre3)

        return render_template('ejercicio2.html', maximo=maximo, maximoC=maximoC)
    return render_template('ejercicio2.html')

# Ejecución y modo depuración
if __name__ == '__main__':
    app.run(debug=True)