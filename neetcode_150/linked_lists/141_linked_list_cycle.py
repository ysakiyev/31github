from typing import Optional
from list_node import ListNode
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = slow.next
        if fast is None:
            return False

        while slow:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next is None or fast.next.next is None:
                return False
            fast = fast.next.next

        return False
