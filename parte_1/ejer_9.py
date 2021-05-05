payasos = int(input("Ingrese cantidad de payasos vendidos: "))
muñecos = int(input("Ingrese cantidad de muñecas vendidas: "))

payasos_peso = int(payasos * 112)

muñecos_peso = int(muñecos * 75)
peso_total = int(payasos_peso + muñecos_peso)

print(f"El paquete pesara {peso_total} gr")