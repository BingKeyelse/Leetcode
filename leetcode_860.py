import collections
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet=collections.defaultdict(int)

        for bill in bills:
            if bill ==5: # Với số tiền nhỏ chỉ nhận
                wallet[5]+=1
            elif bill==10:
                if wallet[5]==0:
                    return False
                else:
                    wallet[5]-=1
                    wallet[10]+=1
            else:
                if wallet[10]>=1 and wallet[5]>=1:
                    wallet[5]-=1
                    wallet[10]-=1
                    wallet[20]+=1
                elif wallet[5]>=3:
                    wallet[5]-=3
                    wallet[20]+=1
                else:
                    return False
        return True





bills = [5,5,5,10,20]
print(Solution().lemonadeChange(bills))