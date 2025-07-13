class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
       
        stack=[]
        mapping={')': '(', '}': '{', ']': '['}

        for letter in s:
            if letter in mapping:
                if len(stack)>0 and mapping[letter]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        return not stack

print(Solution().isValid(eval(input())))