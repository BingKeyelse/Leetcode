class Solution(object):
    def removeVowels(self, s):
        new_s=''
        for letter in s:
            if not letter in {'u', 'e', 'o', 'a', 'i'}:
                new_s+= letter
        return new_s
    
letter= 'leetcodeisacmmonityforcoders'
print(Solution().removeVowels(letter))