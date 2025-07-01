# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        ## Chuyển đổi head sang list
        vals = []
        while head:
            vals.append(head.val)
            head = head.next

        i=0
        j= len(vals)-1
        while i<j:
            if vals[i] != vals[j]:
                return False
            i=i+1
            j=j-1
        return True
        