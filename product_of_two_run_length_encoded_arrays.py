###https://blog.51cto.com/u_15344287/3646343
###https://linlaw0229.github.io/2021/09/19/1868-Product-of-Two-Run-Length-Encoded-Arrays/
class Solution:
    def findRLEArray(self, encode1:List[List[int]], encode2:List[List[int]])->List[List[int]]:
        p, q = 0, 0
        i, j = None, None##encode1[p][1], encode2[q][1]
        res = []
        while p < len(encode1) and q < len(encode2):
            if not i and p < len(encode1):
                i = encode1[p][1]
            if not j and q < len(encode2):
                j = encode2[q][1]

            num = encode1[p][0]*encode2[q][0]
            count = min(i,j)
            i -= count
            j -= count
            if res and num == res[-1][0]:
                res[-1][1] += count
            else:
                res.append([num, count])
            p += 1 if not i else 0
            q += 1 if not j else 0
        return res

