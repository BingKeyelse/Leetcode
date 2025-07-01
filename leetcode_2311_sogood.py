class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 1  # tương ứng với 2^0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if value + power <= k:
                    value += power
                    count += 1
                # nếu không thì bỏ qua bit '1' này

            power *= 2
            if power > k:
                break  # các bit tiếp theo sẽ có giá trị quá lớn

        # đếm thêm các '0' bên trái chưa xét tới (vì '0' luôn giữ được)
        for j in range(i-1, -1, -1):
            if s[j] == '0':
                count += 1
        return count

a="00101001"
k=1
print(Solution().longestSubsequence(a,k))