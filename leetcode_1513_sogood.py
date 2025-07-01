class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        result = 0
        for c in s:
            if c == '1':
                count += 1
                result += count
            else:
                count = 0
        return result % (10**9 + 7)
        