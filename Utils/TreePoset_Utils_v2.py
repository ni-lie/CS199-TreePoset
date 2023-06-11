import networkx as nx

def get_linear_extensions(cover_relation):
    # Create a directed graph from the cover relation
    G = nx.DiGraph()
    for a, b in cover_relation:
        G.add_edge(a, b)
    
    # Compute all possible topological sortings (i.e., linear extensions) of the graph
    sortings = list(nx.all_topological_sorts(G))
    
    # Convert each sorting to a string and return the list of all sortings
    return sorted([''.join(map(str, sorting)) for sorting in sortings])
 
def VERIFY(P, Y):
    if sorted(P) == sorted(Y):
        return True
    return False

def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234; 
    return linearOrder[index]       # output: 4

def group_linearOrders_by_its_root(upsilon):
    grouped_upsilon = {}
    for linearOrder in upsilon:
        root = linearOrder[0]
        if root in grouped_upsilon:
            grouped_upsilon[root].append(linearOrder)
        else:
            grouped_upsilon[root] = [linearOrder]
    
    return list(grouped_upsilon.values())
