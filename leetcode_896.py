class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        bit_up=False
        bit_down=False

        for i in range(1,len(nums)):
            if nums[i]> nums[i-1]:
                bit_up=True

            if nums[i]< nums[i-1]:
                bit_down=True
                
        return not(bit_up and bit_down)