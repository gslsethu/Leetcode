class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for ch in operations:
            if ch not in "CD+":
                stack.append(int(ch))
            else:
                if ch=="C":
                    stack.pop()
                elif ch=="D":
                    stack.append(2*stack[-1])
                else:
                    stack.append(stack[-1]+stack[-2])
        return sum(stack)
                
