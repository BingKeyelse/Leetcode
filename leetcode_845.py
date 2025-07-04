class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        longest =0
        for i in range(1,len(arr)-1):
            if arr[i]> arr[i-1] and arr[i]> arr[i+1]:
                left= i-1
                right= i+1

                while left>0 and arr[left]> arr[left-1]:
                    left-=1

                while right< (len(arr)-1) and arr[right]> arr[right+1]:
                    right+= 1

                longest = max(longest, right-left+1)
        return longest
    
a= [2,1,4,7,3,2,5]
print(Solution().longestMountain(a))