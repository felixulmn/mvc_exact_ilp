import sys
import os
import networkx as nx

FOLDER_PATH = sys.argv[1]
print()

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

complement_derived_vertex_cover = set()
with open(FOLDER_PATH + '/lploads.txt') as file:
    for line in file:
        node, included = line.split()
        if int(float(included)) == 0:
            complement_derived_vertex_cover.add(node)

calculated_vertex_cover = set()
with open(FOLDER_PATH + '/_min_weighted_vertex_cover.sol') as file:
    for line in file:
        line = line.rstrip('\n')
        calculated_vertex_cover.add(line)
        if not G.has_node(line):
            print(f"Solution contains non-existing vertex {line}")
            sys.exit(1)


complement_weight = 0
calculated_weight = 0

for vertex in G.nodes:
    if vertex in complement_derived_vertex_cover:
        complement_weight += G.nodes[vertex]['weight']
    if vertex in calculated_vertex_cover:
        calculated_weight += G.nodes[vertex]['weight']


print(
    f'Complement-derived vertex cover node count: {len(complement_derived_vertex_cover)}')
print(f'Complement-derived vertex cover weight: {complement_weight}')
print()
print(f'Calcualted vertex cover node count: {len(calculated_vertex_cover)}')
print(f'Calculated vertex cover weight: {calculated_weight}')

print()
if (complement_derived_vertex_cover == calculated_vertex_cover):
    print("Vertex covers are equal.")
else:
    print("Vertex covers are not equal.")
