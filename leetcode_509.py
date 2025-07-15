class Solution(object):
    def __init__(self):
        self.memo = {} # Dùng để lưu các giá trị mà đã tính toán trước đó 

    def fib(self, n):
        if n in self.memo:
            return self.memo[n]
        if n <= 1:
            return n
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
