partido = input("Ingrese a que partido va a votar (A / B / C): ")
partido = partido.capitalize()

if partido == "A":
    print("Usted ha votado por el partido rojo")
elif partido == "B":
    print("Usted ha votado por el partido verde")
elif partido == "C":
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")
