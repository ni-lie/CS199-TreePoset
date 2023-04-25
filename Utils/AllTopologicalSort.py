class Poset:
    #initializing poset P(v, cover_relations)
    def __init__(poset, vertices, cover_relations):
        poset.vertices = vertices                           #list of vertices
        poset.cover_relations = cover_relations             #list of tuples containing all cover relations
        poset.indegree = [0] * len(vertices)                #initializing list contaning indegree values (either 0 or 1) of each vertex 
        for edge in cover_relations:                        #for each edge: (u, v) in cover_relations
            poset.indegree[edge[1] - 1] = 1                 #set indegree of v to 1
        poset.adjList = [[] for v in range(len(vertices))]  #initialize list of adjacent lists for each vertex
        for v in range(len(vertices)):                      #for each vertex, find all adjacent elements
            for pair in cover_relations:                    #check if current vertex is in current pair
                if v in pair:
                    if pair[0] == v:                        #if current pair = (v, u), append vertex u to adjList[v]
                        poset.adjList[v-1].append(pair[1])  
                    else:                                   #if current pair = (u, v), append vertex u to adjList[v]
                        poset.adjList[v-1].append(pair[0])

#Recursive function to find all topological orderings of a given DAG
def findAllTopologicalOrders(poset, path, discovered, N):  #algorithm based on https://www.geeksforgeeks.org/all-topological-sorts-of-a-directed-acyclic-graph/
    # do for every vertex
    for v in range(1,N+1):

        # proceed only if in-degree of current node is 0 and
        # current node is not processed yet
        if poset.indegree[v-1] == 0 and not discovered[v-1]:

            #for every adjacent vertex u of v,
            #reduce in-degree of u by 1
            for u in poset.adjList[v-1]:
                poset.indegree[u-1] = poset.indegree[u-1] - 1

            #include current node in the path
            #and mark it as discovered
            path.append(v)
            discovered[v-1] = True
            
            #recur
            findAllTopologicalOrders(poset, path, discovered, N)

            # backtrack: reset in-degree
            # information for the current node
            for u in poset.adjList[v-1]:
                poset.indegree[u-1] = poset.indegree[u-1] + 1
            
            # backtrack: remove current node from the path and mark it as undiscovered
            # mark it as undiscovered
            path.pop()
            discovered[v-1] = False

    #print the topological order if
    #all vertices are included in the path
    if len(path) == N:
        print(path)

def printAllTopologicalOrders(poset):
    N = len(poset.vertices)
    discovered = [False] * N
    path = []
    findAllTopologicalOrders(poset, path, discovered, N)

P = Poset((1,2,3,4,5), [(1,2), (1,3), (2,4), (3,5)])  
printAllTopologicalOrders(P)