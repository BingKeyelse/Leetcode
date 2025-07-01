class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list= list(s)
        leng= len(s_list)

        swap=0

        for i in range(0, leng, 2*k):
            swap= min(k, leng-i)
            s_list[i:i+swap]=s_list[i:i+swap][::-1]
            # print(s_list)
        return "".join(s_list)

test= "abcdefg"
k=2
print(Solution().reverseStr(test,k))

        
