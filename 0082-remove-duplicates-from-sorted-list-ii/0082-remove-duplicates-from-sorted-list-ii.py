# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        current=head
        while current:
            l.append(current.val)
            current=current.next
        if len(l)==0:
            return head
        l1=[]
        for i in l:
            if l.count(i)==1:
                l1.append(i)
        if len(l1)==0:
            return None
        head=ListNode(l1[0])
        current=head
        for j in range(1,len(l1)):
            current.next=ListNode(l1[j])
            current=current.next
        return head