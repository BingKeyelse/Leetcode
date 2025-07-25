class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        aset= set()
        j=0
        sum= 0
        result=0

        for i in range(len(nums)):
            
            while nums[i] in aset: # Neu co trung lap
                aset.remove(nums[j])
                sum-=nums[j]
                j+=1
                
            aset.add(nums[i])
            sum+=nums[i]
            result=max(result,sum) #Lay ket qua la gia tri max

        return result
