import collections

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        s_count= collections.Counter(s)
        t_count= collections.Counter(t)
        sum=0
        for key in t_count:
            if s_count.get(key):
                if t_count[key]>s_count[key]:
                    sum+= t_count[key]-s_count[key]
            else:
                sum+=t_count[key]
        print(sum)
          


s= "bab"
t= "aba"
Solution().minSteps(s,t)

        