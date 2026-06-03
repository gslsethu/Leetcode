class Solution(object):
    def checkPerfectNumber(self, num):
        count=1
        if num==1:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                count=count+i
                if i!=num//i:
                    count+=num//i
        if count==num:
            return True
        else:
            return False

        