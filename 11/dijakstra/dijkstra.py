# https://www.techiedelight.com/single-source-shortest-paths-dijkstras-algorithm/
import sys
from heapq import heappop, heappush
 
 
# A class to store a graph edge
class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight
 
 
# A class to store a heap node
class Node:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
 
    # Override the `__lt__()` function to make `Node` class work with a min-heap
    def __lt__(self, other):
        return self.weight < other.weight
 
 
# A class to represent a graph object
class Graph:
    def __init__(self, edges, N):
        # allocate memory for the adjacency list
        self.adj = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for edge in edges:
            self.adj[edge.source].append(edge)
 
 
def get_route(prev, i, route):
    if i >= 0:
        get_route(prev, prev[i], route)
        route.append(i)
 
 
# Run Dijkstra’s algorithm on a given graph
def findShortestPaths(graph, source, N):
 
    # create a min-heap and push source node having distance 0
    pq = []
    heappush(pq, Node(source, 0))
 
    # set initial distance from the source to `v` as INFINITY
    dist = [sys.maxsize] * N
 
    # distance from the source to itself is zero
    dist[source] = 0
 
    # list to track vertices for which minimum cost is already found
    done = [False] * N
    done[source] = True
 
    # stores predecessor of a vertex (to a print path)
    prev = [-1] * N
    route = []
 
    # run till min-heap is empty
    while pq:
 
        node = heappop(pq)      # Remove and return the best vertex
        u = node.vertex         # get the vertex number
 
        # do for each neighbor `v` of `u`
        for edge in graph.adj[u]:
            v = edge.dest
            weight = edge.weight
 
            # Relaxation step
            if not done[v] and (dist[u] + weight) < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u
                heappush(pq, Node(v, dist[v]))
 
        # mark vertex `u` as done so it will not get picked up again
        done[u] = True
 
    for i in range(1, N):
        if i != source and dist[i] != sys.maxsize:
            get_route(prev, i, route)
            print(f"Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {route}")
            route.clear()
 
 
if __name__ == '__main__':
 
    # initialize edges as per the above diagram
    # `(u, v, w)` triplet represent undirected edge from
    # vertex `u` to vertex `v` having weight `w`
    edges = [Edge(0, 1, 10), Edge(0, 4, 3), Edge(1, 2, 2),
            Edge(1, 4, 4), Edge(2, 3, 9), Edge(3, 2, 7),
            Edge(4, 1, 1), Edge(4, 2, 8), Edge(4, 3, 2)]
 
    # total number of nodes in the graph
    N = 5
 
    # construct graph
    graph = Graph(edges, N)
 
    source = 0
    findShortestPaths(graph, source, N)