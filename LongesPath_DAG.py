### given a weighted directed acyclic graph (DAG)
### find the longest distsances from source to all other vertices 
### topological sort
def topologicalSortUtil(v):
    global Stack, visited, adj
    visited[v] = True

    for i in adj[v]:
        if not visited[i[0]]:
            topologicalSortUtil(i[0])
    Stack.append(v)

def longestPath(s):
    global Stack, visited, adj, V
    dist = [-10**9 for i in range(V)]

    for i in range(V):
        if (visited[i] == False):
            topologicalSortUtil(i)

    dist[s] = 0
    while (len(Stack) > 0):
        u = Stack[-1]
        del Stack[-1]
        ### next vertex from topological order

        ### update distances of all adjacent vertices
        if (dist[u] != 10**9):
            for i in adj[u]:
                if (dist[i[0]] < dist[u] + i[1]):
                    dist[i[0]] = dist[u] + i[1]

    for i in range(V):
        print("INF ", end="") if dist[i] == -10**9 else print(dist[i], end = " ")

if __name__ == '__main__':
    V, Stack, visited = 6, [], [False for i in range(7)]
    adj = [[] for i in range(7)]

    adj[0].append([1, 5])
    adj[0].append([2, 3])
    adj[1].append([3, 6])
    adj[1].append([2, 2])
    adj[2].append([4, 4])
    adj[2].append([5, 2])
    adj[2].append([3, 7])
    adj[3].append([5, 1])
    adj[3].append([4, -1])
    adj[4].append([5, -2])

    s = 1
    print("Following are longest distances from source vertex ",s)
    longestPath(s)


