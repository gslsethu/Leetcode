# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        s=len(l)
        index=s-n
        l.pop(index)

        if len(l)==0:
            return None

        head = ListNode(l[0])
        current = head

        for i in range(1, len(l)):
            current.next = ListNode(l[i])
            current = current.next
        return head
