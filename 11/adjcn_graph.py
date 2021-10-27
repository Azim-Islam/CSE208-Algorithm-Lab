from collections import defaultdict

class AdjGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.edges = list()
        
    def add_node(self, node: str, adjcn_node: str, weight: int):
        self.graph[node].append((adjcn_node, weight))
        self.edges.append((node, adjcn_node, weight))

    def remove_node(self, node:str):
        del self.graph[node]
    
    def print_node(self):
        print("\n")
        for i in self.graph.keys():
            print(", ".join(map(str, (i, self.graph[i]))))
    
    def print_edge(self):
        print(*self.edges, sep="\n")
            
    def get_graph(self):
        return self.graph
    
    def sort_edges(self):
        #Sort the edges
        self.edges.sort(key=lambda x : x[2])