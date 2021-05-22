#En en una escuela de 1000 alumnos, se han evaluado literatura, matemática y biología, obteniéndose los
# siguientes resultados:


# 1. declaraciones
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

#490 aprobaron matemática. Los datos de la evaluación de Matemática se registraron en una lista:
matematica = [34, 40, 61, 75, 87, 90, 103]

#320 aprobaron biología. Los datos de la evaluación de Biología se registraron en una tupla:
biologia = (40, 50, 60, 75, 34, 61)

#680 aprobaron literatura. Los datos de la evaluación de Literatura se registraron en un diccionario:
literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
 "Antigüa": 56, "Poesía": 131, "Cuento": 87, "Novela": 103}


# 2. definir funciones de control (opcional) y otras (necesarias)
def aprobaron_las_tres(x, y, z):
    return x.intersection(y, z)

def aprobaron_dos(x, y):
    return x.intersection(y)

def dibujar_respuesta(eje_x, eje_y, mensaje):
    plt.text(eje_x, eje_y,  
         s=mensaje,
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),)) 


# 3. convertir en set las estructuras
total_alumnos = {1000}

# Aprobaron matemática
M = set(matematica)

# Aprobaron biología
B = set(biologia)

# Aprobaron literatura
L = set(literatura.values())


# 4. Resolver las preguntas y resto de opciones para armar el gráfico
aprobaron_las_tres = aprobaron_las_tres(M, B, L)
M -= aprobaron_las_tres
B -= aprobaron_las_tres
L -= aprobaron_las_tres

# aprobaron matemática y biología
M_B = aprobaron_dos(M, B)
M -= M_B
B -= M_B

# aprobaron matemática y literatura
M_L = aprobaron_dos(M, L)
M -= M_L
L -= M_L

# aprobaron biología y literatura
B_L = aprobaron_dos(B, L)
B -= B_L
L -= B_L

# Respuestas
dibujar_respuesta(-0.60, -1.00, "Respuestas: ")
#A)
dibujar_respuesta(-0.60, -1.10, f"Aprobaron biología, matemática y literatura: {sum(aprobaron_las_tres)}")
#B)
dibujar_respuesta(-0.60, -1.20, f"Literatura y matemática: {sum(M_L)}")
#C)
dibujar_respuesta(-0.60, -1.30, f"Solo literatura: {sum(L)}")
#D)
dibujar_respuesta(-0.60, -1.40, f"Solo biología: {sum(B)}")
#E)
dibujar_respuesta(-0.60, -1.50, f"Solo matemática: {sum(M)}")
#F)
dibujar_respuesta(-0.60, -1.60, f"Aprobaron 2 de 3 examenes: {sum(M_B) + sum(M_L) + sum(B_L)}")


# 5. Definir diagrama de Venn, gráfico y respuestas.
lista = [aprobaron_las_tres, M_B, M_L, M, B_L, B, L]
target = ["111", "110", "101", "100", "011", "010", "001"]
diagram = venn3(subsets=(1,1,1,1,1,1,1), set_labels=('Matematica', 'Biologia', 'Literatura'))

for subset, seet in zip(target, lista):
    diagram.get_label_by_id(subset).set_text(sum(seet))

venn3_circles(subsets=(1,1,1,1,1,1,1),alpha=1,linestyle="-.",linewidth=2)

plt.text(-0.80, -0.75, f"Total alumnos: {sum(total_alumnos)}", size=8) 
plt.text(-0.80, -0.85, f"No aprobaron ningun examen: {0}", size=8)
          
plt.title("Resueltados de examenes de escuela")
plt.show()