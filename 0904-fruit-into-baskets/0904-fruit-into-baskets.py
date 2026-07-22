class Solution(object):
    def totalFruit(self, fruits):
        left=0
        fruit={}
        max_fruit=0
        for right in range(len(fruits)):
            if fruits[right] in fruit:
                fruit[fruits[right]]+=1
            elif fruits[right] not in fruit and len(fruit)<2:
                fruit[fruits[right]]=1
            else:
                while len(fruit)>=2:
                    fruit[fruits[left]]-=1
                    if fruit[fruits[left]]==0:
                        del fruit[fruits[left]]
                    left+=1
                fruit[fruits[right]]=1    
                
            max_fruit=max(max_fruit,right-left+1)
        return max_fruit