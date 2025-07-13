class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        aSet= set()

        i=0
        j=0
        result=0

        while i< len(s):
            if s[i] in aSet:
                aSet.remove(s[j])
                j+=1
            else:
                aSet.add(s[i])
                i+=1
            result=max(len(aSet), result)
        
        return result

# s = "abcabcbb"
# print(Solution().lengthOfLongestSubstring(s))
print(Solution().lengthOfLongestSubstring(eval(input())))
