# Overview

These scripts are used to calculate exact solutions for (un-)weighted vertex cover using integer linear programming. The scripts use gurobipy and networkx.

# Usage

### `min_vertex_cover.py`

_Calculates the minimum vertex cover for a given problem file._

`python min_vertex_cover.py <problemfile>`

<br>

**Arguments**

1. `<problemfile>`

   - The problem file contains all edges of the underlying graph. Each row contains one edge in the format `u v`

   - Example

     ```
     1 2
     1 3
     2 3
     2 4
     ```

---

### `min_weighted_vertex_cover.py`

_Calculates the weighted minimum vertex cover for a given problem folder._

`python min_weighted_vertex_cover.py <problemfolder>`

<br>

**Arguments**

1. `<problemfolder>`

   - The problem folder contains files as the problems presented in[^1]. The files used are `conflict_graph.txt` and `node_weights.txt`, which represent the graph's edges and the vertices' weights, respectively. The `conflict_graph.txt` has the same format as the problem file for the unweighted script with the exception of the first row. It contains the node and edge count in the format `nodecount edgecount`. The `node_weights.txt` file has one node with its weight in each row. The format it `node nodeweitght`

   - Example for `conflictgraph.txt`

     ```
     25 300
     1 2
     1 3
     2 3
     2 4

     ...
     ```

   - Example for `node_weights.txt`

     ```
     1 34834
     2 90561
     3 120349
     4 87342
     ```

---

### `check_solution.py`

_Derives solution for min. weighted vertex cover from complement solution and compares it against the saved solution from `min_weighted_vertex_cover.py`._

`python check_solution.py <problemfolder>`

<br>

**Arguments**

1. `<problemfolder>`

   - The problem folder is the same as in `min_weighted_vertex_cover.py`. In addition, the file `solution.txt` is used. It contains one node per row and is the solution to the maximum independent set problem of the given graph. It is used to calculate the minimum vertex cover using the complement graph. It also uses `_min_weighted_vertex_cover.sol` generated by `min_weighted_vertex_cover.py` which has the same format as `solution.txt` to compare the complement-derived solution to the one generated by the script.

   - Example for `solution.txt` and `_min_weighted_vertex_cover.sol`

     ```
     4
     5
     9
     17
     ```

# References

[^1]: Dong Yuanyuan and Goldberg, A. V. and N. A. and P. N. and R. M. G. C. and S. Q. (2021). New Instances for Maximum Weight Independent Set From a Vehicle Routing Application. _Operations Research Forum_, _2_(4), 48. https://doi.org/10.1007/s43069-021-00084-x
