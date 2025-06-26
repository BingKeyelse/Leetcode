class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
            elif s_list[i] in vowels:
                j -= 1
            elif s_list[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1

        return "".join(s_list)
