from collections import Counter

class Solution(object):
    def balancedString(self, s):
        n = len(s)
        max_value = n // 4
        count = Counter(s)
        
        # Nếu đã balanced thì trả về 0
        if all(count[c] == max_value for c in 'QWER'):
            return 0

        res = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            # Khi nào tất cả ký tự đều <= max_value thì thử cập nhật kết quả
            while left < n and all(count[c] <= max_value for c in 'QWER'):
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res
    
print(Solution().balancedString(eval(input())))