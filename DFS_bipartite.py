V = 4
def colorGraph(G, color, pos, c):
    if color[pos] != -1 and color[pos] != c:
        return False

    color[pos] = c
    ans = True
    for i in range(0, V):
        if G[pos][i]:
            if color[i] == -1:
                ans &= colorGraph(G, color, i, 1-c)
            if color[i] != -1 and color[i] != 1-c:
                return False
        if not ans:
            return False
    return True

def isBipartite(G):
    color = [-1]*V
    pos = 0
    return colorGraph(G, color, pos, 1)

if __name__ == "__main__":
    G = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]]

    if isBipartite(G):
        print("Y")
    else:
        print("N")
