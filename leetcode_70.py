
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {} # Dùng để lưu 
        def count_step(step_left):
            if step_left==0: # hết bước chân rồi 
                return 1
            
            if step_left < 0:
                return 0
            
            if step_left in memo: # Nếu đã được tính toán rồi thì trả lại giá trị luôn
                return memo[step_left]
            
            memo[step_left] = count_step(step_left - 1) + count_step(step_left - 2)
            return memo[step_left]
            
        sum= count_step(n)
        print(sum)
        return sum