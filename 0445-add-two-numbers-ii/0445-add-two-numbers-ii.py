# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        current=l1
        while current:
            s1+=str(current.val)
            current=current.next
        s2=""
        current=l2
        while current:
            s2+=str(current.val)
            current=current.next
        s=int(s1)+int(s2)
        if s==0:
            return l1
        l=list(map(int,str(s)))
        head=ListNode(l[0])
        current=head
        for i in range(1,len(l)):
            current.next=ListNode(l[i])
            current=current.next
        return head



        