from adjcn_graph import AdjGraph
from stack import stack

graph = AdjGraph()


for _ in range(int(input("Input the number of EDGES:"))):
    node, adj_node, weight = input().split()
    graph.add_node(node, adj_node, int(weight))
    

visited_nodes = set()
stack_ = stack()
adj_list = graph.get_graph()

stack_.push(list(adj_list.keys())[0])

while not stack_.is_empty():
    visiting_node = stack_.pop()
    print(f"Visiting '{visiting_node}'")
    
    visited_nodes.add(visiting_node)
    
    for i in adj_list[visiting_node]:
        if i not in visited_nodes:
            stack_.push(i)