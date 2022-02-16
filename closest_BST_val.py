class Solution:
    def closestValue(self, root:TreNode, target:float) ->int:
        res = root.val
        nd = root
        while nd:
            res = min(res, nd.val, key = lambda x: abs(x-target))
            nd = nd.left if nd.val > target else nd.right
        return res

