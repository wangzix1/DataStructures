### bipartite 

### 1. if graph is connected, start with source 0 and assume vertices are visited from it

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = [[0]*V for _ in range(V)]

"""
    def isBipartite(self, src):
        ### create a color array to store colors assigned to all vertices
        ### vertex number: used as index in the array
        ### value -1 of colorArr[i] is used to indicate no color is assigned to vertex 'i'. 1, 0 two colors
        colorArr = [-1]*self.V
        colorArr[src] = 1
        ### create a queue (FIFO) of vertex numbers and enqueue source vertex for BFS traversal
        q = []
        q.append(src)
        while q:
            u = q.pop()
            if self.graph[u][u] == 1: 
                ### self-loop
                return False

            for v in range(self.V):
                if self.graph[u][v] and colorArr[v] == -1:
                    colorArr[v] = 1 - colorArr[u]
                    q.append(v)
                elif self.graph[u][v] and colorArr[v] == colorArr[u]:
                    return False
        return True
"""


    ### if not connected graph
    def isBipartiteUtil(self, src):
        q = []
        q.append(src)
        while q:
            u = q.pop()
            if self.graph[u][u]:
                return False
            for v in range(self.V):
                if (self.graph[u][v] == 1 and self.colorArr[v] == -1):
                    self.colorArr[v] = 1 - self.colorArr[u]
                    q.append(v)
                elif (self.graph[u][v] == 1 and self.colorArr[v] == self.colorArr[u]):
                    return False
        return True

    def isBipartite(self):
        self.colorArr = [-1 for i in range(self.V)]
        for i in range(self.V):
            if self.colorArr[i] == -1:
                if not self.isBipartiteUtil(i):
                    return False
        return True

if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
            ]

    print ("Yes" if g.isBipartite(0) else "No")

