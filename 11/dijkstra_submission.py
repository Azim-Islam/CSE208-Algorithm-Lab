import heapq
import adjcn_graph

graph = adjcn_graph.AdjGraph()

for _ in range(int(input("Input the number of EDGES:"))):
    node, adj_node, weight = input().split()
    graph.add_node(node, int(weight), adj_node)
    graph.add_node(adj_node, int(weight), node) # This is an undirected graph.
    
def dijkstra(graph: graph.graph, source_node: str):
    #stnc = source_to_node_costs
    stnc = {node:9999999999999 for node in list(graph.keys())} #setting the initial value as inf distance to the source
    visited_nodes = set() # A set to track the visited nodes
    
    # Inserting all the edges to source_node -> adj_nodes
    edges = [(weight, source_node, adj_node) for  weight, adj_node in graph[source_node]]
    # Transforming those edges into a Priority Queue
    heapq.heapify(edges)
    visited_nodes.add(source_node) # Adding the source_node into visited_node
    stnc[source_node] = 0
    count = 0
    while edges: # While the edges are not empty
        count += 1
        print(f"While loop run time {count}")
        edge = heapq.heappop(edges) # edge[0] = weight, edge[1] = source_node, edge[2] = adj_node
        weight = edge[0]
        src_node = edge[1]
        adj_node = edge[2]
        
        if stnc[src_node] + weight < stnc[adj_node] and adj_node not in visited_nodes: 
            stnc[adj_node] = stnc[src_node] + weight # picking up the smallest value (node to source)for a node
            [heapq.heappush(edges, (weight, adj_node, next_node)) for weight, next_node in graph[adj_node] if next_node not in visited_nodes] # Adding edges into the heap
        visited_nodes.add(src_node)
    print(stnc)
    
dijkstra(graph.graph, "A")