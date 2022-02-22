import collections
def Solution(words):
#    records = []
#    for i in range(len(words)-1):
#        for j in range(min(len(words[i]), len(words[i+1]))):
#            if words[i][j] == words[i+1][j]:
#                continue
#            records.append([words[i][j], words[i+1][j]])
#            break
#
#    ### 
#    if not records:
#        return []
#
#    characters = set()
#    for word in words:
#        characters.update(word)

 #   ###buble sorting O(n^2)
 #   characters = list(characters)
 #   last_character = []
 #   while last_character != characters:
 #   last_character = characters.copy()

 #   for record in records:
 #       first_index = characters.index(record[0])
 #       second_index = characters.index(record[1])
 #       if first_index > second_index:
 #           characters[first_index], characters[second_index] = \
 #                   characters[second_index], characters[first_index]

#    ###topological sort O(n^2)
#    overlapped_char = set(i[0] for i in records)
#    missing_key = (characters - overlapped_char).pop()
#    all_char = len(characters)
#    characters = [missing_key]
#    while len(characters) < all_char:
#        for record in records:
#            if record[1] == characters[0]:
#                characters = [record[0]]+characters
#    return characteres
###BFS 
#    res = []
#    indegree = collections.Counter()
#    for (s,e) in records:
#        indegree[e]+=1
#    q = collections.deque([])
#    for a in characters:
#        if indegree[a] == 0:
#            q.append(a)
#            res.append(a)
#
#    while q:
#        c = q.popleft()
#        for (s,e) in records:
#            if s == c:
#                indegree[e]-=1
#                if indegree[e] == 0:
#                    q.append(e)
#                    res.append(e)
#    return res if len(res) == len(characters) else []

### DFS
    g = [[False]*26 for _ in range(26)]
    visited = [False]*26
    res = []
    for w in words:
        for c in w:
            g[ord(c) - ord('a')][ord(c) - ord('a')] = True

    for i in range(len(words)-1):
        mn = min(len(words[i]), len(words[i+1]))
        j = 0
        while j < mn:
            if words[i][j] != words[i+1][j]:
                g[ord(words[i][j]) - ord('a')][ord(words[i+1][j]) - ord('a')] = True
                break
            j += 1
        if j == mn and len(words[i]) > len(words[i+1]):
            return []
    
    def dfs(i, visited):
        if not g[i][i]:
            return True
        visited[i] = True
        for ii in range(26):
            if ii == i or not g[ii][i]:
                continue
            if visited[ii]:
                return False
            if not dfs(ii, visited):
                return False
        visited[i] = False
        g[i][i] = False
        res.append(chr(ord('a')+i))
        return True

    for i in range(26):
        if not dfs(i, visited):
            return []
    return res



if __name__ == '__main__':
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    print(Solution(words))
    

