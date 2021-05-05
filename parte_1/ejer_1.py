""" ESTAS COMILLAS SON PARA PONER
COMENTARIOS DE MAS DE UNA LINEA"""

# PARA COMENTARIOS EN UNA LINEA UTILIZAMOS #
tunombre=input("Ingresa tu nombre:")
print(f"Hola {tunombre}!!!")

# Para cargar por teclado una cadena de caracteres utilizamos la función input
# usamos variables para almacenar el valor introducido por teclado
nombre1=input("ingrese nombre del producto:")
precio1=int(input("ingrese un precio:"))
nombre2=input("ingrese nombre del producto:")
precio2=int(input("ingrese otro precio:"))

# esta es una constante
BONIFICACION = 20

# sumamos los dos precios y su resultado lo guardamos en una variable
precio_total = precio1 + precio2 # operador aritmético +
print(f"El precio total es: {precio_total}")
print(f"Resultados de la suma de producto {nombre1} y del producto {nombre2}.:")

# concatenar se puede hacer de esta manera con el signo + y en la variable la propiedad str
print ("la suma de los dos productos es:" + str(precio_total))
""" VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO """
precio_total += BONIFICACION # operador de asignación compacta
print ("al precio total le incrementamos su valor que tiene la constante:" + str(precio_total))

#Prueba el programa desde VSC guardándolo con un nombre y la extensión .py