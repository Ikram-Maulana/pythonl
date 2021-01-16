# Python MultiDiGraph
# Ikram Maulana
# 1930511075

import networkx as nx
import matplotlib.pyplot as plt

G = nx.MultiDiGraph()
# Menambahkan Node
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
# Menambahkan Edge
G.add_edge('A', 'C', rad=0.1)
G.add_edge('A', 'C', rad=0.2)
G.add_edge('B', 'A', rad=0.0)
G.add_edge('B', 'D', rad=0.0)

plt.figure(figsize=(6, 6))

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)

for edge in G.edges(data=True):
    nx.draw_networkx_edges(G, pos, edgelist=[(
        edge[0], edge[1])],
        connectionstyle=f'arc3, rad = {edge[2]["rad"]}')

plt.show()
