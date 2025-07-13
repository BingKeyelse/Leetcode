class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for sym in s:
            if not stack or sym != stack[-1]:
                stack.append(sym)
                continue
            stack.pop()
        return "".join(stack)
