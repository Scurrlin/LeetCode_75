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
        list = []
        current = head
        while current:
            list.append(current.val)
            current = current.next
        
        i, maxSum = 0, 0
        while i < (len(list) // 2):
            currSum = list[i] + list[-(i + 1)]
            if currSum > maxSum:
                maxSum = currSum
            i += 1
        return maxSum