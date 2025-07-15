class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        store={}
        def caculate(i):
            if i <=0:
                return 0
            if i==1 or i==2:
                return 1
            if i in store:
                return store[i]
            store[i]= caculate(i-1) = caculate(i-2) + caculate(i-3)

            return store[n]
        return callable(n)