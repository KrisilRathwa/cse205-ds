class Solution(object):
    def findNumbers(self, nums):
        return len([s for s in nums if len(str(s))%2==0])