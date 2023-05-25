import networkx as nx
from TreePoset_Utils_v2 import get_linear_extensions

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

def areTreePosets(group_posets):
    flag = True
    for poset in group_posets:
        if not isTreePoset(poset):
            flag = False
            return flag
    return flag

def isAllConnected(P,n):
    for p in P:
        check_vertices = [False for x in range(n)] #array that checks if all vertices are included
        for (a,b) in p:
            check_vertices[a-1] = True
            check_vertices[b-1] = True
        if False not in check_vertices and nx.is_directed_acyclic_graph(nx.DiGraph(p)):
            continue
        else:
            return False
    return True

def binaryToCover(P,n):
    coverRelations = []
    for (u,v) in P:
        if (u,v) in coverRelations:
            continue
        if len(coverRelations) == n - 1:
            break
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

def covered(group_posets):
    coveredlinearorders = []
    for poset in group_posets:
        coveredlinearorders += get_linear_extensions(poset)
    coveredlinearorders = [int(x) for x in list(set(coveredlinearorders))]
    return sorted(coveredlinearorders)
