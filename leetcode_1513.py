class Solution:
    def numSub(self, s: str) -> int:
        count =0
        value=0

        for i in range (0,len(s)):
            if i==0:
                if s[i]=='1':
                    count+=1
            else:
                if s[i]==s[i-1] and s[i]=='1':
                    count+=1
                else:
                    if s[i]=='1':
                        count=1
                    else:
                        count=0
            value+=count
        return value 
    
s="0110111"
print(Solution().numSub(s))