###Prim's Minimum Spanning Tree (MST) adjacency matrix representation
###O(V^2)

import sys
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        mini = sys.maxsize

        for v in range(self.V):
            if key[v] < mini and mstSet[v] == False:
                mini = key[v]
                mini_index = v
        return mini_index

    ###function to construct and print MST for a graph
    def primMST(self):
        ### Key values used to pick minimum weight edge in cut
        key = [sys.maxsize]*self.V
        parent = [None]*self.V 
        key[0] = 0
        mstSet = [False]*self.V

        parent[0] = -1

        for cout in range(self.V):
            ### pick the minimum distance vertex from the set of vertices not yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            mstSet[u] = True
            ###put the minimum distance vertex in the shortest path tree

            ###update dist value of the adjacent vertices of the picked vertex only if the current distance is greater than new distance and the vertex is not in the shortest path tree yet
            for v in range(self.V):
                if self.graph[u][v]>0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

if __name__ == "__main__":
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

    g.primMST()



