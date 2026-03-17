# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        r1=[]
        r2=[]
        current1=list1
        while current1:
            r1.append(current1.val)
            current1=current1.next
        current2=list2
        while current2:
            r2.append(current2.val)
            current2=current2.next
        r3=r1+r2
        r3.sort()
        if len(r3)==0:
            return None
        head =ListNode(r3[0])
        current = head
       
        

    
        for i in range(1, len(r3)):
            current.next = ListNode(r3[i])
            current = current.next

        return head
        
        
        
        