### https://blog.csdn.net/qq_37821701/article/details/108807236
### topological sort

class Solution:
    def alienOrder(self, words:list[str])->str:
        ### adject matrix of graph
        adj_list = collections.defaultdict(sef)

        indegrees = {}
        for w in words:
            for c in w:
                if c in indegrees:
                    continue
                indegrees[c] = 0

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c!=d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                    break
            else:
                ### this else will still match with if inside the for loop
                if len(second_word) < len(first_word):
                    return ''
                ### check if the second word is a prefix of the first word
            q = deque()
            for k, v in indegrees.items():
                if v==0:
                    q.append(k)

            ans = []
            while q:
                c = q.popleft()
                ans.append(c)
                for d in adj_list[c]:
                    indegrees[d] -= 1
                    if indegrees[d] == 0:
                        q.append(d)

            if len(ans) < len(indegrees):
                return ''

            return "".join(ans)

