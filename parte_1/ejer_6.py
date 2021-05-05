print("Conversora de millas y galones a metros y litros")
letra = input("Ingrese M para millas o G para galones: ")

metros = 0
litros = 0

if  letra.capitalize() == "M":
    millas = float(input("Ingrese millas a covertir a metros: "))
    metros = millas * 1.6
    print(f"son {metros:.2f} metros")
else:
    galones = float(input("Ingrese galones a covertir a litros: "))
    litros = galones * 3.7
    print(f"son {litros:.2f} litros")


