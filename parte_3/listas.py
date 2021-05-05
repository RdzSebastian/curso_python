#1. Escribe un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego
#solicitar esa cantidad de palabras para crear la lista. Por último, el programa tiene que emitir la lista.
'''
cantidad_palabras = int(input("Ingrese el tamaño de la lista: "))
palabras = []
for i in range(cantidad_palabras):
    palabra = input(f"Ingrese palabra numero {i+1}: ")
    palabras.append(palabra)

print(palabras)
'''

#2. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas
#veces aparece esa palabra en la lista.
'''
palabras = ['jamon', 'tomate', 'tomate', 'lechuga', 'lechuga', 'lechuga']
print(palabras)

palabra = input(f"Ingrese palabra a buscar: ")
j=0
for i in range(len(palabras)):
    if palabra == palabras[i]:
        j += 1

print(f"la palabra {palabra} se encuentra {j} veces" )
'''

#3. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y sustituya la
#primera (que debe estar en la lista) por la segunda. Emitir la lista.
'''
palabras = ['jamon', 'tomate', 'lechuga']
print(palabras)

palabra = input(f"Ingrese palabra a reemplazar: ")
reemplazo = input(f"Ingrese reemplazo: ")

for i in range(len(palabras)):
    if palabra == palabras[i]:
       palabras[i] = reemplazo

print(palabras)
'''

#4. Escribe un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y elimine esa
#palabra de la lista.
'''
palabras = ['jamon', 'tomate', 'tomate', 'lechuga', 'lechuga', 'lechuga']
print(palabras)

palabra = input(f"Ingrese palabra a eliminar: ") 
i = 0

while i < len(palabras):
    if palabra == palabras[i]:
        del palabras[i]
    else:
        i += 1

print(palabras)
'''

#5. Escribe un programa que permita crear dos listas de palabras y que, a continuación, elimine de la primera lista los
#nombres de la segunda lista.
'''
palabras1 = ['queso', 'pepino', 'queso', 'queso', 'tomate', 'lechuga', 'lechuga', 'tomate','tomate', 'tomate']
palabras2 = ['queso', 'tomate', 'lechuga']
print(f"Lista 1: {palabras1}")
print(f"Lista 2: {palabras2}")

i = 0
while i < len(palabras1):
    for j in range(len(palabras2)):
        if palabras1[i] == palabras2[j]:
            del palabras1[i]
            i -= 1
            break
    i += 1

print(f"Lista 2: {palabras1}")
'''

#6. Escribe un programa que permita crear una lista de palabras y que, a continuación, cree una segunda lista igual a la
#primera, pero al revés (crear una lista distinta).
'''
palabras = ['queso', 'tomate', 'lechuga']
print(palabras)

palabras_invertidas = []

for i in range(len(palabras)):
    palabras_invertidas.append(palabras[len(palabras) - i - 1])

print(palabras_invertidas)
'''