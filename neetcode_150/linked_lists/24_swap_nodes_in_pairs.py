from typing import Optional
from list_node import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        adj_node = head.next
        next_node = adj_node.next
        adj_node.next = head
        head.next = next_node

        head.next = self.swapPairs(head.next)

        return adj_node