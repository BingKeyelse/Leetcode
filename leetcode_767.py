import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        table_hash = Counter(s)

        for fre in table_hash.values():
            if fre > (len(s)+1)//2:
                return ""

        prev_fre=0
        prev_text=""
        result=''

        max_heap=[]

        # Create max Heap 
        for text, fre in table_hash.items():
            heapq.heappush(max_heap, (-fre,text))
        
        #Take per data in heap
        while max_heap:

            fre, text= heapq.heappop(max_heap)

            result+=text

            if prev_fre <0:
                heapq.heappush(max_heap, (prev_fre, prev_text))

            prev_fre= fre+1
            prev_text= text
        return "".join(result)

  
s = "aab"
print(Solution().reorganizeString(s))