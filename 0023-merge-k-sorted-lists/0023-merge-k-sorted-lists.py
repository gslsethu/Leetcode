# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        r1=[]
        for head in lists:
            current=head
            while current:
                r1.append(current.val)
                current=current.next
        r1.sort()
        if len(r1)==0:
            return None
        current1=ListNode(r1[0])
        head1=current1
        for i in range(1,len(r1)):
            current1.next=ListNode(r1[i])
            current1=current1.next
        return head1






