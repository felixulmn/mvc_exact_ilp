import sys
import os
import networkx as nx

FOLDER_PATH = sys.argv[1]
print()


def is_vertex_cover(graph: nx.Graph, vertices):
    graph = graph.copy()

    for vertex in vertices:
        graph.remove_node(vertex)

    return graph.number_of_edges() == 0


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

try:
    calculated_vertex_cover = set()
    with open(FOLDER_PATH + '/_min_weighted_vertex_cover.sol') as file:
        for line in file:
            line = line.rstrip('\n')
            calculated_vertex_cover.add(line)
            if not G.has_node(line):
                print(f"Solution contains non-existing vertex {line}")
                sys.exit(1)

    calculated_weight = 0

    for vertex in G.nodes:
        if vertex in calculated_vertex_cover:
            calculated_weight += G.nodes[vertex]['weight']

    print('#### Calculated solution\n')
    print(f'{"Node count:" : >16} {len(calculated_vertex_cover)}')
    print(f'{"Total weight:" : >16} {calculated_weight}')
    print(f'{"Is vertex cover:" : >16} {is_vertex_cover(G, calculated_vertex_cover)}')
except:
    print("No file for calculated solution found")

print()

complement_weight = 0
for vertex in G.nodes:
    if vertex in complement_derived_vertex_cover:
        complement_weight += G.nodes[vertex]['weight']


print('#### Complement-derived solution\n')
print(f'{"Node count:" : >16} {len(complement_derived_vertex_cover)}')
print(f'{"Total weight:" : >16} {complement_weight}')
print(f'{"Is vertex cover:" : >16} {is_vertex_cover(G, complement_derived_vertex_cover)}')
