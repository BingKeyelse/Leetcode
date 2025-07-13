class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check constraints
        if not (1 <= len(nums) <= 1000):
            raise ValueError("Length of nums must be between 1 and 1000.")
        if any(n < -10**9 or n > 10**9 for n in nums):
            raise ValueError(
                "Each number in nums must be between -10^9 and 10^9.")

        leng = len(nums)
        total = 0

        for i in range(leng):
            current_max = current_min = nums[i]
            for j in range(i, leng):
                current_max = max(current_max, nums[j])
                current_min = min(current_min, nums[j])
                total += current_max - current_min

        return total
