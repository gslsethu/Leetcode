# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        r1=[]
        current=head
        while current:
            r1.append(current.val)
            current=current.next
        r1.reverse()
        if len(r1)==0:
            return None
        head1=ListNode(r1[0])
        current1=head1
        for i in range(1,len(r1)):
            current1.next=ListNode(r1[i])
            current1=current1.next
        return head1

        