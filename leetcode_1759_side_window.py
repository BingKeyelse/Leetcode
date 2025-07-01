class Solution:
    def countHomogenous(self, s: str) -> int:
        count=0
        value=0 

        i=0 # start window
        j=0 # start side 

        while i< len(s):
            while j< len(s) and s[j]==s[i]:
                j+=1
            count=j-i
            value+= count*(count +1)//2
            i=j
        return value 
    
s= "abbcccaa"
print(Solution().countHomogenous(s))




                