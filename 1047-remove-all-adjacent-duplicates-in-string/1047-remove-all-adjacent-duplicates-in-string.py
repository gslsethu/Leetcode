class Solution(object):
    def removeDuplicates(self, s):
        stack=[]
        for ch in s:
            if len(stack)==0:
                stack.append(ch)
            elif stack[-1]==ch:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)
        
        