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

def gen_tree_poset(upsilon):    
    Ptree = []
    m = len(upsilon)     
    n = len(upsilon[0])

    minRank = [0 for i in range(n)]
    numCoverRelation = 0
    coverRelationP = []
    nextset = False

    while len(upsilon) > 0:
        nextset = False
        for h in range(m, 0, -1):
            if nextset:
                break
            for i in range(1,n):
                for j in range(h):
                    v2 = rankInverse(i, upsilon[j])
                    if minRank[int(v2)-1] == 0:
                        v1 = rankInverse(i-1, upsilon[j])
                        coverRelationP.append((int(v1),int(v2)))
                        minRank[int(v2)-1] = i
                        minRank[int(v1)-1] = i-1
                        numCoverRelation +=1
                if numCoverRelation == n-1:
                    P = get_linear_extensions(coverRelationP)
                    if VERIFY(P, upsilon[:h]):
                        Ptree.append(coverRelationP)
                        upsilon = upsilon[h:]
                        if len(upsilon) > 0:
                            m = len(upsilon)     
                            n = len(upsilon[0])
                        minRank = [0 for i in range(n)]
                        numCoverRelation = 0
                        coverRelationP = []
                        nextset = True
                        break
                    else:
                        minRank = [0 for i in range(n)]
                        numCoverRelation = 0
                        coverRelationP = []
                        break
    
    # P = get_linear_extensions(coverRelationP)

    # if VERIFY(P, upsilon):
    return Ptree

    # return None

def VERIFY(P, Y):
    if sorted(P) == sorted(Y):
        return True
    return False

def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234; 
    return linearOrder[index]       # output: 4

input_linear_order = [1234, 1243, 1324, 1342, 1423]
# input_linear_order = [1234, 1243, 1324, 1342, 1423, 1432]

input_linear_order = [str(item) for item in input_linear_order]
input_linear_order.sort()

poset = gen_tree_poset(input_linear_order)

if poset != None:
    for i in range(len(poset)):
        print(f"P{str(i+1)}: {poset[i]}")