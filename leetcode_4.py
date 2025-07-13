from collections import Counter

class Solution(object):
    def balancedString(self, s):
        count= Counter(s)
        left=0
        result=len(s)
        maximum= len(s)//4

        if all(count[letter] == maximum for letter in 'QWER'):
            print(0)
            return 0
        
        

        for index, let in enumerate(s):
            count[let]-=1
            while left < len(s) and all(count[letter] <= maximum for letter in 'QWER'):
                result=min(result, index-left+1)
                count[s[left]]+=1
                left+=1

        print(result)
        return result
                
# s= "QQQW"
# Solution().balancedString(s)

        
        
Solution().balancedString(eval(input()))