###https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/298.%20Binary%20Tree%20Longest%20Consecutive%20Sequence.md

class Solution(object):
    """
    :type root: TreeNode
    :rtype: int
    """
    def dfs(root, curLen):
        self.res = max(curLen, self.res)
        if root.left:
            if root.val == root.left.val+1:
                dfs(root.left, curLen+1)
            else:
                dfs(root.left, 1)

        if root.right:
            if root.right.val == root.val + 1:
                dfs(root.right, curLen+1)
            else:
                dfs(root.right,1)

    if not root: return 0
    self.res = 0
    dfs(root,1)
    return self.res
