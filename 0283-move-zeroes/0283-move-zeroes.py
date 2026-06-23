class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        d=nums.count(0)
        c=[0]*d
        while 0 in nums:
            nums.remove(0)
        nums[:]=nums+c
        return nums