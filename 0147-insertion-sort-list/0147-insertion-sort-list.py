# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        r=[]
        current=head
        while current:
            r.append(current.val)
            current=current.next
        r.sort()
        if len(r)==0:
            return None
        head1=ListNode(r[0])
        current1=head1
        for i in range(1,len(r)):
            current1.next=ListNode(r[i])
            current1=current1.next
        return head1
            