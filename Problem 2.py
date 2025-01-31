# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int):
        dummy = ListNode(-1, head)

        p1 = dummy
        p2 = dummy

        while (n > 0):
            p2 = p2.next
            n -= 1

        while (p2.next != None):
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return dummy.next

# TC: O(N)
# TC: O(1)
