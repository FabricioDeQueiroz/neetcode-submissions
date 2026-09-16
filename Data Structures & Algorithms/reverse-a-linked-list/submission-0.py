# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        actual = head
        prev = None

        while actual is not None:
            n_next = actual.next
            
            actual.next = prev

            prev = actual
            
            actual = n_next
        
        return prev