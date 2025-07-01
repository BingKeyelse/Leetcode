class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        res = 0

        # Tổng max
        stack = []
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] < nums[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                res += nums[j] * (i - j) * (j - k)
            stack.append(i)

        # Trừ tổng min
        stack = []
        for i in range(n + 1):
            while stack and (i == n or nums[stack[-1]] > nums[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                res -= nums[j] * (i - j) * (j - k)
            stack.append(i)

        return res


a=[1,2,3]
Solution().subArrayRanges(a)