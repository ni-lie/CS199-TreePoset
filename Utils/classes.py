# source: songsong and angeles
import time

INVALID = -1
Sequence = list[int]
Vertices = list[int]
Relations = list[tuple[(int, int)]]
LinearOrders = list[list[int]]

class Poset():

    def __init__(self, size: int, relations: Relations, isNull = False):
        self.vertices = None if isNull else [i for i in range(1, size + 1)]
        self.relations = None if isNull else sorted(relations)

    def isEmpty(self, keyword = "both"):
        if keyword in ['both', 'vertices'] and self.vertices == None: return True
        if keyword in ['both', 'relations'] and self.relations == None: return True

        return False

    def isEqual(self, poset: "Poset") -> bool:
        if ((not self.isEmpty()) and 
            max(self.vertices) == max(poset.vertices) and
            sorted(self.relations) == sorted(poset.relations)): return True
        
        return False

    def isIn(self, posets: list["Poset"]) -> bool:
        for poset in posets:
            if self.isEqual(poset): return True
        
        return False

    def subtract(self, poset: "Poset") -> Relations:
        relations = []
        for relation in self.relations:
            if relation not in poset.relations:
                relations.append(relation)

        return relations

    def generateLinearExtensions(self) -> list[LinearOrders]:
        graph = Graph(self.relations, len(self.vertices), [])
        graph.getAllTopologicalOrders()
        
        return graph.listofLO

class LinearOrder(Poset):

    def __init__(self, sequence: Sequence):
        self.sequence = sequence
        super().__init__(len(sequence), self._getRelations(sequence))

    def _getRelations(self, sequence: Sequence) -> Relations:
        relations = []
        for i in range(0, len(sequence) - 1):
            for j in range(i + 1, len(sequence)):
                relations.append((sequence[i], sequence[j]))
        
        return relations

class Graph:

    def __init__(self, edges, N, inputs):
        self.inputLO = inputs
        self.listofLO = [] 
        self.edges = edges
        self.adjList = [[] for _ in range(N)]

        self.indegree = [0] * N
        for (src, dst) in edges:
            self.adjList[src-1].append(dst-1)
 
            self.indegree[dst-1] = self.indegree[dst-1] + 1
    
    def _findAllTopologicalOrders(self, path, marked, N):
        for v in range(N):
            if self.indegree[v] == 0 and not marked[v]:
                for u in self.adjList[v]:
                    self.indegree[u] = self.indegree[u] - 1
                path.append(v)
                marked[v] = True
                self._findAllTopologicalOrders(path, marked, N)

                for u in self.adjList[v]:
                    self.indegree[u] = self.indegree[u] + 1

                path.pop()
                marked[v] = False

        if len(path) == N:
            path = [i+1 for i in path]
            self.listofLO.append(path.copy())

    def getAllTopologicalOrders(self):
        lenNodes = len(self.adjList)
        marked = [False] * lenNodes
        path = []
        self._findAllTopologicalOrders(path, marked, lenNodes)

class Timer:

    def __init__(self):
        self._start_time = None
    
    def start(self):
        self._start_time = time.perf_counter()
    
    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        return elapsed_time