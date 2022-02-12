### Kruskal's Minimum Spanning Tree of a given connected, undirected and weighted graph
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [] 

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    ###path compression
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    ###union by rank
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        res = []
        i = 0
        e = 0
        ###step1 sort edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, 
                key = lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            ### create V subsets with single elements
            parent.append(node)
            rank.append(0)

        while e < self.V-1:
            ###step2 pick the smallest edge and increment the index for iteration
            u,v, w = self.graph[i]
            i += 1 ###index of edges
            pu = self.find(parent, u)
            pv = self.find(parent, v)

            if pu != pv:
                e += 1 
                res.append([u,v,w])
                self.union(parent, rank, pu, pv)
            ###if no cycle add the edge else discard the edge

        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, w in res:
            minimumCost += w
            print("%d -- %d == %d" % (u,v,w))
        print("Minimum Spanning Tree by Kruskal", minimumCost)


###driver code
if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0,1,10)
    g.addEdge(0,2,6)
    g.addEdge(0,3,5)
    g.addEdge(1,3,15)
    g.addEdge(2,3,4)

    g.KruskalMST()
