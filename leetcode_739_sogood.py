class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        res = [0] * n
        stack = []  # Stack lưu index

        for i in range(n - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
 