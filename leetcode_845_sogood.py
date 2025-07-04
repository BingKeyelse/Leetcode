class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0
        
        max_length = up = down = 0

        for i in range(1, len(arr)):
            if (down > 0 and arr[i] > arr[i-1]) or (arr[i]==arr[i-1]):
                up = down = 0
            
            if arr[i] > arr[i-1]:
                up += 1
            elif arr[i] < arr[i-1] and up > 0:
                down += 1
                max_length = max(max_length, up + down + 1)
        
        return max_length
