import sys
import os
import networkx as nx

SOLUTION_FILE = sys.argv[1]
FOLDER_PATH = os.path.dirname(SOLUTION_FILE)

# Read graph
G = nx.Graph()

for line in open(FOLDER_PATH + '/node_weights.txt'):
    vertex, weight = line.split()
    G.add_node(vertex, weight=int(weight))


with open(FOLDER_PATH + '/conflict_graph.txt') as file:
    next(file)
    for line in file:
        u, v = line.split()
        G.add_edge(u, v)

print(f"Vertices: {len(G.nodes)}")
print(f"Edges: {len(G.edges)}")

solution = set()

with open(SOLUTION_FILE) as file:
    for line in file:
        solution.add(line.rstrip('\n'))

leftover = G.copy()


for vertex in G.nodes:
    if vertex in solution:
        leftover.remove_node(vertex)


print(f"Edges: {len(leftover.edges)}")
