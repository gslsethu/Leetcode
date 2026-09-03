class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for s, e in intervals:

            if e < newInterval[0]:
                ans.append([s, e])

            elif s > newInterval[1]:
                ans.append(newInterval)
                newInterval = [s, e]

            else:
                newInterval[0] = min(newInterval[0], s)
                newInterval[1] = max(newInterval[1], e)

        ans.append(newInterval)
        return ans
        