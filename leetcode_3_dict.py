class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_index = {}
        j = 0
        result = 0
        for i, char in enumerate(s):
            if char in last_index and last_index[char] >= j:
                j = last_index[char]
            last_index[char] = i
            result = max(result, i - j)
        return result
    
# s = "abcabcbb"
# print(Solution().lengthOfLongestSubstring(s))
print(Solution().lengthOfLongestSubstring(eval(input())))