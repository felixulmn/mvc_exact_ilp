import sys
import time
import networkx as nx
from gurobipy import *


G = nx.Graph()
max_clique_size = 0

for line in open(sys.argv[1]):
    fields = line.split()
    u = fields[0]
    v = fields[1]
    G.add_node(u)
    G.add_node(v)
    G.add_edge(u, v)

print("G has", G.number_of_nodes(), "vertices and",
      G.number_of_edges(), "edges.", file=sys.stderr)


start = time.time()

try:

    # Model with variables
    m = Model("Minimum Vertex Cover")
    for v in G.nodes:
        m.addVar(vtype=GRB.BINARY, name=v)
    m.update()

    # Objective Function
    obj = LinExpr()
    for v in G.nodes:
        obj.add(m.getVarByName(v))
    m.setObjective(obj, GRB.MINIMIZE)
    m.update()

    # Add constraints
    for (u, v) in G.edges:
        xu = m.getVarByName(u)
        xv = m.getVarByName(v)
        m.addConstr(xu + xv >= 1)

    m.update()
    m.optimize()
    m.write("min_vertex_cover.lp")

    print("Optimized.\nTotal running time:", "{:7.3f}".format(
        time.time()-start), "s.\nCurrent max clique size:", max_clique_size)

    # TODO: Add output


except GurobiError as e:
    print(e.message)
