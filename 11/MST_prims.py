from collections import defaultdict
from adjcn_graph import AdjGraph
from queue import PriorityQueue


def mst_add_node(graph:dict, node:str, mst: set, mst_edges: list) -> None: 
    edge = min(graph[node], key=lambda x: x[1])
    adj_node = edge[0]
    weight = edge[1]
    mst_edges.append((node, adj_node, weight))
    mst.add(node)
    mst.add(adj_node)

    
    

graph = AdjGraph()

for _ in range(int(input("Input the number of EDGES:"))):
    node, adj_node, weight = input().split()
    graph.add_node(node, adj_node, int(weight))
    graph.add_node(adj_node, node, int(weight)) #uncommenting this line for undirected graph
    
mst = set()
mst_edges = list()
nodes = list(graph.graph.keys())

for node in nodes:
    #check if A is in the MST, if it is then check if it can be added to the MST
    
    if node not in mst:
        mst_add_node(graph.graph, node, mst, mst_edges)
    
print(nodes)
        
if not len(mst_edges) == len(nodes) - 1:
    last_node = graph.graph[nodes[-1]]
    second_last_node = graph.graph[nodes[-2]]
    last_second = sorted(last_node + second_last_node, key=lambda x: x[1])
    
    for node in last_second:
        if nodes[-1] in node or nodes[-2] in node:
            pass
        else:
            for i in graph.graph[node[0]]:
                if i[0] == nodes[-1]:
                    mst_edges.append((node[0], nodes[-1], node[-1]))
                    break
                else:
                    mst_edges.append((node[0], nodes[-2], node[-1]))
                    break
            break

#graph.print_node()
#graph.print_edge()
print(mst_edges)