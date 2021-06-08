
import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (12.0, 5.0)

G = nx.Graph()

G.add_nodes_from((["Argentina", "Jujuy", "Salta", "Tucumán", "Catamarca", "Santiago\ndel\nEstero",
                   "Formosa", "Chaco", "Misiones", "Corrientes",
                   "Entre\nRíos", "Santa\nFé", "Córdoba", "Buenos\nAires", "La\nPampa",
                   "San\nJuan", "San\nLuis", "Mendoza", "La\nRioja",
                   "Neuquén", "Río\nNegro", "Chubut", "Santa\nCruz", "Tierra\ndel\nFuego"]))

G.add_edges_from([("Jujuy", "Argentina"),
                  ("Salta", "Argentina"),
                  ("Tucumán",  "Argentina"),
                  ("Catamarca", "Argentina"),
                  ("Santiago\ndel\nEstero", "Argentina"),
                  ("Formosa", "Argentina"),
                  ("Chaco", "Argentina"),
                  ("Misiones", "Argentina"),
                  ("Corrientes", "Argentina"),
                  ("Entre\nRíos", "Argentina"),
                  ("Santa\nFé", "Argentina"),
                  ("Córdoba", "Argentina"),
                  ("Buenos\nAires", "Argentina"),
                  ("La\nPampa", "Argentina"),
                  ("San\nJuan", "Argentina"),
                  ("San\nLuis", "Argentina"),
                  ("Mendoza", "Argentina"),
                  ("La\nRioja", "Argentina"),
                  ("Neuquén", "Argentina"),
                  ("Río\nNegro", "Argentina"),
                  ("Chubut", "Argentina"),
                  ("Santa\nCruz", "Argentina"),
                  ("Tierra\ndel\nFuego", "Argentina")])

pais = ["Argentina"]

nx.draw(G,
        node_color=['lightblue' if node in pais else 'pink' for node in G.nodes()],
        edge_color="black",
        font_size=8,
        width=2,
        with_labels=True,
        node_size=2000
        )
plt.show()

print("Nodos: ", G.number_of_nodes(), G.nodes())

print("Enlaces: ", G.number_of_edges(), G.edges())

print("Radio: %d" % nx.radius(G))
print("Diámetro: %d" % nx.diameter(G))
print("Excentricidad: %s" % nx.eccentricity(G))
print("Centro: %s" % nx.center(G))
print("Periferia: %s" % nx.periphery(G))
print("Densidad: %s" % nx.density(G))