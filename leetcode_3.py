class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list=list(s)
        value=0 
        i=j=0

        while i< len(s):
            j=i+1
            while j< len(s):
                if s_list[j]== s_list[j-1]:
                    break
                j+=1
            value=max(value,j-i)     
            i=j
        return value


s="abcabcbb"
print(Solution().lengthOfLongestSubstring(s))