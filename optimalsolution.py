import networkx as nx

def linear_extensions(cover_relation):
    # Create a directed graph from the cover relation
    G = nx.DiGraph()
    for a, b in cover_relation:
        G.add_edge(a, b)
    
    # Compute all possible topological sortings (i.e., linear extensions) of the graph
    sortings = list(nx.all_topological_sorts(G))
    
    # Convert each sorting to a string and return the list of all sortings
    return [''.join(map(str, sorting)) for sorting in sortings]

cover_relation = [(1, 2), (1, 4), (2, 3)]
cover_relation = [(1, 2), (1, 3), (1, 4)]
extensions = linear_extensions(cover_relation)
print(sorted(extensions))
