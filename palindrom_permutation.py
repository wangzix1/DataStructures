###https://blog.csdn.net/danspace1/article/details/86552613
class Solution(object):
    def PermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cnt = Counter(s)
        odd = sum([v%2 for k,v in cnt.items()])
        if odd > 1:
            return False
        return True

