class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack=[]
        result=[0]*len(temperatures)
        
        for i in range(len(temperatures)-1,-1,-1):
            if not stack:
                stack.append([temperatures[i], i])
            else:
                while stack:
                    if temperatures[i] >=stack[-1][0]:
                        stack.pop()
                    else:
                        result[i]=(stack[-1][1]-i)
                        stack.append([temperatures[i], i])
                        break
                if not stack:
                    stack.append([temperatures[i], i])
                    
        return result
    
a= [73,74,75,71,69,72,76,73]
Solution().dailyTemperatures(a)