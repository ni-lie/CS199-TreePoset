import networkx as nx
# gets binary relation for each linear order
def binaryRelation(input):
    P = []
    for linear_order in input:
        binaryRel = linear_order_to_binary_relation(linear_order)
        P.append(binaryRel)
    return P

# given a linear order, get its corresponding binary relation
def linear_order_to_binary_relation(order):
    """
    Takes a linear order as input and returns its binary relation as a list of tuples.
    """
    n = len(order)
    relation = []
    for i in range(n):
        for j in range(i+1, n):
            relation.append((int(order[i]), int(order[j])))
    relation = sorted(relation, key=lambda x: (x[0], x[1]))  # Sort the relation in ascending order
    return relation

# Example usage:
# order = '14235'
# relation = linear_order_to_binary_relation(order)
# print(relation)


def get_linear_extensions(cover_relation):
    # Create a directed graph from the cover relation
    G = nx.DiGraph()
    for a, b in cover_relation:
        G.add_edge(a, b)
    
    # Compute all possible topological sortings (i.e., linear extensions) of the graph
    sortings = list(nx.all_topological_sorts(G))
    
    # Convert each sorting to a string and return the list of all sortings
    return sorted([''.join(map(str, sorting)) for sorting in sortings])


# returns True if (b, x) not in P1 and (a, x) not in P2
def checkerTail(P1, P2, a, b):
    V = getVertices(P1)
    for x in V:
        if (b, x) in P1 or (a, x) in P2:
            return False
    return True

# returns P1 - P2
def getDifference(P1, P2):
    return [x for x in P1 if x not in P2]

# given a poset -- a list of tuples -- returns V that contains all elements of poset
def getVertices(P):
    return list(set([x for t in P for x in t]))

# given a poset -- a list of tuples -- returns the root of the poset
def getRoot(P):
    index_1_elements = {t[1] for t in P}
    all_elements = {x for t in P for x in t}
    return list(all_elements - index_1_elements)[0]


# returns True if poset P is a Tree Poset
def isTreePoset(P):
    V = getVertices(P)
    root = getRoot(P)

    prec = [0 for i in range(len(V))]
    succ = [0 for i in range(len(V))]

    for i in range(len(P)):
        prec[P[i][1] - 1] += 1
        succ[P[i][0] - 1] += 1
    
    # for i in range(len(V)):
    #     if i == root-1 and prec[i] == 0:
    #         continue

    if sum(prec) == sum(succ) and succ[root-1] > 0:
        return True

    return False

    
def combinePoset(P1, P2):
    P3 = getDifference(P1, P2)
    P4 = getDifference(P2, P1)

    if len(P1) == len(P2):
        if len(P3)!=1 or len(P4)!=1:
            return None
        
        P3_ele = P3[0]
        P4_ele = P4[0]
        a, b = P3_ele[0], P3_ele[1]
        c, d = P4_ele[0], P4_ele[1]

        if a != d or b != c:
            return None
        
        P = getDifference(P1, P3)
        return P
    
    elif len(P3) > 1 and len(P4) > 1:
        return None
    elif len(P3) == 1:
        P3_ele = P3[0]
        a, b = P3_ele[0], P3_ele[1]

        # if (b,a) in P4 and checkerTail(P1, P2, a, b) and getDifference(P1, P3) == getDifference(P2, P4):
        #     P = getDifference(P1, P3)
        if (b, a) in P4 and set(getDifference(P1, P3)) == set(getDifference(P2, P4)):
            P = getDifference(P1, P3)
            return P
    elif len(P4) == 1:
        P4_ele = P4[0]
        a, b = P4_ele[0], P4_ele[1]
         
        if (b, a) in P3 and set(getDifference(P1, P3)) == set(getDifference(P2, P4)):
            P = getDifference(P1, P3)
            return P
    # if isTreePoset(P):
    return None

def combinePosetv2(P1, P2):
    

    


# P1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
# P2 = [(1, 2), (1, 4), (1, 3), (2, 4), (2, 3), (4, 3)]

# P1 = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 2), (3, 4)]
# P2 = [(1, 2), (1, 3), (1, 4), (3, 2), (3, 4), (4, 2)]
# P2 = [(1, 2), (1, 3), (1, 4), (2, 3), (4, 2), (4, 3)]
# P1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]

# P1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
# P2 = [(1, 2), (1, 3), (1, 4), (3, 2), (3, 4)] 

# P1 = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 2), (3, 4)]
# P2 = [(1, 2), (1, 3), (1, 4), (3, 2), (3, 4), (4, 2)]

# unbalanced P1 and P2
# P1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
# P2 = [(1, 2), (1, 3), (1, 4), (2, 3), (4, 2), (4, 3)]

# P1 = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)]
# P2 = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 2), (3, 4)]

# p = combinePoset(P1, P2)
# if p != None:
#     print(p)
# else:
#     print("No returned poset")




