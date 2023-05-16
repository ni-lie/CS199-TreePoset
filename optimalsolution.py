import os, sys
from itertools import combinations
import networkx as nx

#UTILS
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

def isAllConnected(parents, relations):
    root = 0
    for i in parents:
        if i == 0:
            root = i + 1
    
def VERIFY_GROUP(Group_P, Y): 
    covered = []
    for P in Group_P:
        covered += get_linear_extensions(P)
    if sorted(covered) == sorted(Y):
        return True
    else:
        return False
    
args = sys.argv[1:]
args[0] = int(args[0])

#get number of vertices
n = args[0]
vertices = [int(x) for x in range(1,n+1)]

#generate all possible tuples
all_relations = []
for a in range(1,n+1):
    for b in range(1,n+1):
        if a!=b:
            all_relations.append((a,b))

#generate all possible permutations of tuples of size 2
all_combinations_relations = combinations(all_relations, n-1)

#remove all invalid permutations; e.g [(1,2),(2,1)] - does not contain 3
Tree_Posets = []
for p in list(all_combinations_relations):
    check_vertices = [False for x in range(n)] #array that checks if all vertices are included
    parent = [0 for x in range(n)] #array of number of parents of a vertex
    cycle = False
    isTreePoset = True
    for (a,b) in p:
        if (b,a) in p:
            cycle = True
        check_vertices[a-1] = True
        check_vertices[b-1] = True
        parent[b-1] += 1
        
    #Check if the valid poset permutation is a tree poset
    for v in parent:
        if (v > 1) or (0 not in parent):
            isTreePoset = False
            break

    #check if all edges are connected
    if False not in check_vertices and isTreePoset and not cycle and nx.is_directed_acyclic_graph(nx.DiGraph(p)):
        Tree_Posets.append(list(p))

#output lines
lines = []
#generate all one-tree posets
lines.append("k = 1")
covered_groups_LE = []
for P in Tree_Posets:
    L_P = get_linear_extensions(P)
    covered_groups_LE.append(L_P)
    lines.append(str(P) + " L(P) = " + str(L_P))

count_one_tree_posets = len(covered_groups_LE)

#generate all possible groups of posets

#get all possible combinations of size k from range 2 to len(one-tree posets)
#get linear extensions of the posets and combine into one group of linear extensions
#convert into set, then convert back to list
#check if group is already covered
#if no, print, append to covered groups


for i in range(2, count_one_tree_posets + 1): #end shoud be count_one_tree_posets + 1
    lines.append("k = " + str(i))
    combinations_of_posets = combinations(Tree_Posets, i)
    for group in combinations_of_posets:
        covered_group = []
        for poset in group:
            covered_group += get_linear_extensions(list(poset))
        covered_group = set(covered_group)
        covered_group = sorted(covered_group)
        if covered_group not in covered_groups_LE:
            lines.append(str(list(group)) + " L(P) = " + str(covered_group))
            covered_groups_LE.append(covered_group)
        #else:
        #    print("NOT INCLUDED:", group, covered_group)

if not os.path.exists("optsol/"):
    os.makedirs("optsol/")


if not os.path.exists(f"optsol/{args[1]}/"):
    os.makedirs(f"optsol/{args[1]}/")
    
output = open(f"optsol/{args[1]}/{args[0]}{args[1]}optsol.txt", "w")

for l in lines:
    output.write(l+"\n")
output.close()

print("FINISH")

