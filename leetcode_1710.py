class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        nums=sorted(boxTypes, key=lambda x: -x[1])
        count=0

        for num in nums:
            if num[0]< truckSize:
                truckSize= truckSize-num[0]
                count+=num[0]* num[1]
            else:
                count+=truckSize* num[1]
                break
        return count


boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(Solution().maximumUnits(boxTypes, truckSize))