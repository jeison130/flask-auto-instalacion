from src.config.db import DB


class ProductosModel():
    def traerTodos(self):
        cursor = DB.cursor()

        cursor.execute('select * from productos ')

        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre,descripcion,precio_compra, precio_venta):
        cursor = DB.cursor()

        cursor.execute('insert into productos(nombre,descripcion,precio_compra,precio_venta) values(?,?,?,?)', (nombre,descripcion,precio_compra,precio_venta))
        
        cursor.close()
        
        