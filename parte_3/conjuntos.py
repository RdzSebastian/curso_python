#1 Diseña un programa que reciba dos conjuntos y devuelva los elementos comunes a ambas, sin repetir ninguno.
#Ejemplo: si recibe los conjuntos [1, 2, 1] y [2, 3, 2, 4], devolverá 2.
'''
conjunto1 = set([1, 2, 1])
conjunto2 = set([2, 3, 2, 4])

print(conjunto1)
print(conjunto2)

print(conjunto1.intersection(conjunto2))
'''

#2 Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen a una o a otra, pero sin repetir
#ninguno. Ejemplo: si recibe los conjuntos [1, 2, 1] y [2, 3, 2, 4], devolverá el conjunto [1, 2, 3, 4].

'''
conjunto1 = set([1, 2, 1])
conjunto2 = set([2, 3, 2, 4])

print(conjunto1)
print(conjunto2)

print(conjunto1.union(conjunto2))
'''

#3 Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen al primero pero no al segundo,
#sin repetir ninguno. Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4], devolverá la lista [1]

'''
conjunto1 = set([1, 2, 1])
conjunto2 = set([2, 3, 2, 4])
print(conjunto1)
print(conjunto2)

print(conjunto1.difference(conjunto2))
'''

#4 Diseña un programa que facilite el trabajo con conjuntos. Recuerda que un conjunto es una lista en la que no hay
#elementos repetidos. Debes implementar:
# a) lista_a_conjunto(lista): Devuelve un conjunto con los mismos elementos que hay en lista, pero sin
#repeticiones. (Ejemplo: lista_a_conjunto([1,1,3,2,3]) devolverá la lista [1, 2, 3] (aunque también se acepta
#como equivalente cualquier permutación de esos mismos elementos, como [3,1,2] o [3,2,1]).
# b) union(A, B): devuelve el conjunto resultante de unir los conjuntos A y B.
# c) interseccion(A, B): devuelve el conjunto cuyos elementos pertenecen a A y a B.
# d) diferencia(A, B): devuelve el conjunto de elementos que pertenecen a A y no a B.
# e) iguales(A, B): devuelve cierto si ambos conjuntos tienen los mismos elementos, y falso en caso contrario. 


print("Para enviar una lista y que se devuelva sin repeticiones ingrese 1")
print("Para mostrar el conjunto resultante de unir los conjuntos A y B ingrese 2")
print("Para mostrar el conjunto cuyos elementos pertenecen a A y a B ingrese 3")
print("Para mostrar el conjunto de elementos que pertenecen a A y no a B ingrese 4")
print("Para saber si son conjuntos iguales ingrese 5 ")
opcion = int(input())
if opcion == 1:
    lista_repetida = [1, 1, 3, 2, 3]
    print(list(set(lista_repetida)))

elif opcion == 2:
    conjunto1 = set([1, 2, 3])
    conjunto2 = set([4, 5, 6 ,7])
    print(conjunto1.union(conjunto2))

elif opcion == 3:
    conjunto1 = set([1, 2, 1])
    conjunto2 = set([2, 3, 2, 4])
    print(conjunto1.intersection(conjunto2))

elif opcion == 4:
    conjunto1 = set([1, 2, 1])
    conjunto2 = set([2, 3, 2, 4])
    print(conjunto1.difference(conjunto2))
    
else:
    conjunto1 = set([1, 2])
    conjunto2 = set([1, 2])
    print(conjunto1 == conjunto2)
    conjunto1 = set([1, 2])
    conjunto2 = set([3, 4])
    print(conjunto1 == conjunto2)
