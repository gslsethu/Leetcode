# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        l=[]
        while(head):
            l.append(head.val)
            head=head.next
        if len(l)==0:
            return None
        s=len(l)
        
        l[k-1],l[s-k]=l[s-k],l[k-1]

        head=ListNode(l[0])
        curr=head
        for i in range(1, len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        return head


      
    





