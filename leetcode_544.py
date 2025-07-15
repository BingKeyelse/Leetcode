class Solution:
    def findContestMatch(self, n: int) -> str:
    # if n<2 or n>24:
        # return "Error: n is out of the valid range (2 <= n <= 24)"
        # return None
        per_team= [str(i+1) for i in range(n)] 

        while n>1:
            for i in range(n//2):
                per_team[i]= f'({ per_team[i]},{per_team[n-1-i]})'
            n//=2
        return str(per_team[0])

print(Solution().findContestMatch(32))