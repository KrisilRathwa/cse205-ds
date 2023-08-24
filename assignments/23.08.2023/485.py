class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        num1=0
        num2=0
        for i in range(0, len(nums)):
            if nums[i]==1:
                num1=num1+1
                if num1>num2:
                    num2=num1
            else:
                num1=0
        return num2