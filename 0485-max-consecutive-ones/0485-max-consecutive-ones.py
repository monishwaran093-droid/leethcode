class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
         c=0
         d=0
         for i in nums:
            if i==1:
                d+=1
            else:
                c=max(c,d)
                d=0
         return max(c,d)