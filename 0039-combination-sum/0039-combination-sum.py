class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, current, total):
            if total == target:
                ans.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # i, not i+1 → can reuse same number
                backtrack(i, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)
        return ans
        