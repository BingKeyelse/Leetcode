class Solution(object):
    def getHint(self, secret, guess):
        bulls = 0
        cows = 0

        # Dùng 2 bảng đếm cho chữ số 0–9
        secret_count = [0] * 10
        guess_count = [0] * 10

        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1

        # Đếm cows: chữ số trùng nhưng sai vị trí
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return str(bulls) + 'A' + str(cows) + 'B'
