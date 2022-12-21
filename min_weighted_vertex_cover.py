import sys
import time
import networkx as nx
from gurobipy import *

FOLDER_PATH = './dataset_weighted/MT-D-01'

if len(sys.argv) > 1:
    FOLDER_PATH = sys.argv[1]

# FIXME Problem with MT-D-01: multiple duplicate edges. E.g. edge (3,338) lines 19, 20

# Generate graph from file
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


# Calculate minimum weighted vertex cover
start = time.time()

try:

    # Model with variables
    m = Model("Minimum Weighted Vertex Cover")
    for v in G.nodes:
        m.addVar(vtype=GRB.BINARY, name=v)
    m.update()

    # Objective Function
    obj = LinExpr()
    for v in G.nodes:
        wv = G.nodes[v]['weight']
        obj.add(m.getVarByName(v)*wv)
    m.setObjective(obj, GRB.MINIMIZE)
    m.update()

    # Add constraints
    for (u, v) in G.edges:
        xu = m.getVarByName(u)
        xv = m.getVarByName(v)
        m.addConstr(xu + xv >= 1)
    m.update()

    # Run optimization
    m.optimize()

    # Print running time
    print("Optimized.\nTotal running time:", "{:7.3f}".format(
        time.time()-start))

    # Write model to file
    m.write(FOLDER_PATH + "/_min_weighted_vertex_cover.lp")

    # Write solution to file
    with open(FOLDER_PATH + '/_min_weighted_vertex_cover.sol', 'w') as file:
        for v in m.getVars():
            if v.x > 0:
                file.write(v.varName + '\n')

except GurobiError as e:
    print(e.message)
