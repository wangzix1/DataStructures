### Prim MST with heap def
from collections import defaultdict
import sys

class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]

    def minHeapify(self, idx):
        smallest = idx
        left = 2*idx+1
        right = 2*idx+2

        if left < self.size and self.array[left][1] < \
                self.array[smallest][1]:
                    smallest = left
        if right < self.size and self.array[right][1] < \
                self.array[smallest][1]:
                    smallest = right

        if smallest != idx:
            #swap positions
            self.pos[self.array[smallest][0]] = idx
            self.pos[self.array[idx][0]] = smallest

            self.swapMinHeapNode(smallest, idx)
            self.minHeapify(smallest)

    def extractMin(self):
        if self.isEmpty() == True:
            return
        ###store the root node
        root = self.array[0]
        ###replace root with the last node
        lastNode = self.array[self.size-1]
        self.array[0] = lastNode
        ###update position of last node
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        ###reduce heap size and heapify root
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def decreaseKey(self, v, dist):
        ###get the index of v in heap array
        i = self.pos[v]
        self.array[i][1] = dist 
        ### travel up while the complete tree is not heapified
        while i > 0 and self.array[i][1] < \
                self.array[(i-1)//2][1]:
            self.pos[self.array[i][0]] = (i-1)//2
            self.pos[self.array[(i-1)//2][0]] = i
            self.swapMinHeapNode(i, (i-1)//2)

            i = (i-1)//2

    def isInMinHeap(self,v):
        ### check if a given vertex v is in min heap or not
        if self.pos[v] < self.size:
            return True
        return False

def printArr(parent, n):
    for i in range(1, n):
        print("% d - % d" % (parent[i], i))

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)

    def PrimMST(self):
        V = self.V
        key = []
        parent = []
        minHeap = Heap()
        ###initialize min heap with all vertices with initial weight inf
        for v in range(V):
            parent.append(-1)
            key.append(1e8)
            minHeap.array.append(minHeap.newMinHeapNode(v,key[v]))
            minHeap.pos.append(v)

        ###make key value of 0th vertex as 0 so that it's extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        minHeap.size = V
        while not minHeap.isEmpty():
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]

            ###traverse through all adjacent vertices of u (the extracted vertex) and update their distance values
            for pCrawl in self.graph[u]:
                v = pCrawl[0]

                ##if shortest distance to v is not finalized yet and distance to v through u is less than its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u
                    minHeap.decreaseKey(v, key[v])
        printArr(parent,V)
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.PrimMST()

