from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head = ListNode(val=0, next=head)
        current_nth = current = head

        for _ in range(n):
            current = current.next
        while current.next:
            current = current.next
            current_nth = current_nth.next

        current_nth.next = current_nth.next.next

        return head.next
