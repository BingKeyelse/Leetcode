class Solution:
    def countHomogenous(self, s: str) -> int:
        count=1
        value=1
        MOD= 10**9 +7

        for i in range(1,len(s)):
            if s[i]== s[i-1]:
                value+=1
            else: 
                value=1
            count+=value
        return count%MOD