class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        count = 1
        result.append(s[0])  # thêm ký tự đầu tiên vào

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1  

            if count <= 2:
                result.append(s[i])

        return ''.join(result)
s = "leeetcode"
print(Solution().makeFancyString(s))




        