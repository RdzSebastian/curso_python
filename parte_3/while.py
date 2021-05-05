#1. Escribe un programa que pida la cantidad de números positivos que se tienen que ingresar y a continuación 
# pida números hasta que se hayan ingresado la cantidad de números indicada.


#2. Escribe un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea
#mayor que el primero. El programa termina y emitirá los números.

#3. Escribe un programa que pida números decimales mientras el usuario escriba número mayores que el primero.

#4. Escribe un programa que pida números enteros mientras el usuario ingresa números cada vez más grandes, el
#programa emite en cada iteración el número anterior ingresado y finaliza ingresando un número menor.

#5. Escribe un programa que pida números mientras no se escriba un número negativo. El programa terminará emitiendo
#la suma de los números ingresados.

#6. Escribe un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los números
#introducidos supere el límite inicial.

#7. Escribe un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros
#situados entre ellos. El programa terminará cuando se escriba un número que no esté comprendido entre los dos
#valores iniciales y emitirá la cantidad de números ingresados.

numero1 = int(input("Ingrese un numero entero: "))
numero2 = int(input("Ingrese otro numero entero mayor al anterior: "))
esta_entre_ellos = True
numeros_entre_ellos = []

while(esta_entre_ellos):
    numero_entre_ellos = int(input("Ingrese un numero entero que este entre el primer numero ingresado y el segundo (para terminar ponga uno que no): "))
    if (numero1 < numero_entre_ellos and numero2 > numero_entre_ellos):
        numeros_entre_ellos.append(numero_entre_ellos)
    else:
        esta_entre_ellos = False

print(numeros_entre_ellos)

#8. Escribe un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números.
#Para indicar que quiere seguir escribiendo números, el usuario deberá contestar ‘S’ o ‘s’ a la pregunta.