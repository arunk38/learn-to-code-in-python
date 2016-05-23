"""
    A graph in mathematics and computer science consists of "nodes" which may or may not be connected with one another.
    connections between nodes are called edges.
"""

# directed graph
graph = {'A' : ['B', 'C'],
         'B' : ['C', 'A'],
         'C' : ['D'],
         'D' : ['A']}

print(graph)

# graphs using networkx, has support for creating and manupulating graphs
import networkx as nx

G = nx.Graph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A", "B")
G.add_edge("B", "C")
G.add_edge("C", "A")

print("Nodes: " + str(G.nodes()))
print("Edges: " + str(G.edges()))