
def find_parent(parents, u):
    if parents[u] != u:
        return find_parent(parents, parents[u])
    return parents[u]

def union(parents, rank, u, v):
    if rank[u] > rank[v]:
        parents[v] = u #parent of v is now u
        print(f"Parent of '{v}' is now '{u}'")
    else:
        parents[u] = v #parent of u is now v
        rank[v] = rank[u] + 1 #rank of v has increased to u + 1 since the depth has also increased
        print(f"Parent of '{u}' is now '{v}'")
        