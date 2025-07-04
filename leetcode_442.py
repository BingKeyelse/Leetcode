import collections
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        arr=collections.Counter(nums)
        value= []

        for key in arr:
            if arr[key]>1:
                value.append(key)

        return value


        