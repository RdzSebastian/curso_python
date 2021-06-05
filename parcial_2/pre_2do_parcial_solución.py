# Ejercicio 1

# Ejercicio 2

import networkx as nx
import matplotlib.pyplot as plt

def emitoGraph(G, pos):
    nx.draw_networkx_nodes(G, pos, node_color='violet', node_size=600)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family='sans-serif')
    nx.draw_networkx_edges(G, pos, edge_color='grey', width=2, arrowstyle= '<|-|>', arrowsize = 10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.axis('off')
    plt.show()

def cargoGraph(G):
    G.add_weighted_edges_from([('a', 'b', 12),
                               ('a', 'd', 14),
                               ('b', 'd', 4),
                               ('b', 'e', 11),
                               ('b', 'c', 7),
                               ('b', 't', 23),
                               ('c', 't', 10),
                               ('c', 'e', 2),
                               ('d', 'e', 6),
                               ('e', 't', 9)])

G = nx.Graph()
cargoGraph(G)
print("Número de nodos: ", G.number_of_nodes())
print("Nodos: ", G.nodes())
print("Número de enlaces: ", G.number_of_edges())
print("Enlaces: ", G.edges())
print("Vecinos: ", list(G.neighbors('b')))
print("Cantidad de aristas de cada nodo: ",G.degree()) 
print(dict(G.degree()))
M = nx.adjacency_matrix(G)
print(M.todense()) 
I =  nx.incidence_matrix(G)
print(I.todense())
print("Valores de los enlaces del nodo: ",G['c'])
print("Peso de la relación entre ", G['b']['e']['weight'])
print("Ruta mas corta al objetivo: ", nx.algorithms.shortest_path(G, 'a')) 
print("Longitud de Ruta mas corta desde: ",nx.single_source_shortest_path_length(G, 'a'))
print("Promedio de la ruta mas corta ", nx.algorithms.average_shortest_path_length(G, method="floyd-warshall"))
print("Ruta mas corta usando el algoritmo de Dijkstra entre:",nx.algorithms.dijkstra_path(G, 'a', 't'))
print("Longitud de Ruta ponderada más corta entre:",nx.dijkstra_path_length(G,'a','t'))
print("Longitud de Ruta ponderada más corta desde el nodo:", nx.single_source_dijkstra_path_length(G,'c'))
print("Radio:",nx.radius(G))
print("Diámetro:", nx.diameter(G))
print("Excentricidad:", nx.eccentricity(G))
print("Centro:", nx.center(G))
print("Periferia:", nx.periphery(G))
print("Densidad:", nx.density(G))
pos = nx.shell_layout(G)
emitoGraph(G, pos)
H = G.to_directed()
cargoGraph(H)
pos = nx.shell_layout(H)
emitoGraph(H, pos)

# Ejercicio 3

import re 

texto = """
98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180
"""

a_buscar = r'[A-Z]{1,}\s\/*.*\d\.\d'

x = re.findall(a_buscar, texto) 

print(x)
