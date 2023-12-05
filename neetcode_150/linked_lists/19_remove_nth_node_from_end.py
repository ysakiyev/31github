from typing import Optional
from list_node import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        left, right = head, head

        while n > 0:
            right = right.next
            n -= 1

        prev_left = None

        while right is not None:
            prev_left = left
            left = left.next
            right = right.next

        next_left = left.next
        if prev_left is None:
            head = next_left
        else:
            prev_left.next = next_left

        return head
