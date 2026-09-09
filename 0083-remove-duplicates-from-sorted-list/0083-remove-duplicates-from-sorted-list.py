# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        while c:
            n=c.next
            if n and n.val==c.val:
                c.next=n.next
            else:
                c=n
        return head