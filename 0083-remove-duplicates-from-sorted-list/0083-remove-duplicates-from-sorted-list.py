# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        result=[]
        current=head
        while current:
            result.append(current.val)
            current=current.next
        result=list(set(result))
        result.sort()
        if len(result)==0:
            return None
        head=ListNode(result[0])
        curr=head
        for i in range(1,len(result)):
            curr.next=ListNode(result[i])
            curr=curr.next
        return head
        

    
