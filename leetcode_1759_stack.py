class Solution:
    def countHomogenous(self, s: str) -> int:
        arr= []

        for letter in s:
            if not arr:
                arr.append([letter,1])
            else:
                if letter == arr[-1][0]:
                    arr[-1][1]+=1
                else:
                    arr.append([letter,1])
        sum=0
        for i in range(len(arr)):
            sum+= arr[i][1]*( arr[i][1] +1)//2
        return sum

s = "abbcccaa"
Solution().countHomogenous(s)