class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       s=[]
       for i in range(len(nums)):
            if nums[i] not in s:
               s.append(nums[i])
            else :
                s.remove(nums[i])
       return s[0]