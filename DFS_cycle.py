from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True
        ### add to recursion stack

        for nb in self.graph[v]:
            if visited[nb] == False:
                if self.isCyclicUtil(nb, visited, recStack):
                    return True
            elif recStack[nb] == True:
                return True

        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False]*(self.V + 1)
        recStack = [False]*(self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack):
                    return True

        return False

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")



