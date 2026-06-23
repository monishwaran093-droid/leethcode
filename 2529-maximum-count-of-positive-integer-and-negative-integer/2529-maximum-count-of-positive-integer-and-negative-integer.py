class Solution:
    def maximumCount(self, nums: List[int]) -> int:
         c=0
         n=0
         for i in range(len(nums)):
            if nums[i]>0:
                c+=1
            elif nums[i]<0:
                n+=1
         return max(c,n)