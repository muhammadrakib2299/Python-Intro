# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            # Detect duplicate sequence
            if curr.next and curr.val == curr.next.val:
                # Skip all nodes with this value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next  # remove entire block
            else:
                prev = prev.next  # move prev only if no duplicate
            
            curr = curr.next
        
        return dummy.next