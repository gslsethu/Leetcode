# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        while val in l:
            l.remove(val)
        if len(l)==0:
            return None
        head=ListNode(l[0])
        curr=head
        for i in range(1,len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        return head

        




 

        