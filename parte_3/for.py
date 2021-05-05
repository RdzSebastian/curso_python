#1. Escribe un programa que le permita realizar la escritura de los primeros 100 números naturales.
'''
for i in range(100):
    print(i+1)
'''

#2. Escribe un programa que le permita realizar la suma de los primeros N números impares. El N debe ingresarse por
#teclado.

'''
n = int(input("Ingrese un numero y se sumaran todos los numeros impares desde el 0 hasta ese numero: "))
suma_numeros_impares = 0

for i in range(n+1):
    if i%2 != 0:
        suma_numeros_impares += i
    
print(suma_numeros_impares)
'''

#3. Escribe un programa que calcule el factorial de un número cualquiera que se ingresa por teclado.
'''
n = int(input("Ingrese un numero y se hara el factorial: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i
    
print(factorial)
'''

#4. Muestre los N primeros números de la secuencia de Fibonacci, siendo n un dato entero. 
'''
n = int(input("Ingrese un numero y se mostrara esa cantidad de numeros de la secuencia de fibonacci: "))
a = 0
b = 1
    
for i in range(n):
    c = b+a
    a = b
    b = c
    print(c)
'''

