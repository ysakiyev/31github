from typing import Optional
from list_node import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head

        carry = 0
        while l1 and l2:
            dsum = l1.val + l2.val + carry
            carry = dsum // 10
            val = dsum % 10

            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            dsum = l1.val + carry
            carry = dsum // 10
            val = dsum % 10

            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next

        while l2:
            dsum = l2.val + carry
            carry = dsum // 10
            val = dsum % 10

            cur.next = ListNode(val)
            cur = cur.next
            l2 = l2.next

        if carry > 0:
            cur.next = ListNode(carry)

        return head.next
