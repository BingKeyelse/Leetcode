class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            cur = nums[i % n]
            while stack and stack[-1] <= cur:
                stack.pop()
            if i < n:
                if stack:
                    res[i] = stack[-1]
            stack.append(cur)

        return res


nums = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
Solution().nextGreaterElements(nums)
