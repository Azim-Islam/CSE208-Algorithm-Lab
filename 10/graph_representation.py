

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
    
    def color_graph(self):
        colors = []
        vertices_set = set()

        #available vertices
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[i][j] == 1:
                    vertices_set.add(i)
                    vertices_set.add(j)

        colors.append(vertices_set)
        l = 0
        for i in colors:
            for j in i:
                tmp_set = set()
                for k in i:
                    if self.adjMatrix[j][k] == 1:
                        tmp_set.add(k)
                print(tmp_set)
                #tmp_set contains all the invalid colors
            #print(i)
            #print(i.intersection(i - tmp_set))
            break 
            
            
            if len(tmp_set) > 1:
                colors.append(tmp_set)
            else:
                print("breaking up")
                break
            
            
            print(*colors)
        #print(*colors)
        
                
            
        
        
        
    
def main():
    size = int(input("Please enter number of Vertex: "))
    graph = adjcn_matrix_Graph(size)
    size = int(input("Please enter number of Edges: "))
    for i in range(size):
        v1, v2 = map(int, input("Enter V1, V2: ").split())
        graph.add_edge(v1-1, v2-1)
        
    graph.print_matrix()

    graph.color_graph()


if __name__ == '__main__':
        
    main()