# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l=[]
        current=head
        while current:
            l.append(current.val)
            current=current.next
        if len(l)==1 or len(l)==0:
            return head
        
        
        l[left-1:right]=l[left-1:right][::-1]
        head=ListNode(l[0])
        current=head
        for i in range(1,len(l)):
            current.next=ListNode(l[i])
            current=current.next
        return head

        