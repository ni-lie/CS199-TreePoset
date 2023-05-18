import networkx as nx

def isTreePoset(P):
    flag = True
    #find number of vertices
    n = 1
    for pair in P:
        if max(pair) > n:
            n = max(pair)

    parent = [0 for x in range(n)] #array of number of parents of a vertex
    
    #store number of parents of each vertex by checking each pair in P
    for (a,b) in P:
        parent[b-1] += 1
        
    #check if a vertex has multiple parents,
    for v in parent:
        if (v > 1) or (0 not in parent): #if 0 not in parent, Poset possibly has a cycle
            flag = False
            break
    return flag

def areTreePosets(group_posets):
    flag = True
    for poset in group_posets:
        if not isTreePoset(poset):
            flag = False
            return flag
    return flag

def isAllConnected(P,n):
    check_vertices = [False for x in range(n)] #array that checks if all vertices are included
    for (a,b) in P:
        check_vertices[a-1] = True
        check_vertices[b-1] = True
    if False not in check_vertices and nx.is_directed_acyclic_graph(nx.DiGraph(P)):
        return True
    else:
        return False