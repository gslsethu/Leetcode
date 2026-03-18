# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        r1=[]
        left=0
        right=1
        current=head
        while current:
            r1.append(current.val)
            current=current.next

        while right<len(r1):
            r1[left],r1[right]=r1[right],r1[left]
            left=left+2
            right=right+2
        if len(r1)==0:
            return None
        head1=ListNode(r1[0])
        current1=head1
        for i in range(1,len(r1)):
            current1.next=ListNode(r1[i])
            current1=current1.next
        return head1


        
        

        
        
       
