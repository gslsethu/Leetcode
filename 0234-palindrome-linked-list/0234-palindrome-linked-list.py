# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        result=[]
        current=head
        while(current):
            result.append(current.val)
            current=current.next
        reversed=result[::-1]
        if(reversed==result):
            return True
        else:
            return False
           

        