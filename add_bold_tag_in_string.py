###https://www.cnblogs.com/grandyang/p/7043394.html
class Solution:
    def boldWords(words, S):
        N = len(S)
        mark = [0]*N
        res = ""

        for w in words:
            L =len(w)
            for i in range(N-L):
                S[i] == w[0] and S[i:i+L] == w:
                    for j in range(i, i+L):
                        mark[j] = 1
        for i, c in enumerate(S):
            if mark[i] and not mark[i-1]:
                res += "<b>"
            res.append(S[i])
            if mark[i] and (i+1<N and not mark[i+1]):
                res += "</b>"

        return res
