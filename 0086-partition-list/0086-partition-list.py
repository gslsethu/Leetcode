# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        r=[]
        r1=[]
        r2=[]
        r3=[]
        current=head
        while current:
            r.append(current.val)
            current=current.next
        if len(r)==0:
            return None
        for i in range(len(r)):
            if r[i]<x:
                r1.append(r[i])
            else:
                r2.append(r[i])
        r3=r1+r2
    
        head1=ListNode(r3[0])
        current1=head1
        for i in range(1,len(r3)):
            current1.next=ListNode(r3[i])
            current1=current1.next
        return head1