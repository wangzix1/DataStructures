###https://goodtecher.com/leetcode-1762-buildings-with-an-ocean-view/

class Solution:
    def findBuildings(self, heights:List[int]) -> List[int]:
        res = []
        prev_max = None
        for i in range(len(heights)-1, -1, -1):
            height = heights[i]

            if not prev_max:
                prev_max = height
                res.append(i)
            else:
                if height > prev_max:
                    res.append(i)
                prev_max = max(prev_max, height)

        return res[::-1]
