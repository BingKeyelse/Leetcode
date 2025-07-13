class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        level_high = 0  # tương ứng với '(' là nhu cầu cao vì '(' ta coi như nó làm tham lam
        level_low = 0  # tương ứng với ')' là nhu cầu thấp vì ')' ta coi như là sự thỏa mãn

        for letter in s:
            if letter == '(':  # Tham lam
                level_high += 1  # mức tham lam tăng lên
                level_low += 1  # mức thỏa mãn tương ứng
            elif letter == ')':
                level_high -= 1  # giảm tham lam đi
                level_low -= 1  # giảm tham lam tương ứng
            else:  # tương ứng với '*'
                level_high += 1  # nếu nó là ( thì nó đang tham lam mà
                level_low -= 1  # nếu nó là ) thì nó đang giảm bớt tham lam mà

            # Lúc nào tham lam <0 thì có nghĩa là trừ tham lam đi nhiều quá( siêu thỏa mãn)
            if level_high < 0:
                return False

            if level_low < 0:  # Mức độ thỏa mãn về 0
                level_low = 0
        print(level_high)

        return level_high == 0  # khi thỏa mãn về 0 có nghĩa là chuỗi là cân bằng


Solution().checkValidString(eval(input()))
