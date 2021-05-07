"""
En una comunidad de 100 deportistas se sabe que 30 de ellos entrenan fútbol, 50 entrenan squash 
y 60 entrenan tenis. 22 entrenan tenis y fútbol, 30 entrenan squash y tenis y 15 entrenan squash y fútbol. 
Se tomó un registro de los consultados en diferentes estructuras, lista, tupla y diccionarios.
Preguntas:
Si 10 deportistas entrenan los tres deportes 
1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

lista_futbol = [4, 7, 9, 3, 5, 2]
tupla_squash = (10, 3, 9, 7, 5, 12, 4)
diccio_tenis = {"infantil": 12,  "juniors": 15,
                "adolescentes": 16, "adultos": 17}

# sumamos los elementos de cada estructura utilizando funciones

def suma_futbol(lista_futbol):
    suma = 0
    for elemento in lista_futbol:
        suma = suma + elemento
    return suma

def suma_squash(tupla_squash):
    suma = 0
    for elemento in tupla_squash:
        suma = suma + elemento
    return suma

def suma_tenis(diccio_tenis):
    suma = 0
    for elemento in diccio_tenis.values():
        suma = suma + elemento
    return suma

# Definimos e inicializamos variables

universal = 100
futbol = suma_futbol(lista_futbol)
squash = suma_squash(tupla_squash)
tenis = suma_tenis(diccio_tenis)
tenis_futbol = 22
squash_tenis = 30
squash_futbol = 15
squash_tenis_futbol = 10
ninguno = 0

# Funciones y operaciones

def solo2(x, y):
    z = x - y
    return z

def solo1(u, v, x, y):
    z = u - v - x - y
    return z

def tenis_o_futbol(s, t, u, v, x, y):
    z = s + t + u + v + x + y
    return z

soloFT = solo2(tenis_futbol, squash_tenis_futbol)

soloTS = solo2(squash_tenis, squash_tenis_futbol)

soloFS = solo2(squash_futbol, squash_tenis_futbol)

soloF = solo1(futbol, soloFT, soloFS, squash_tenis_futbol)

soloT = solo1(tenis, soloTS, soloFT, squash_tenis_futbol)

soloS = solo1(squash, soloFS, soloTS, squash_tenis_futbol)

tenis_o_futbol = tenis_o_futbol(
    soloFT, soloTS, soloFS, soloF,  soloT, squash_tenis_futbol)

# preparamos la ventana del gráfico
plt.figure('Ejemplo de primer parcial ')

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Futbol", "Squash", "Tenis"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloF)
diagram.get_label_by_id('010').set_text(soloS)
diagram.get_label_by_id('001').set_text(soloT)
diagram.get_label_by_id('110').set_text(soloFS)
diagram.get_label_by_id('011').set_text(soloTS)
diagram.get_label_by_id('101').set_text(soloFT)
diagram.get_label_by_id('111').set_text(squash_tenis_futbol)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# agregamos más datos aclaratorios al gráfico
plt.text(-0.90, 0.67,      # Texto Universal =
         "Universal =",
         size=10)

plt.text(-0.60, 0.67,   # Cantidad universal
         universal,
         size=10)

plt.text(0.40, -0.5,      # Texto fuera del conjunto
         "Fuera\nde los\nconjuntos =",
         size=8)

plt.text(0.65, -0.5,    # Cantidad fuera de los conjuntos
         ninguno,  
         size=10)  

# Respondemos las preguntas
plt.text(-1.10, -0.20,  
         s="Respuestas solicitadas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,  
         s="Entrenan sólo tenis = " + str(soloT),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,  
         s="Entrenan sólo fútbol = " + str(soloF),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,  
         s="Entrenan sólo squash = " + str(soloS),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,  
         s="Entrenan tenis o fútbol = " + str(tenis_o_futbol),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.axis('on')   ## Recuadro 
plt.title("Deportistas")
plt.show()