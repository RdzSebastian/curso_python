
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 5.0)

G = nx.Graph()

G.add_node("Argentina")

G.add_nodes_from(["Noroeste", "Nordeste", "Pampeana",
                  "Cuyo", "Patagónica"])

G.add_nodes_from((["Jujuy", "Salta", "Tucumán", "Catamarca", "Santiago\ndel\nEstero",
                   "Formosa", "Chaco", "Misiones", "Corrientes",
                   "Entre\nRíos", "Santa\nFé", "Córdoba", "Buenos\nAires", "La\nPampa",
                   "San\nJuan", "San\nLuis", "Mendoza", "La\nRioja",
                   "Neuquén", "Río\nNegro", "Chubut", "Santa\nCruz", "Tierra\ndel\nFuego"]))

G.add_edge("Noroeste", "Argentina")

G.add_edge("Nordeste", "Argentina")

G.add_edge("Pampeana", "Argentina")

G.add_edge("Cuyo", "Argentina")

G.add_edge("Patagónica", "Argentina")

lista_noroeste = [("Jujuy",  "Noroeste"), ("Salta", "Noroeste"),
                  ("Catamarca", "Noroeste"), ("Santiago\ndel\nEstero", "Noroeste"), ("Tucumán", "Noroeste")]
G.add_edges_from(lista_noroeste)

lista_nordeste = [("Formosa", "Nordeste"), ("Chaco", "Nordeste"),
                  ("Misiones", "Nordeste"), ("Corrientes", "Nordeste")]
G.add_edges_from(lista_nordeste)

lista_pampeana = [("Entre\nRíos", "Pampeana"), ("Santa\nFé", "Pampeana"),
                  ("Córdoba", "Pampeana"),("La\nPampa", "Pampeana"), ("Buenos\nAires", "Pampeana")]
G.add_edges_from(lista_pampeana)

lista_cuyo = [("San\nJuan", "Cuyo"), ("San\nLuis", "Cuyo"),
              ("Mendoza", "Cuyo"), ("La\nRioja", "Cuyo")]
G.add_edges_from(lista_cuyo)

lista_patagonica = [("Neuquén", "Patagónica"), ("Río\nNegro", "Patagónica"), ("Chubut", "Patagónica"), 
                    ("Santa\nCruz", "Patagónica"), ("Tierra\ndel\nFuego", "Patagónica")]
G.add_edges_from(lista_patagonica)

regiones = ["Noroeste", "Nordeste", "Pampeana","Cuyo", "Patagónica"]

nx.draw(G,
        node_color= ['pink' if not node in regiones else 'violet' for node in G.nodes()],
        edge_color="black",
        font_size=8,
        width=2,
        with_labels=True,
        node_size=2000,
        )
plt.show()

print("Nodos: ", G.number_of_nodes(), G.nodes())
print("Enlaces: ", G.number_of_edges(), G.edges())

print("radius: %d" % nx.radius(G))
print("diameter: %d" % nx.diameter(G))
print("eccentricity: %s" % nx.eccentricity(G))
print("center: %s" % nx.center(G))
print("periphery: %s" % nx.periphery(G))
print("density: %s" % nx.density(G))