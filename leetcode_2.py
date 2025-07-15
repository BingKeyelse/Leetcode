# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        vals_1 = []
        while l1:
            vals_1.append(l1.val)
            l1 = l1.next

        vals_2 = []
        while l2:
            vals_2.append(l2.val)
            l2 = l2.next
        result = []
        pre = 0
       

        for i in range(max(len(vals_1), len(vals_2))):
            if vals_1[i]+vals_2[i]+pre > 9:
                result.append((vals_1[i]+vals_2[i]+pre) % 10)
                pre = (vals_1[i]+vals_2[i]+pre)//10
                

            else:
                result.append((vals_1[i]+vals_2[i]+pre) % 10)
                pre=0

        if pre > 0:
            result.append(pre)
        print(result)
        return result
a=[2,4,3]
b=[5,6,4]
Solution().addTwoNumbers(a,b)
