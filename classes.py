import networkx as nx
class Poset:
    def __init__(self, binaryRel, linearOrder):
        self.binaryRel = binaryRel
        self.linearOrder = linearOrder

    def getLinearExtensions(self):
        # Create a directed graph from the cover relation
        G = nx.DiGraph()
        for a, b in self.binaryRel:
            G.add_edge(a, b)
        
        # Compute all possible topological sortings (i.e., linear extensions) of the graph
        sortings = list(nx.all_topological_sorts(G))
        
        # Convert each sorting to a string and return the list of all sortings
        return sorted([''.join(map(str, sorting)) for sorting in sortings])