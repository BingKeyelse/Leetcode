from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        ## Method 1
        sorted_words = sorted(count.items(), key=lambda x: (-x[1], x[0]))

        ## Method 2
        sorted_words = sorted(count.keys(), key=lambda x: (-count[x], x))

        return [word for word, _ in sorted_words[:k]]
    

words = ["i","love","leetcode","i","love","coding"]
k = 2
Solution().topKFrequent(words,k)
