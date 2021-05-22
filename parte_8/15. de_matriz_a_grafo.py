import networkx as nx
import matplotlib.pyplot as plt

mat = [
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0]
]

G = nx.Graph()

a = ["a"+str(i) for i in range(len(mat))]

b = ["b"+str(j) for j in range(len(mat[0]))]

G.add_nodes_from(a, bipartite=0)

G.add_nodes_from(b, bipartite=1)

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] != 0:
            G.add_edge(a[i], b[j])

pos_a = {}
const = 0.100
x = 0.100
y = 1.0

for i in range(len(a)):
    pos_a[a[i]] = [x, y-i*const]
print(pos_a)

pos_b = {}
x = 0.500

for i in range(len(b)):
    pos_b[b[i]] = [x, y-i*const]
print(pos_b)

nx.draw_networkx_nodes(G, pos_a, nodelist=a,
                       node_color="pink", node_size=1000)

nx.draw_networkx_nodes(G, pos_b, nodelist=b,
                       node_color="lightblue", node_size=1000)
pos = {}
pos.update(pos_a)
pos.update(pos_b)
print(pos)

nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
nx.draw_networkx_edges(G, pos, width=2, alpha=0.7)

plt.show()
