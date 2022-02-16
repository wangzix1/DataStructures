class Solution(self):
    def verticalOrder(self, root):
        """
        :type root:TreeNode
        :rtype:List[list[int]]
        """
        if not root:
            return []

        cols = collections.defaultdict(list)
        q = [(root, 0)]

        while q:
            new_q = []
            for node, col in q:
                cols[col].append(node.val)
                if node.left:
                    new_q.append((node.left, col-1))
                if node.right:
                    new_q.append((node.right, col+1))
            q = new_q
        return [cols[c] for c in sorted(cols.keys())]
            
            
