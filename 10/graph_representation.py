from collections import defaultdict
import string


class adjcn_matrix_Graph(object):

    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0]*size)
        self.size = size

    # Adding edges
    def add_edge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1 #Uncomment this line for undirected graph

    # Removing edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print(f"No edge between {v1} and {v2}")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        print("\n")
        for row in self.adjMatrix:
            print(row)
    
    def valid_node_color(self, node_list: list, j_node: int):
        for i in node_list:
            if self.adjMatrix[i][j_node] == 1:
                return False
        return True
    
    def color_graph(self):
        vertices_set = set()
        #available vertices
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[i][j] == 1:
                    vertices_set.add(i)
                    vertices_set.add(j)
        
        colors = defaultdict(list)
        key = 0
        #colors set
        while len(vertices_set) > 0:
            key += 1
            blacklist = set()
            for i in vertices_set: #this for loop runs only once
                colors[key] = [i]
                for j in vertices_set:
                    if i != j:
                        if self.adjMatrix[i][j] == 1:
                            blacklist.add(j)
                        else:
                            if self.valid_node_color(colors[key], j): # checks if a new node 'j' can be added.
                                colors[key].append(j)
                            else:
                                blacklist.add(j) 
                break
            vertices_set = blacklist
        return colors
    
    def print_colored_graph(self, colors: defaultdict[list]):
        for i in colors.keys():
            print(f"Color {string.ascii_letters[i-1]} = {', '.join(map(str, colors[i]))}")
        
    
def main():
    size = int(input("Please enter number of Vertex: "))
    graph = adjcn_matrix_Graph(size)
    size = int(input("Please enter number of Edges: "))
    for i in range(size):
        v1, v2 = map(int, input("Enter V1, V2: ").split())
        graph.add_edge(v1-1, v2-1)
        
    graph.print_matrix()
    graph.print_colored_graph(graph.color_graph())


if __name__ == '__main__':
        
    main()