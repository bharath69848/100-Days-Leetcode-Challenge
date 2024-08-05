#Time Complexity : O(n)
#space Complexity : O(1)

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close = nums[0]
        for i in nums:
            if abs(i) < abs(close):
                close = i
        
        if close < 0 and abs(close) in nums:
            return abs(close)
        else:
            return close