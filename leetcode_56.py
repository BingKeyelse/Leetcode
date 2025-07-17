class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0]) # Must to sort
        result =[]

        for inter in intervals:
            if not result or result[-1][1]<inter[0]:
                result.append(inter)
            else:
                result[-1][-1]= max(result[-1][-1], inter[-1])
        return result