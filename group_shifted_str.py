###https://baihuqian.github.io/2018-07-26-group-shifted-strings/
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        if len(strings) == 0:
            return []
        str_map = collections.defaultdict(list)
        for s in strings:
            delta = ord(s[0]) - ord('a')
            key = "".join([chr( ord(c) - delta) if c >= s[0] 
                else chr(26 + ord(c) - delta)])
            str_map[key].append(s)
        return str_map.values()

         

