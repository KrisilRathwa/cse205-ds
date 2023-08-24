class Solution(object):
    def sumOfMultiples(self, n):
        sum_all=0
        for i in range(1,n+1):
            if (i%3==0 or i%5==0 or i%7==0):
                sum_all=sum_all+i
        return sum_all 