import sys
import networkx as nx

FOLDER_PATH = './dataset_weighted/MT-D-01'
SOLUTION_FILE = 'solution.txt'

if len(sys.argv) > 2:
    FOLDER_PATH = sys.argv[1]
    SOLUTION_FILE = sys.argv[2]

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

with open(f'{FOLDER_PATH}/{SOLUTION_FILE}') as file:
    for line in file:
        solution.add(line.rstrip('\n'))

leftover = G.copy()


for vertex in G.nodes:
    if vertex in solution:
        leftover.remove_node(vertex)


print(f"Edges: {len(leftover.edges)}")
