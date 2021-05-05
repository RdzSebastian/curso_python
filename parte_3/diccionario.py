#1. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono (no es necesario validar). Tendrás
#que ir pidiendo contactos hasta el usuario diga que no quiere insertar más. No se podrán ingresar nombres repetidos.

#diccionario= {"Juan" : 23, "Jose" : 20, "Pedro" : 26}
#d = dict(Python=1991, C=1972, Java=1996)
'''
diccionario = {}
sigue = True
while(sigue):
    nombre = input(f"Ingrese nombre de usuario o 'stop' para terminar: ")
    if(nombre == "stop"):
        sigue = False
    else:
        telefono = int(input(f"Ingrese telefono del usuario: "))
        if(nombre not in diccionario):
            diccionario[nombre] = telefono

print(diccionario)
'''

#2. Crear un programa donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. El programa
#pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los
#datos guardados en el diccionario. Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntar
#á si queremos hacer otra consulta.
'''
diccionario = {"frutilla" : 3, "limon" : 4, "manzana" : 1}
sigue = True
while(sigue):
    fruta = input(f"Ingrese la fruta vendida o stop para terminar: ")
    if(fruta == "stop"):
        sigue = False
    else:
        print(f"el precio de {fruta}: " + str(diccionario.get(fruta, "Error no está en el diccionario")))
         
    if(fruta in diccionario):
        precio = diccionario.get(fruta)
        precio *= int(input(f"Ingrese cantidad de kilos vendidos: "))
        print(f"El precio final es {precio}")
'''

#3. Codifica un programa que permita guardar los nombres de alumnos de una clase y las notas que han obtenido. Cada
#alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres
#de los alumnos y los valores serán listas con las notas de cada alumno. El programa pedirá el número de alumnos que
#vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. Al final el
#programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el
#nombre de un alumno que ya existe el programa nos dará un error

diccionario = {}
notas = []

cantidad_alumnos = int(input(f"Ingrese cantidad de alumnos a ingresar: "))

for i in range(cantidad_alumnos):
    alumno = input(f"Ingrese nombre del alumno {i+1}: ")
    
    if(alumno in diccionario):
        print(f"El alumno con nombre {alumno} ya ha sido ingresado, intente con otro")
    else:
        nota = 0
        while nota >= 0:
            nota = int(input(f"Ingrese nota o un numero negativo para terminar: "))
            if nota >= 0:
                notas.append(nota)
        diccionario[alumno] = notas

print(diccionario)