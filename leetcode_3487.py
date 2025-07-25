class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        aset=set()
        sum_=0

        value_max=max(nums)
        negative=True

        for num in nums:
            if not num in aset and num>=0:
                sum_ += num
                aset.add(num)
            if num>=0:
                negative=False

        return (sum_ if negative==False else value_max)

nums= [-100]
print(Solution().maxSum(nums))