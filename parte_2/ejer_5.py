anio = int(input("Ingrese un año: "))

if ((anio % 4) == 0 and not (anio % 100) == 0) or ((anio % 4) == 0 and (anio % 100) == 0 and (anio % 400) == 0):
    print("Es año biciesto")
else: 
    print("No es año biciesto")
