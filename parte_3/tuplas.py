#1. Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite.
'''
tupla = (1, 2, 3, 4, 5, 1)
numero = int(input("Ingrese un numero entero y le dira cuantas veces se repite en la tupla: "))

print(tupla.count(numero))
'''

#2. Crea una tupla con valores ya predefinidos del 1 al 10, pide un índice por teclado y muestra los valores de la tupla.
'''
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numero = int(input("Ingrese un numero entero para ser usado de indice y motrara dicho el valor dentro de la tupla: "))

#print(tupla.index(numero))
print(tupla[numero])
'''

#3. Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma:
#(nombre, dni, destino). Ejemplo:

lista_viajeros = [("Manuel Juarez", 19823451, "Liverpool"),
    ("Silvana Paredes", 22709128, "Buenos Aires"),
    ("Rosa Ortiz", 15123978, "Glasgow"),
    ("Luciana Hernandez", 38981374, "Lisboa"),
    ("Luciana Hernandez", 38981374, "Lisboa")
]

#Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:

lista_destinos = [("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Londres", "Inglaterra"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")
]

#Hacer un programa que permita al usuario realizar las siguientes operaciones:
#-Agregar pasajeros a la lista de viajeros.
#-Agregar ciudades a la lista de ciudades.
#-Dado el DNI de un pasajero, emitir a qué ciudad y país viaja.
#-Dado un país, mostrar cuántos pasajeros viajan a ese país.
#-Salir del programa.

seguir = True
while(seguir):
    print("Para agregar pasajeros ingrese 1")
    print("Para agregar ciudad y pais ingrese 2")
    print("Para buscar a que ciudad y pais viaja un pasajero segun dni ingrese 3")
    print("Para para buscar cuantos pasajeros viajan a cierto pais ingrese 4")
    opcion = int(input("Para salir ingrese 5 "))
    if opcion == 1:
        nombre = input("Ingrese nombre de pasajero: ")
        dni = int(input("Ingrese dni: "))
        ciudad = input("Ingrese ciudad de destino: ")
        lista_viajeros.append((nombre, dni, ciudad))
    elif opcion == 2:
        ciudad = input("Ingrese ciudad de destino: ")
        pais = input("Ingrese pais de dicha ciudad: ")
        lista_destinos.append((ciudad, pais))
    elif opcion == 3:
        dni_buscar = int(input("Ingrese dni a buscar: "))
        for nombre, dni, ciudad in lista_viajeros:
            if dni_buscar == dni:
                ciudad_viaja = ciudad
                break
        for ciudad, pais in lista_destinos:
            if ciudad == ciudad_viaja:
                pais_viaja = pais
        print(f"El viajero dni: {dni_buscar} viaja a {ciudad_viaja}, {pais_viaja}")
    elif opcion == 4:
        pais_buscar = input("Ingrese pais a buscar: ")
        ciudades_de_pais = []
        cantidad_pasajeros_viajan_pais = 0
        for ciudad, pais in lista_destinos:
            if(pais_buscar == pais):
                ciudades_de_pais.append(ciudad)
        for nombre, dni, ciudad in lista_viajeros:
            for ciudad_de_pais in ciudades_de_pais:
                if ciudad_de_pais == ciudad:
                    cantidad_pasajeros_viajan_pais += 1
        print(cantidad_pasajeros_viajan_pais)
    else:
        seguir = False

