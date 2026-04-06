from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Base de datos simple (memoria)
movimientos = []

@app.route('/')
def index():
    stock = {}

    for m in movimientos:
        nombre = m["medicamento"]
        cantidad = int(m["cantidad"])

        if nombre not in stock:
            stock[nombre] = 0

        if m["tipo"] == "Entrada":
            stock[nombre] += cantidad
        else:
            stock[nombre] -= cantidad

    return render_template("index.html", movimientos=movimientos, stock=stock)


@app.route('/agregar', methods=['POST'])
def agregar():
    data = {
        "medicamento": request.form['medicamento'],
        "tipo": request.form['tipo'],
        "cantidad": request.form['cantidad'],
        "paciente": request.form['paciente'],
        "usuario": request.form['usuario']
    }

    movimientos.append(data)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
