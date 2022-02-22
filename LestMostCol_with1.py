##https://blog.csdn.net/MrJustin/article/details/105672624
### binary matrix, row non-decreasing
### BinaryMatrix.get(x,y)
### BinaryMatrix.dimensions()
### 1. each row binary search
### O(nlogm)
class Solution:
    def leftMostColumnWithOne(M):
        n, m = M.dimensions()
        res = m
        for i in range(n):
            l, r = 0, m-1
            while l < r:
                md = l+(r-l)//2
                if M.get(i,md) == 0:
                    l = md+1
                else:
                    r = md
            if M.get(i, l):
                res = min(res, l)
        return -1 if res == m else res


###2. Linear, start from upper right corner, if 1, go left; until reach 0, go down
        res = m
        x = 0
        y = m-1
        while x < n and y >= 0:
            if M.get(x,y):
                res = y
                y -= 1
            else:
                x += 1
        return -1 if res == m else res


