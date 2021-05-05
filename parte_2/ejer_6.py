dia=input("Ingrese un dia de la semana: ")
cantidad_alumnos = 30

if dia == "lunes":
    print("Día de nivel inicial")
    examenes = input("Se tomaron examenes (S / N) ")
    if examenes.capitalize() == "S":
        aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
        porcentaje_aprobado = (aprobados / cantidad_alumnos) * 100
        print(f"El porcentaje de aprobados es {porcentaje_aprobado:.0f}%")
elif dia == "martes":
    print("Día de nivel intermedio")
    examenes = input("Se tomaron examenes (S / N) ")
    if examenes.capitalize() == "S":
        aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
        porcentaje_aprobado = (aprobados / cantidad_alumnos) * 100
        print(f"El porcentaje de aprobados es {porcentaje_aprobado:.0f}%")
elif dia == "miercoles":
    print("Día de nivel avanzado")
    examenes = input("Se tomaron examenes (S / N) ")
    if examenes.capitalize() == "S":
        aprobados = int(input("Ingrese cantidad de alumnos aprobados: "))
        porcentaje_aprobado = (aprobados / cantidad_alumnos) * 100
        print(f"El porcentaje de aprobados es {porcentaje_aprobado:.0f}%")
elif dia == "jueves":
    print("Día de practica")
    porcentaje_asistencia = int(input("Ingrese porcentaje de asistencia: "))
    if porcentaje_asistencia > 50:
        print("asistió la mayoría")
    else:
        print("no asistió la mayoría")
else:
    print("Día de consulta")
    cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
    arancel = int(input("Ingrese arancel por alumno: "))
    total = cantidad_alumnos * arancel
    print(f"El total de ingreso fue ${total}")