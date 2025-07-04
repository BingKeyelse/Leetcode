class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        value=[]
        for i in range(len(nums)):
            a=0
            b= len(nums)-1
            product=1
            while a< i:
                product*= nums[a]
                a+=1
                
            while i<b:
                product*= nums[b]
                b-=1
            value.append(product)
        return value
    
a=[-1,1,0,-3,3]
print(Solution().productExceptSelf(a))        