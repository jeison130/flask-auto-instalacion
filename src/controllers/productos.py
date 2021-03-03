from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel

@app.route('/productos')
def productos():
    productosModel =ProductosModel()

    productos = productosModel.traerTodos()
   
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods =['GET', 'POST'])
def crear_producto():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
       #mostramos el formulario de cracion
        return render_template('productos/crear.html')

    nombre = request.form.get('nombre')
    productosModel = ProductosModel()

    productosModel.crear(nombre)
    

    #aca es la cracion del producto
    return redirect(url_for('productos'))
