class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack=[]
        point=0
        value=0
        for sym in s:
            if sym =='(': # Là kí tự (
                stack.append(0)
            else: # Là kí tự )
                if stack[-1]== 0: # Khi giá trị cuối là (
                    stack.pop()
                    stack.append(1)

                else:# Khi là số
                    value=0
                    while stack[-1]!= 0:
                        value += stack.pop()
    
                    stack.pop()
                    stack.append(value*2)

        return sum(stack)
    
s =  "(()()())"
Solution().scoreOfParentheses(s)
                        

