class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        count = 0

        for ch in s:
            if ch == "(":
                count += 1
                if count > 1:
                    ans += ch
            else:
                count -= 1
                if count > 0:
                    ans += ch

        return ans
        
      