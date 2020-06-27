class solution:
    def ispalindrome(self, head: ListNode) -> bool:

        if head is none:
            return True
        slow,fast = head, head
        stk = []

        while fast and fast.next:
            stk.append(slow.val)

            slow = slow.next
            fast = fast.next.next

        if fast:
            slow  = slow.next
        while (slow and len(stk)):
            if stk.pop() != slow.val:
                return False
            slow = slow.next
        return True
