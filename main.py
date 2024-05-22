from db import Session, engine, Model
from modelos import *
from sqlalchemy import select

def main():
    Model.metadata.drop_all(bind=engine)
    Model.metadata.create_all(bind=engine)
    # Primera parte del ejercicio
    # # session = Session()
    # # p = Producto(codigo='AB12345', nombre='MiFi 5G', costo=100, precio=500)
    # # session.add(p)
    # # p2 = Producto(codigo='ZW9955', nombre='Micro TONOR', costo=10, precio=60)
    # # session.add(p2)
    # # session.commit()
    #
    # session = Session()
    # query = select(Producto)
    # # print(query)
    # # resultado = session.execute(query).all()
    # # print(resultado)
    # resultado = session.execute(query)
    # print(resultado)
    #
    # # resultado2 = session.scalars(query).all()
    # # print(resultado2)
    #
    # resultado2 = session.scalars(query)
    #
    # # desde scalars
    # for producto in resultado2:
    #     print(producto.codigo, producto.nombre, producto.precio)
    #
    # # desde execute
    # for producto_tupla in resultado:
    #     print(producto_tupla[0].codigo, producto_tupla[0].nombre, producto_tupla[0].precio)


if __name__ == '__main__':
    main()