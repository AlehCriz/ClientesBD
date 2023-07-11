from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from cliente import Cliente

db = dbase.dbConnection()

app = Flask(__name__)

#home
@app.route('/')
def home():
    clientes = db['clientes']
    clientesReceived = clientes.find({"visible": 1})
    return render_template('index.html', clientes = clientesReceived)

#insert
@app.route('/clientes', methods=['POST'])
def addcliente():
    clientes = db['clientes']
    rut = request.form['rut']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']
    visible = 1

    if rut and nombre and direccion and telefono and email and visible:
        cliente = Cliente(rut, nombre, direccion, telefono, email, visible)
        clientes.insert_one(cliente.toDBCollection())
        response: jsonify({
            'rut': rut,
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'email': email,
            'visible': 1
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#delete
@app.route('/delete/<string:cliente_rut>')
def delete(cliente_rut):
    clientes = db['clientes']
    clientes.update_one({"rut": cliente_rut}, {"$set": {
        'visible': 0
    }})
    return redirect(url_for('home'))

#update
@app.route('/edit/<string:cliente_rut>', methods=['POST'])
def editCliente(cliente_rut):
    clientes = db['clientes']
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    telefono = request.form['telefono']
    email = request.form['email']

    if nombre and direccion and telefono and email:
        clientes.update_one({"rut": cliente_rut}, {"$set": {
            'nombre': nombre,
            'direccion': direccion,
            'telefono': telefono,
            'email': email,
        }})
        response = jsonify({"message": "Cliente actualizado" + cliente_rut})
        return redirect(url_for('home'))
    else:
        return notFound()
    
#error
@app.errorhandler
def notFound(error=None):
    message ={
        "message": "No encontrado" + request.url,
        "status": "404"
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True, port=1707)
