import networkx as nx
# from classes import Poset

# creates an object/class Poset for each linear order
def binaryRelation(input):
    P = []
    for linear_order in input:
        binaryRel = linear_order_to_binary_relation(linear_order)
        # poset = Poset(binaryRel, linear_order)
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
def isTreePoset(cover_relations):
    n = len(cover_relations)+1
    check_vertices = [False for x in range(n)] #array that checks if all vertices are included
    parent = [0 for x in range(n)] #array of number of parents of a vertex
    for (a,b) in cover_relations:
        check_vertices[a-1] = True
        check_vertices[b-1] = True
        parent[b-1] += 1
        
    #Check if the valid poset permutation is a tree poset
    for v in parent:
        if (v > 1) or (0 not in parent):
            return False

    #check if all edges are connected
    if False not in check_vertices and nx.is_directed_acyclic_graph(nx.DiGraph(cover_relations)):
        return True
    else:
        return False

#INPUT: set of binary relations; OUTPUT: equivalent set of cover relations
def binaryToCover(P):
    #find number of vertices n
    n = 1
    for pair in P:
        if max(pair) > n:
            n = max(pair)

    coverRelations = []
    for (u,v) in P:
        if (u,v) in coverRelations:
            continue
        #if len(coverRelations) == n - 1:
        #    break
        transitive = False
        for w in range(1, n+1):
            if w == u or w == v:
                continue
            else:
                if (u,w) in P and (w,v) in P:
                    transitive = True
                    break
        if not transitive:
            coverRelations.append((u,v))
    return sorted(coverRelations)
    
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
        #return P
    
    elif len(P3) > 1 and len(P4) > 1:
        return None
    elif len(P3) == 1:
        P3_ele = P3[0]
        a, b = P3_ele[0], P3_ele[1]

        # if (b,a) in P4 and checkerTail(P1, P2, a, b) and getDifference(P1, P3) == getDifference(P2, P4):
        #     P = getDifference(P1, P3)
        if (b, a) in P4 and set(getDifference(P1, P3)) == set(getDifference(P2, P4)):
            P = getDifference(P1, P3)
            #return P
    elif len(P4) == 1:
        P4_ele = P4[0]
        a, b = P4_ele[0], P4_ele[1]
         
        if (b, a) in P3 and set(getDifference(P1, P3)) == set(getDifference(P2, P4)):
            P = getDifference(P1, P3)
            #return P
    if isTreePoset(binaryToCover(P)):
        return P
    return None

def combinePosetv2(P1, P2):
    # check first if same root
    if getRoot(P1) != getRoot(P2):
        return None
    P3 = getDifference(P1, P2)
    P4 = getDifference(P2, P1)

    if len(P1) == len(P2):
        if len(P3) != 1 or len(P4) != 1:
            return None
        
        P3_ele = P3[0]
        P4_ele = P4[0]
        a, b = P3_ele[0], P3_ele[1]
        c, d = P4_ele[0], P4_ele[1]

        if a != d or b != c:
            return None
        
        P = getDifference(P1, P3)
        #return P

    elif len(P3) > 1 and len(P4) > 1:
        return None
    
    else:
        if len(P3) == 1:
            P3_ele = P3[0]
            a, b = P3_ele[0], P3_ele[1]

            P1_temp = P1.copy()
            P2_temp = P2.copy()
            P1_temp.remove((a, b))
            P2_temp.remove((b, a))

            if (b, a) not in P4:
                return None
            elif set(P1_temp).issubset(set(P2_temp)):
                P = getDifference(P1, P3)
                #return P
        elif len(P4) == 1:
            P4_ele = P4[0]
            a, b = P4_ele[0], P4_ele[1]

            P1_temp = P1.copy()
            P2_temp = P2.copy()
            P1_temp.remove((b, a))
            P2_temp.remove((a, b))

            if (b, a) not in P3:
                return None
            elif set(P2_temp).issubset(set(P1_temp)):
                P = getDifference(P1, P3)
                #return P 
    if isTreePoset(binaryToCover(P)):
        return P
    return None
            
# OneTreePoset function
def gen_tree_poset(upsilon):
    roots = []
    for linearOrder in upsilon:
        roots.append(linearOrder[0])
    if len(set(roots)) > 1:
        return None
    
    # m = number of linear orders; n = length of Vertex set
    m = len(upsilon)     
    n = len(upsilon[0])
    minRank = [0 for i in range(n)]
    numCoverRelation = 0
    coverRelationP = []

    for i in range(1,n):
        for j in range(m):
            v2 = rankInverse(i, upsilon[j])
            if minRank[int(v2)-1] == 0:
                v1 = rankInverse(i-1, upsilon[j])
                coverRelationP.append((int(v1),int(v2)))
                minRank[int(v2)-1] = i
                minRank[int(v1)-1] = i-1
                numCoverRelation +=1
        if numCoverRelation == n-1:
            break
    
    P = get_linear_extensions(coverRelationP)

    if VERIFY(P, upsilon):
        return coverRelationP
    
    return None

def VERIFY(P, Y):
    if sorted(P) == sorted(Y):
        return True
    return False

def rankInverse(index, linearOrder):
    # sample input: index = 3; linearOrder = 1234; 
    return linearOrder[index]       # output: 4

#returns the tuple (intersection, difference) of all posets in Pstar
def intersection_difference(Pstar):
    intersection = Pstar[0].copy()

    difference = []
    union = []
    for poset in Pstar[1:]:
        not_intersection = []
        for relation in intersection:
            if relation not in poset:
                not_intersection.append(relation)
            
        for relation in not_intersection:
            intersection.remove(relation)
    
    for poset in Pstar:
        union += poset
    union = sorted(list(set(union)))
    difference = getDifference(union, intersection)
    return (intersection, difference)

# Y = ['1234', '1243']

# P = gen_tree_poset(Y)

# if P != None:
#     print(P)

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

# P1 = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 5)]
# P2 = [(1, 2), (1, 3), (1, 4), (1, 5), (2, 4), (3, 2), (3, 4), (3, 5)]
# p = combinePosetv2(P1, P2)
# if p != None:
#     print(p)
# else:
#     print("No returned poset")




