import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        # Bước 1: Hash đếm từ
        count = Counter(words)  # {'i':3, 'love':2, 'leetcode':1}

        # Bước 2: Đưa vào heap theo (-tần suất, từ)
        heap = []
        for word, freq in count.items():
            heapq.heappush(heap, (-freq, word))  # max heap theo freq, min theo word nếu freq bằng nhau

        # Bước 3: Lấy ra k từ đầu
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
    
words = ["i","love","leetcode","i","love","coding"]
k = 2
Solution().topKFrequent(words,k)
