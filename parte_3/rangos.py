#1. Escribe un tipo range() que emita: [100, 101, 102, 103]
'''
print(list(range(100,104)))
'''

#2. Escribe un tipo range() que emita: [-50, -2050, -4050, -6050]
'''
print(list(range(-50,-8050,-2000)))
'''
#3. Escribe un programa que pida un número entero y emita una lista de números consecutivos del 0 al valor dado.
'''
numero = int(input("Ingrese un numero entero: "))
print(list(range(0,numero+1)))
'''

#4. Escribe un programa que pida dos números enteros (el segundo mayor que el primero) y emita listas de números consecutivos al derecho y al revés.
'''
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero mayor al anterior: "))
print(list(range(numero1,numero2+1)))
print(list(range(numero2,numero1-1,-1)))
'''

#5. Escribe un programa que pida dos números enteros y emita la lista de números consecutivos que hay entre ellos, de menor a mayor.
'''
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero mayor al anterior: "))
print(list(range(numero1+1,numero2)))
'''

#6. Escribe un programa que pida dos números enteros y emita la lista de números pares que hay entre ellos (incluidos ellos mismos si son pares)
'''
numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero mayor al anterior: "))

if (numero1 % 2) == 0 and (numero2 % 2) == 0:
    print(list(range(numero1,numero2+1,2)))
elif (numero1 % 2) != 0 and (numero2 % 2) != 0:
    numero1 += 1
    print(list(range(numero1,numero2,2)))
elif (numero1 % 2) != 0:
    numero1 += 1
    print(list(range(numero1,numero2+1,2)))
elif (numero2 % 2) != 0:
    print(list(range(numero1,numero2,2)))
'''

#7. Escribe tres programas que emitan las siguientes secuencias de números:
# * En el primer programa, el tipo range() que se utilice en cada bucle debe tener un único argumento.
# * En el segundo programa, el tipo range() que se utilice en cada bucle debe tener dos argumentos.
# * En el tercer programa, el tipo range() que se utilice en cada bucle debe tener tres argumentos.
'''
print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,1)))
'''



