
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (15.0, 7.5)

aeropuertos = pd.read_csv('ejemplos/networkx/grafos_con_archivos/aeropuertos.csv', encoding='latin-1')
df_a = pd.DataFrame(aeropuertos)
df_a.head(5)

vuelos = pd.read_csv("ejemplos/networkx/grafos_con_archivos/combi_precios.csv", encoding='latin-1')
df_p = pd.DataFrame(vuelos)
df_p.head(5)

df_p = df_p.iloc[0:25,0:2]
print(df_p)

DG = nx.DiGraph()

for i in range(0, len(df_a)):
    DG.add_node(df_a.iloc[i]['COD'])
    i = i + 1
print(DG.number_of_nodes())
print(DG.nodes())


for i in range(0, len(df_p)):
    DG.add_edge(df_p.iloc[i]['Origen'], df_p.iloc[i]['Destino'])
    i = i + 1
print(DG.number_of_edges())
print(DG.edges())

DG.nodes(data=True)

nx.draw_circular(DG,
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=8,
                 width=2, with_labels=True, node_size=500,
                 )
plt.show()
