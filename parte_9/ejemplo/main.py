# obtengo la ruta
import os
print(os.getcwd())

# escribo el path de la ruta donde ejecutaré el script
import sys
sys.path.append('c:/Users/Notebook/Documents/git/curso_python/parte_9/ejemplo/paquete')
# Documentación de importación de módulos
# https://docs.python.org/es/3/tutorial/modules.html#intra-package-references

# importo clases y funciones (según la documentación hacer from .... import * no es recomendable)

from paquete.modulo import Restaurante, Cliente, Hotel, Gerente, Mozo, Encargado, marcacionTrabajador

rest1 = Restaurante('Rest_1', '30-11111111-8', 3, 'Comida rápida')
rest2 = Restaurante('Rest_2', '30-22222222-7', 2, 'Para llevar')
print(rest1)
print(rest2)

geren1 = Gerente('12341234', 'Pepe')
geren2 = Gerente('43214321', 'Pepito')
print(geren1)
print(geren2)

mozo1 = Mozo()
marcacionTrabajador(mozo1)
print(geren1.marcacion())
print(geren2.marcacion())

cliente1 = Cliente('Pachi')
cliente1.factura(2000)
print(cliente1)

cliente2 = Cliente('Lola')
cliente2.factura(1500)
print(cliente2)

hotel1 = Hotel('Hotel Python', '30-12341234-9', 5,
               'Boutique', geren1.dni, geren1.apellido, 'Si')
print(hotel1)

hotel2 = Hotel('Hotel Super-Python', '30-43214321-5', 5,
               'Excepcional', geren2.dni, geren2.apellido, 'Si')
print(hotel2)

rest3 = Restaurante('Rest 3', '30-11111111-9', 2, 'Buffet')
rest4 = Restaurante('Rest 4', '30-22222222-7', 3, 'Especialidad')
rest5 = Restaurante('Rest 5', '30-33333333-5', 5, 'Temático')
rest6 = Restaurante('Rest 6', '30-44444444-3', 4, 'Comida rápida')
print(Restaurante.restaurantes)

print(rest1)
print(rest2)
print(rest3)
print(rest4)
print(rest5)
print(rest6)
