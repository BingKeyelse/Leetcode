import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        table= Counter(words)

        h=[]

        for tex, fre in table.items():
            heapq.heappush(h, (-fre,tex))
        
        print(h)
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(h)[1])
        return result

words = ["i","love","leetcode","i","love","coding"]
# words = ["b", "a", "a", "b", "c", "c"]
k = 2
print(Solution().topKFrequent(words,k))