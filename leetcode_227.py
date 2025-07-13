class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        num = 0
        sign='+'

        for idx, cur in enumerate(s):
            if cur.isdigit():
                num= num*10 + int(cur)

            if cur in '+-*/' or  idx== len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign =='-':
                    stack.append(-num)
                elif sign=='*':
                    stack[-1]= stack[-1]*num
                else:
                    stack[-1]= int(stack[-1]/float(num))

                num=0 # Gặp dấu thì phải reset về 0
                sign= cur
        return sum(stack)