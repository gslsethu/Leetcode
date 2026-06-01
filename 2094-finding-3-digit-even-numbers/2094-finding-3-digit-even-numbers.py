class Solution(object):
    def findEvenNumbers(self, digits):
        from itertools import permutations

        res = set()

        for a,b,c in permutations(digits, 3):
            if a==0:
                continue
            
            num = int(a*100 + b *10 + c)
            if num & 1 == 0:

                res.add(num)

        return sorted(res)