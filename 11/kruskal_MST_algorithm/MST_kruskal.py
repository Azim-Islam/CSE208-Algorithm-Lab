# https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/
# https://www.techiedelight.com/union-find-algorithm-cycle-detection-graph/
# https://www.youtube.com/watch?v=UBY4sF86KEY

from adjcn_graph import AdjGraph
from disjoint_set import find_parent, union


graph = AdjGraph()

for _ in range(int(input("Input the number of EDGES:"))):
    node, adj_node, weight = input().split()
    graph.add_node(node, adj_node, int(weight))
    graph.add_node(adj_node, node, int(weight)) # This is an undirected graph.


graph.sort_edges()
graph.print_edge()

parents = dict()
rank = dict()

for i in list(graph.graph.keys()):
    parents[i] = i
    rank[i] = 0


total_cost = 0
final_result = []

for i in graph.edges:
    u, v = i[0], i[1]
    parent_of_u = find_parent(parents, u)
    parent_of_v = find_parent(parents, v)
    # print(parent_of_u)
    # print(parent_of_v)
    
    
    if parent_of_u != parent_of_v:
        final_result.append(i)
        union(parents, rank, u, v)
    

print(final_result)