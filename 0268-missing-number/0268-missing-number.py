class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = len(nums)
        while a > 0: 
            if a not in nums:
                return a 
            else:
                a -= 1
        return a