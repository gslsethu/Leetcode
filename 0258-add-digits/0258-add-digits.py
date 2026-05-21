class Solution(object):
    def addDigits(self, num):
    
    
        count = 0
        if len(str(num))>1:
            for i in range(len(str(num))):
                digit=num%10
                count=count+digit
                num=num//10
            if len(str(count))>1:
                return self.addDigits(count)
            else: 
                return count
        else:
            return num
        
        