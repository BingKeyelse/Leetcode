import re

class Solution(object):

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Chuyển sang chữ cái thường và xóa hết tất cả các dấu đặc biệt đi
        s= s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        s_new= list(s)
        print(s_new)
        i=0
        j= len(s_new)-1
        while i<j:
            if s_new[i] != s_new[j]:
                return False
            i=i+1
            j=j-1
        return True

s= "0P"
print(Solution().isPalindrome(s))