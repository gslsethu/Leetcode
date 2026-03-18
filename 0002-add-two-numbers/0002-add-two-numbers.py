# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        r1=[]
        r2=[]
        current1=l1
        while current1:
            r1.append(current1.val)
            current1=current1.next
        current2=l2
        while current2:
            r2.append(current2.val)
            current2=current2.next
        r1.reverse()
        r2.reverse()
        num1="".join(map(str,r1))
        num2="".join(map(str,r2))
        num3=int(num1)+int(num2)
        num4=list(map(int, str(num3)))
        num4.reverse()
        head=ListNode(num4[0])
        current=head
        for i in range(1,len(num4)):
            current.next=ListNode(num4[i])
            current=current.next
        return head

        
        