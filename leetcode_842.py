class Solution(object):
    def splitIntoFibonacci(self, num):
        n = len(num)

        def backtrack(index, path):
            if index == n and len(path) >= 3:
                return path[:]

            for i in range(index + 1, n + 1):
                if num[index] == '0' and i > index + 1:
                    break  # loại số có 0 ở đầu

                val = int(num[index:i])
                if val > 2**31 - 1:
                    break

                if len(path) < 2 or path[-1] + path[-2] == val:
                    path.append(val)
                    res = backtrack(i, path)
                    if res:
                        return res
                    path.pop()
                elif len(path) >= 2 and path[-1] + path[-2] < val:
                    break  # vượt target sớm → cắt

            return []

        return backtrack(0, [])
