class Solution:
    def findContestMatch(self, n: int) -> str:
        # Lập trình tại đây
        def generate(aList):
            if len(aList) == 2:
                return aList
            else:
                newList = []
                length = len(aList)
                i = 0
                while i < length // 2:
                    newList.append("({},{})".format(
                        aList[i], aList[length-1-i]))
                    i += 1
            return generate(newList)

        aList = [i for i in range(1, n+1)] # Tạo mảng
        final = generate(aList)

        print("({},{})".format(final[0], final[1]))
        return "({},{})".format(final[0], final[1])
