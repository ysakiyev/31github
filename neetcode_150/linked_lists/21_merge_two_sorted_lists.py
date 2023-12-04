from typing import Optional
from list_node import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = ListNode(0)
        cur = dummy
        cur1, cur2 = list1, list2

        while cur1 is not None and cur2 is not None:
            while cur1 is not None and cur2 is not None and cur1.val <= cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next

            while cur1 is not None and cur2 is not None and cur2.val <= cur1.val:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        while cur1 is not None:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next

        while cur2 is not None:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next

        return dummy.next

