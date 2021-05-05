segundos = int(input("Ingrese cantidad de segundos: "))

horas = int(segundos / 3600)
segundos = int(segundos - (3600 * horas))
minutos = int(segundos / 60)
segundos = int(segundos - (60 * minutos))


print(f"son {horas} h {minutos} min {segundos} seg")
