class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Những phần tử còn lại trong stack không có next greater
        for num in stack:
            next_greater[num] = -1

        # Trả kết quả cho nums1
        return [next_greater[num] for num in nums1]


# Solution().nextGreaterElement(eval(input()))
num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
Solution().nextGreaterElement(num1, num2)
