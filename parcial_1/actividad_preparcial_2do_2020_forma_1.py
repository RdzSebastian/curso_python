"""4. Se encuesta a 150 familias consultando por el nivel educacional actual de sus hijos.
Los resultados obtenidos son:
 ▪ 10 familias tienen hijos en Enseñanza Básica, Enseñanza Media y Universitaria.
 ▪ 16 familias tienen hijos en Enseñanza Básica y Universitaria
 ▪ 30 familias tienen hijos en Enseñanza Media y Enseñanza Básica.
 ▪ 22 familias tienen hijos en Enseñanza Media y Universitaria.
 ▪ 72 familias tienen hijos en Enseñanza Media.
 ▪ 71 familias tienen hijos en Enseñanza Básica.
 ▪ 38 familias tienen hijos en Enseñanza Universitaria.
Con la información anterior, deducir:
- El número de familias que solo tienen hijos universitarios.
- El número de familias que tienen hijos solo en dos niveles.
- El número de familias que tienen hijos que no estudian.
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
B = {10, 6, 20, 35}
M = {10, 20, 12, 30}
U = {10, 6, 12, '10'}
#UT={10}

diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    'Básica', 'Media', 'Universitaria'))
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_text(subset)
plt.title("Enseñanza")
diagram.get_label_by_id("111").set_text(B & M & U)
diagram.get_label_by_id("110").set_text((B & M)-U)
diagram.get_label_by_id("101").set_text((B & U)-M)
diagram.get_label_by_id("100").set_text(B-(M | U))
diagram.get_label_by_id("011").set_text((U & M)-B)
diagram.get_label_by_id("010").set_text(M-(U | B))
diagram.get_label_by_id("001").set_text(U-(M | B))

plt.show()
