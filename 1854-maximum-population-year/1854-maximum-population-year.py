class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        ans=1950
        max_population=0
        for year in range(1950,2051):
            population=0
            for birth,death in logs:
                if birth<=year<death:
                    population+=1
                if max_population<population:
                    max_population=population
                    ans=year
        return ans
                
        