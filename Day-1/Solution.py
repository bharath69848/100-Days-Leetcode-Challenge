#Finding the Closest number to Zero
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close = nums[0]
        for x in nums:
            if abs(x) < abs(close):
                close = x
        
        if close < 0 and abs(close) in nums:
            return abs(close)
        else:
            return close
#Time Complexity : O(n)
#Space Complexity : O(1)
