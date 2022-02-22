###https://www.goodtecher.com/leetcode-1182-shortest-distance-to-target-color/
from collections import defaultdict
class Solution:
    def shortestDistanceColor(self, colors:List[int], 
            queries: List[List[int]])->List[int]:
        mp = defaultdict(list)
        for i, c in enumerate(colors):
            mp[c].append(i)
        res = []
        for i, t in queries:
            if t not in mp:
                res.append(-1)
                continue
            ls = mp[t]
            idx = bisect.bisect_left(ls, i)
            
            nearest = abs(ls[max(idx-1, 0)] - i)
            nearest = min(nearest, abs(ls[min(idx, len(ls)-1)] - i))

            res.append(nearest)

        return res
