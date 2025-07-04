class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr= [0]*(len(nums)+1)
        result=[]

        for num in nums:
            arr[num]+=1
        for i in range(1,len(arr)):
            if arr[i]==0:
                result.append(i)
        return result

        