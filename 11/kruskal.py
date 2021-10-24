# A class to represent a graph object
class Graph:
 
    # Constructor
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N + 1)]
 
        # add edges to the graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
 
 
class DisjointSet:
    parent = {}
 
    # stores the depth of trees
    rank = {}
 
    # perform MakeSet operation
    def makeSet(self, universe):
 
        # create `n` disjoint sets (one for each item)
        for i in universe:
            self.parent[i] = i
            self.rank[i] = 0
 
    # Find the root of the set in which element `k` belongs
    def Find(self, k):
 
        # if `k` is not the root
        if self.parent[k] != k:
            # path compression
            self.parent[k] = self.Find(self.parent[k])
 
        return self.parent[k]
 
    # Perform Union of two subsets
    def Union(self, a, b):
 
        # find the root of the sets in which elements
        # `x` and `y` belongs
        x = self.Find(a)
        y = self.Find(b)
 
        # if `x` and `y` are present in the same set
        if x == y:
            return
 
        # Always attach a smaller depth tree under the
        # root of the deeper tree.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] = self.rank[y] + 1
 
 
# Returns true if the graph has a cycle
def findCycle(graph, N):
 
    # initialize `DisjointSet` class
    ds = DisjointSet()
 
    # create a singleton set for each element of the universe
    ds.makeSet(N)
 
    # consider every edge `(u, v)`
    for u in range(1, N + 1):
 
        # Recur for all adjacent vertices
        for v in graph.adjList[u]:
 
            # find the root of the sets to which elements `u` and `v` belongs
            x = ds.Find(u)
            y = ds.Find(v)
 
            # if both `u` and `v` have the same parent, the cycle is found
            if x == y:
                return True
            else:
                ds.Union(x, y)
 
    return False
 
 
# Union–find algorithm for cycle detection in a graph
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11), (11, 12)
        # edge (11, 12) introduces a cycle in the graph
    ]
 
    # total number of nodes in the graph
    N = 12
 
    # construct graph
    graph = Graph(edges, N)
 
    if findCycle(graph, N):
        print("Cycle Found")
    else:
        print("No Cycle is Found")