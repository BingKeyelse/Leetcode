class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create databoard
        db={}

        for idx, num in enumerate(nums):
            point= target -num
            if point in db:
                return [db[point], idx]
            db[num]= idx