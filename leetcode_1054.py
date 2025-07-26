from collections import Counter
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        count = Counter(barcodes)

        # Chỉ giữ keys, sort theo tần suất giảm dần
        datas = sorted(count.keys(), key=lambda x: -count[x])

        result = [0] * len(barcodes)
        i = 0

        for val in datas:
            for _ in range(count[val]):  # Tra freq từ Counter
                result[i] = val
                i += 2
                if i >= len(barcodes): 
                    i = 1  # chuyển sang vị trí lẻ

        return result

barcodes = [1,1,1,2,2,2]
print(Solution().rearrangeBarcodes(barcodes))
        