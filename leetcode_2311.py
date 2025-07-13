class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        leng = len(s)
        value = 0
        test = ''
        new_s = ''

        for i in range(leng-1, -1, -1):
            test = s[i] + test
            value = int(test, 2)
            if value <= k:
                new_s = test
            else:
                test = new_s
        print(len(new_s))
        return len(new_s)


s = "00101001"
k = 1
Solution().longestSubsequence(s, k)
