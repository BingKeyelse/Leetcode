import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        stack = collections.Counter(secret)
        right_location=0
        count=0

        for i in range(len(secret)): 
            if secret[i]==guess[i]:
                right_location+=1
                count-=1
            if stack.get(str(guess[i])):
                if stack[str(guess[i])]>0:    
                    stack[str(guess[i])]-=1
                    count+=1
        return str(right_location)+'A'+str(count)+'B'

a="1807"
b="7810"
print(Solution().getHint(a,b))
        