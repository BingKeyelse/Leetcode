class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))
            else:
                nums[index] = -nums[index]
        return result
    
a=[4,3,2,7,8,2,3,1]
Solution().findDuplicates(a)