"""4. Se encuesta a 150 familias consultando por el nivel educacional actual de sus hijos.
Los resultados obtenidos son:
 ▪ 10 familias tienen hijos en Enseñanza Básica, Enseñanza Media y Universitaria.{B & M & U}
 ▪ 16 familias tienen hijos en Enseñanza Básica y Universitaria 
 ▪ 30 familias tienen hijos en Enseñanza Media y Enseñanza Básica.
 ▪ 22 familias tienen hijos en Enseñanza Media y Universitaria. 
 ▪ 72 familias tienen hijos en Enseñanza Media. {M}
 ▪ 71 familias tienen hijos en Enseñanza Básica. {B}
 ▪ 38 familias tienen hijos en Enseñanza Universitaria.{U}
Con la información anterior, deducir:
- El número de familias que solo tienen hijos universitarios.
- El número de familias que tienen hijos solo en dos niveles.
- El número de familias que tienen hijos que no estudian.
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

Universal = 150
# ▪ 71 familias tienen hijos en Enseñanza Básica. {B}
B = set({10, 6, 20, 35})
#  ▪ 72 familias tienen hijos en Enseñanza Media. {M}
M = set({10, 20, 12, 30})
#  ▪ 38 familias tienen hijos en Enseñanza Universitaria.{U}
U = set({10, 6, 12, 10})  # elimina el 10 repetido

# control
print(f"B={B}")  # {10, 35, 20, 6}
print(f"M={M}")  # {10, 20, 12, 30}
print(f"U={U}")  # {10, 12, 6} elimina el 10 repetido

#  ▪ 16 familias tienen hijos en Enseñanza Básica y Universitaria {B & U}
print(f"B & U={B & U}")  # {10, 6}
#  ▪ 30 familias tienen hijos en Enseñanza Media y Enseñanza Básica.{M & B}
print(f"M & B={M & B}")  # {10, 20}
#  ▪ 22 familias tienen hijos en Enseñanza Media y Universitaria. {M & U}
print(f"M & U={M & U}")  # {10, 12}


# ▪ 10 familias tienen hijos en Enseñanza Básica, Enseñanza Media y Universitaria.{B & M & U}
# diagram.get_label_by_id("111").set_text(B & M & U)
print(f"B & M & U={B & M & U}")  # {10}

# Con la información anterior, deducir:
# - El número de familias que solo tienen hijos universitarios.
soloU = U - ((B & U)-M) - ((U & M)-B)
print(soloU)

# - El número de familias que tienen hijos solo en dos niveles.
solo2N = ((M & B) ^ (B & U) | (U & M) - (B & M & U))
print(solo2N)
# - El número de familias que tienen hijos que no estudian.
# Calculo los que estudian
Estudian = B | M | U
print(Estudian)

# defino función que suma los elementos para calcular quiénes no Estudian
def suma(conjuntos):
    suma = 0
    for elem in conjuntos:
        suma = suma + elem
    return suma

# tengo que considerar los que estudian y los universitarios ya que al
# estar repetido el valor el grupo de los que estudian no lo toma
# por eso llamo dos veces a la función con distintos conjuntos

noEstudian = Universal - suma(Estudian) - suma(soloU)
print(noEstudian)

diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    'Básica', 'Media', 'Universitaria'))
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_text(subset)
plt.title("Enseñanza")
diagram.get_label_by_id("111").set_text(B & M & U)  # 10
diagram.get_label_by_id("110").set_text((B & M)-U)  # 20
diagram.get_label_by_id("101").set_text((B & U)-M)  # 6
diagram.get_label_by_id("100").set_text(B-(M | U))  # 35
diagram.get_label_by_id("011").set_text((U & M)-B)  # 12
diagram.get_label_by_id("010").set_text(M-(U | B))  # 30
diagram.get_label_by_id("001").set_text(U - ((B & U)-M) - ((U & M)-B))  # 10
plt.show()

# Falta responder las preguntas
