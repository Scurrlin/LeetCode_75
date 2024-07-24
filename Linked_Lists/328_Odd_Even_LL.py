# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered
# list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain
# as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time
# complexity.

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = odd_ptr = ListNode(0)
        even = even_ptr = ListNode(0)
        
        while head:
            odd_ptr.next = head
            even_ptr.next = head.next
            
            odd_ptr = odd_ptr.next
            even_ptr = even_ptr.next
            
            head = head.next.next if even_ptr else None
        
        odd_ptr.next = even.next
        return odd.next