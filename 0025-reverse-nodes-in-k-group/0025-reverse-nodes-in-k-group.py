# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        l=[]
        curr=head
        leng=k
        while curr:
            l.append(curr.val)
            curr=curr.next
        for i in range(0,len(l),k):
            if i+k<=len(l):
                l[i:i+k]=l[i:i+k][::-1]
        head=ListNode(l[0])
        curr=head
        for i in range(1,len(l)):
            curr.next=ListNode(l[i])
            curr=curr.next
        return head
            

            

            
    
        
        
        