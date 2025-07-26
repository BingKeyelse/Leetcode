from collections import Counter
class Solution(object):
    def reorganizeString(self, s):
        
        c = Counter(s)
        n = len(s)
        
        if max(c.values()) > (n+1) // 2 : return ''

        sorted_chars = sorted(c.items(), key=lambda x: -x[1])

        res = [0] * n
        i = 0

        for key , value in sorted_chars:

            for _ in range(value):

                res[i] = key

                i += 2

                if i >= n: i = 1
            
        
        return ''.join(res)

s = "aaabbcc"
print(Solution().reorganizeString(s))