class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        store=dict()
        for i in range(len(nums2)):
            store[nums2[i]]=i
        
        stack=[]

        for num in nums1:
            value=-1
            for i in range(store[num], len(nums2)):
                if nums2[i]> num:
                    value=nums2[i]
                    break
            stack.append(value)

        return stack
    
# Solution().nextGreaterElement(eval(input()))
num1=[4,1,2]
num2=[1,3,4,2]
Solution().nextGreaterElement(num1, num2)

