class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack =[]
        store=dict()

        for idx in range(len(nums2)-1, -1, -1):
            if not stack:
                store[nums2[idx]]=-1
                stack.append(nums2[idx])
            else:
                while stack:
                    if nums2[idx] >stack[-1]:
                        stack.pop()
                    else:
                        store[nums2[idx]]=stack[-1]
                        stack.append(nums2[idx])
                        break

                if not stack:
                    store[nums2[idx]]=-1
                    stack.append(nums2[idx])
                    
        result=[]
        for num in nums1:
            result.append(store[num])
        return result
    

                

            
        
    
num1=[1,3,5,2,4]
num2=[6,5,4,3,2,1,7]
Solution().nextGreaterElement(num1, num2)

