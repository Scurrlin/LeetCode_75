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