class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=j=0
        result=0
        for j in range(len(nums)):
            if nums[j]==0:
                k-=1
            while k<0:
                i+=1
                if nums[i-1]==0:
                    k+=1

            result= max(j-i+1,result)
        return result

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(Solution().longestOnes(nums, k))
