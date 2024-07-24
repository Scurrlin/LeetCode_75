# In a linked list of size n, where n is even, the ith node (0-indexed) of the
# linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) -
# 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
# twin of node 2. These are the only nodes with twins for n = 4. The twin sum is
# defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum
# of the linked list.

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        return res