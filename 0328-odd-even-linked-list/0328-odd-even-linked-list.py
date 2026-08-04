# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        current=head
        while current:
            l.append(current.val)
            current=current.next
        if len(l)==0:
            return head
        l1=l[::2]
        l2=l[1::2]
        l1.extend(l2)

        head=ListNode(l1[0])
        current=head
        for i in range(1,len(l1)):
            current.next=ListNode(l1[i])
            current=current.next
        return head
