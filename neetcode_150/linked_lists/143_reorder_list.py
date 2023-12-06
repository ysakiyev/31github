from typing import Optional
from list_node import ListNode

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # first we want to determine the second half of the list
        # to do that we need to get fast pointer to the end of the list and slow to the mid
        slow = head
        fast = head.next
        n = 2

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
            n += 1

            if fast.next is not None:
                fast = fast.next
                n += 1

        head_2 = slow.next
        slow.next = None

        # now we want to reverse the second half of the list
        head_2 = self.reverseList(head_2)

        cur1 = head
        cur2 = head_2

        # start inserting elements of 2nd half between elements of 1st half
        while cur1 is not None and cur2 is not None:
            cur1_next = cur1.next
            cur2_next = cur2.next
            cur1.next = cur2
            cur2.next = cur1_next
            cur1 = cur1_next
            cur2 = cur2_next

        cur = head
        while cur is not None:
            print(cur.val)
            cur = cur.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        return prev
