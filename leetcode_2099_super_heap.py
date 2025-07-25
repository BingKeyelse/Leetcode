import heapq
class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Bước 1: Gắn chỉ số vào mỗi phần tử
        indexed = [(num, i) for i, num in enumerate(nums)]

        # Bước 2: Lấy k phần tử lớn nhất (theo giá trị)
        topk = heapq.nlargest(k, indexed, key=lambda x: x[0])

        # Bước 3: Sắp theo chỉ số gốc để giữ nguyên thứ tự ban đầu
        topk.sort(key=lambda x: x[1])

        # Bước 4: Trả về danh sách giá trị
        return [x[0] for x in topk]
