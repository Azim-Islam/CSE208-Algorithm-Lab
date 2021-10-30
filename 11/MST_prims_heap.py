from adjcn_graph import AdjGraph
import heapq

graph = AdjGraph()

for _ in range(int(input("Input the number of EDGES:"))):
    node, adj_node, weight = input().split()
    graph.add_node(node, int(weight), adj_node)
    graph.add_node(adj_node, int(weight), node)
    
    
mst = list()
visited = set()   
 
def prims(graph: dict, starting_node):
    edges = [(cost, starting_node, adj_node) for cost, adj_node in graph[starting_node]]
    heapq.heapify(edges)
    visited.add(starting_node)
    count = 0
    while edges:
        count += 1
        print(f"while loop run {count}")
        edge = heapq.heappop(edges) #edge[0] = cost, edge[1] = node_1, edge[2] = node_2
        if edge[2] not in visited:
            mst.append((edge[1], edge[2], edge[0]))
            visited.add(edge[2])
            [heapq.heappush(edges, (cost, edge[2], adj_node)) for cost, adj_node in graph[edge[2]] if adj_node not in visited]
        
prims(graph.graph, list(graph.graph.keys())[0])
print(mst)
