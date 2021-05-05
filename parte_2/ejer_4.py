letra = input("Ingrese una letra: ")
letra = letra.capitalize()

if not len(letra) > 1:
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        print("Es vocal")
else: 
    print("no se puede procesar el dato")
