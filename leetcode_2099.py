
class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        table=[]
        for index, num in enumerate(nums):
            table.append([index,num])
            '''Table has a type [idx, value]'''

        # Sort table thus value 
        top_k= sorted(table, key= lambda x: -x[1])[:k]

        top_k.sort(key=lambda x: x[0])

        return [value for _,value in top_k]

nums=[-1,-2,3,4]

print(Solution().maxSubsequence(nums,3))
        

